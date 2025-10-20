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

## ⚙️ Setup & Installation for RAGforGeeks 🧠💬
Follow these steps to set up and run your RAG-based chatbot:
