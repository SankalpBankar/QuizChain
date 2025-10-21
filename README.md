# 🧠 QuizChain 🎯⚡
An intelligent MCQ (Multiple Choice Question) generation system powered by LangChain and Groq, wrapped in an interactive Streamlit interface.
QuizChain can automatically generate, evaluate, and refine quiz questions from any given text — making it a perfect tool for students, educators, and AI enthusiasts.


## 📁 Project Directory Structure 🧠💬

```
QuizChain/
├── env/                   # 🐍 Virtual environment
├── experiment/            # 🧪 Data and analysis
│   ├── machinelearning.csv # 📊 The primary dataset
│   └── mcq.ipynb          # 📓 Jupyter notebook for ML/prototyping
|
├── src/                   # 💻 Source code
│   └── mcqgenerator/
│       ├── __init__.py    # 📦 Package initializer
│       ├── logger.py      # 📜 For application logging
│       ├── MCQGenerator.py # ✨ CORE LOGIC: MCQ generation class/functions
│       └── utils.py       # 🛠️ Helper functions
|
├── StreamlitAPP.py # 🚀 MAIN ENTRY POINT: The user interface
├── .env # 🔑 Environment variables (e.g., API keys)
├── requirements.txt # ✅ List of all necessary Python libraries
├── response.json          # 📩 Example/template for the desired JSON output
└── README.md              # 📖 Project description and setup instructions
```

## 💡 Tech Stack 🛠️
- **Python** 🐍 — Core programming language for logic and data handling
- **Streamlit** 🌐 — For building the interactive web interface
- **LangChain** 🔗 — Framework for orchestrating LLM-based MCQ generation
- **Groq API** ⚡ — High-speed inference for question and answer generation
- **Pandas / JSON / dotenv** 📄 — For data management and configuration

---

## ⚙️ Setup & Installation for QuizChain 🎯⚡
Follow these steps to set up and run your RAG-based chatbot:
### 1️⃣ Clone the Repository 📥
```sh
git clone https://github.com/SankalpBankar/QuizChain.git
cd QuizChain
```

### 2️⃣ Install Dependencies 📦
```sh
pip install -r requirements.txt
```


### 3️⃣ Set Up Environment Variables 🔑
Create a .env file in the root directory
Add your API key:
```sh
GROQ_API_KEY=groq_api_key
```

### 4️⃣ Load the LLM (LLaMA3.1) 🦙
The code uses LangChain + Groq to load the model:
```sh
groq_api_key=os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    groq_api_key=groq_api_key,  
    model_name="llama-3.1-8b-instant",
    temperature=0.2        
)
```

### 5️⃣ Run the Streamlit App 🚀
Ensure you have all backend files and Streamlit app ready. Then run:
```sh
streamlit run StreamlitAPP.py
```
Your browser will open the app at http://localhost:8505


## 🛠️ Troubleshooting 🚨
•	API Key Error
Set your key using:
```sh
os.environ["GROQ_API_KEY"] = "groq_api_key"
```

• Streamlit App not running
If the command fails or you get ModuleNotFoundError.
Ensure dependencies are installed and environment is active:
```sh
# 1. Activate your environment
source env/bin/activate
# 2. Re-install all dependencies
pip install -r requirements.txt
```



