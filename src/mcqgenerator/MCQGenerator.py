import os
import json
import pandas as pd
import traceback
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging

#importing necessary packages from langchain
from langchain_groq import ChatGroq  # correct Groq import
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Load environment variables from the .env file
load_dotenv()

#Access the environment variables just like you would with os.environ
groq_api_key=os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=groq_api_key,  # replace with your actual key
    model_name="llama-3.1-8b-instant",
    temperature=0.2         # lower temperature for more deterministic outputs
)

TEMPLATE="""
CONTEXT TEXT:
{text}

Task: You are an expert MCQ maker. Create a quiz of exactly {number} multiple choice questions
for {subject} students in a {tone} tone.

Hard requirements:
- The output MUST be a single JSON object only (no prose, no backticks), matching RESPONSE_JSON.
- Produce EXACTLY {number} MCQs. If you produce fewer, add more; if more, trim to exactly {number}.
- Keep the language and difficulty aligned to the requested {tone} tone.
- Do not repeat questions; ensure every question is grounded in the context.

RESPONSE_JSON to follow:
{response_json}
"""
quiz_generation_prompt=PromptTemplate(
    input_variables=["text","number","subject","tone","response_json"],
    template=TEMPLATE 
)

quiz_chain=LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

TEMPLATE2="""
You are an expert English grammarian and assessment designer.
Given a Multiple Choice Quiz for {subject} students, evaluate whether the quiz matches the requested
"{tone}" complexity. In at most 50 words, provide a concise assessment.
If the tone does not match "{tone}", minimally edit questions to match the tone while preserving correctness.

Quiz_MCQs JSON:
{quiz}
"""

quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "tone", "quiz"], template=TEMPLATE2)


review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

#This is an Overall Chain where we run the two chains in Sequence
generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=["text", "number", "subject", "tone", "response_json"],
    output_variables=["quiz", "review"],
    verbose=True
)



