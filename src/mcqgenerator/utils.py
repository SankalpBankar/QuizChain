import os
import pypdf
import json
import traceback

# Optional JSON repair fallback
try:
    from json_repair import repair_json  # type: ignore
except Exception:
    repair_json = None


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            # pypdf >= 3 uses PdfReader
            pdf_reader = getattr(pypdf, "PdfReader", None)
            if pdf_reader is None:
                # fallback for very old versions
                pdf_reader = pypdf.PdfFileReader  # type: ignore[attr-defined]
                reader = pdf_reader(file)
                pages = reader.pages
            else:
                reader = pdf_reader(file)
                pages = reader.pages

            text = ""
            for page in pages:
                extracted = page.extract_text() or ""
                text += extracted
            return text

        except Exception as e:
            raise Exception("error reading the PDF file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "unsupported file format only pdf and text file supported"
        )
    

def get_table_data(quiz_str):
    try:
        # Accept dicts or strings; strip any markdown fences and isolate JSON
        if isinstance(quiz_str, dict):
            quiz_dict = quiz_str
        else:
            raw = str(quiz_str).strip()
            # remove ```json / ``` fences if present
            if raw.startswith("```"):
                raw = raw.strip("`")
                # drop a potential leading language token like 'json' on the first line
                first_nl = raw.find("\n")
                if first_nl != -1:
                    raw = raw[first_nl+1:]
            # extract the outermost JSON object
            start = raw.find("{")
            end = raw.rfind("}")
            if start != -1 and end != -1 and end > start:
                raw = raw[start:end+1]
            try:
                quiz_dict=json.loads(raw)
            except Exception:
                if repair_json is not None:
                    fixed = repair_json(raw)
                    quiz_dict = json.loads(fixed)
                else:
                    raise
        quiz_table_data=[]

        #iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq=value["mcq"]
            options=" || ".join(
                [
                    f"{option}-> {option_value}" for option, option_value in value["options"].items()
                ]
            )

            correct=value["correct"]
            quiz_table_data.append({"MCQ":mcq, "Choices": options, "Correct": correct})

        # return AFTER processing all items
        return quiz_table_data
        
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return []
