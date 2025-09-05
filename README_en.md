Pour la version en français, [Cliquez ici](README.md)

# Automatic Analysis of Digital Form Responses

🎓 Final Year Project – Computer Engineering  
👨‍💻 Author: Tayo Tate Desmond Corentin  
📌 Objective: Automate the analysis of open-ended form responses to save time and extract actionable insights.  

---

## 🚀 Features

The application provides 3 main features:

1. **Form Goal Detection**
   - Analyzes form questions to determine the main objective
   - Categories: Customer Satisfaction, Market Research, Performance Analysis, Event Planning, Other

2. **Automatic Summarization of Open-Ended Responses**
   - Abstractively summarizes collected responses
   - Helps quickly identify key points expressed by users

3. **Intelligent Chatbot**
   - Answers questions based solely on imported form data
   - Enables instant interaction with collected responses

---

## 🛠️ Technologies Used

- **Languages & Frameworks** : Python, Streamlit
- **Data** : Pandas, JSON
- **LLM** : Ollama (local), Hugging Face (online)
- **NLP** : Transformers, NLTK, spaCy (optional preprocessing)
- **APIs & Environments** : Hugging Face Inference API, Python-dotenv

---

## 📂 Project Structure

```text
form-response-analyzer/
│── app.py # Streamlit main Script
│── requirements.txt # Python Dependancies
│── .env # Environments variables (API keys)
│── README_en.md # Project Documentation
│── 📂 src/
│   └── llm_helper.py # Abstraction for LLM (local or Hugging Face)
│── 📂 data/ # Examples of unamed datas
│   ├── sample_data_chatbot.json
│   ├── sample_data_form_goal.json
│   ├── sample_data_summarization1.json
│   ├── sample_data_summarization2.json
│   └── test_data_for_form_goal.json
│── 📂 notebooks/ # Notebooks for experiments
│   ├── chatbot.ipynb
│   └── form_goal.ipynb
```

---

## ⚡ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/automatic-form-analysis.git
cd automatic-form-analysis
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv # Linux / macOS
source venv/bin/activate # Windows
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a .env file with your API keys**
```bash
# Hugging Face Inference API key
HF_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxx
```

5. **🏃‍♂️ Run the application**
```bash
streamlit run app.py
```

* The Streamlit interface will open in your browser.
* You can choose a feature from the sidebar and upload your CSV/JSON files.

---

## 📌 Example Usage

1. **Form Goal Detection**

* Upload a questions.csv or questions.json file
* Click “Analyze Goal” → result displayed directly

2. **Automatic Summarization**

* Upload a responses.json file containing open-ended responses
* Click “Generate Summary” → abstract summary generated

3. **Intelligent Chatbot**

* Upload a CSV/JSON file with form data
* Ask questions in the text field → chatbot responds based solely on your data

---

## 🔗 Useful Links

- [Hugging Face Models – Mistral](https://huggingface.co/models)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## 📓 Colab Notebooks

To better understand functionality and prototyping, two Colab notebooks are available:

1. **Chatbot RAG (Retrieval-Augmented Generation)**
   - Prototype of the intelligent chatbot using form data
   - Explores RAG logic and model interactions
   - [Open in Colab](https://colab.research.google.com/drive/19Gdn3ychZTzWUWjaVR2pHmYwREOjjkmR?usp=sharing)  

2. **Form Goal Detection**
   - Notebook demonstrating automatic question analysis
   - Allows testing goal extraction with different datasets
   -[Open in Colab](https://colab.research.google.com/drive/12E6Mj7iUW6MMUluLj9NZX9b8gCGrLHjX?usp=sharing)  

---

## 📜 License

This project is licensed under the MIT License.
Free to use, modify, and distribute.


---
