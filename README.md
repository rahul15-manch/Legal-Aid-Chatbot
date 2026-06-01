# ⚖️ LegiSense – AI-Powered Legal Aid Advisor  

## 📖 Overview  
**LegiSense** is an **AI-powered legal assistance platform** that makes legal help more **accessible, affordable, and efficient**.  
It combines **automation, AI, and law** into a single, easy-to-use application.  

![FAQ Animation](https://raw.githubusercontent.com/rahul15-manch/Legal-Aid-Chatbot/refs/heads/main/Yellow%20Green%20and%20Pink%20Colorful%20Faq%20Animated%20Social%20Media.gif)


## 🚀 Tech Stack

### 🖥️ Frontend
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

### 🧠 AI / ML
![LangChain](https://img.shields.io/badge/LangChain-0E76A8?style=for-the-badge&logo=chainlink&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-2E86C1?style=for-the-badge&logo=vector&logoColor=white)
![Sentence Transformers](https://img.shields.io/badge/Sentence%20Transformers-6C63FF?style=for-the-badge&logo=transformer&logoColor=white)
![Transformers](https://img.shields.io/badge/HuggingFace%20Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

### 📄 Document & Data Processing
![PyPDF2](https://img.shields.io/badge/PyPDF2-003B57?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)
![pdfplumber](https://img.shields.io/badge/pdfplumber-FF6F00?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)
![fpdf](https://img.shields.io/badge/fpdf-FFB300?style=for-the-badge&logo=pdf&logoColor=black)
![python-docx](https://img.shields.io/badge/python--docx-4B8BBE?style=for-the-badge&logo=microsoftword&logoColor=white)
![docx2txt](https://img.shields.io/badge/docx2txt-2E86C1?style=for-the-badge&logo=microsoftword&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=python&logoColor=white)

### 🗄️ Database
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FCA121?style=for-the-badge&logo=python&logoColor=white)

### ⚙️ Utilities
![dotenv](https://img.shields.io/badge/dotenv-000000?style=for-the-badge&logo=dotenv&logoColor=white)
![accelerate](https://img.shields.io/badge/accelerate-FF6F00?style=for-the-badge&logo=lightning&logoColor=white)
![streamlit_option_menu](https://img.shields.io/badge/Streamlit%20Option%20Menu-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![streamlit_mic_recorder](https://img.shields.io/badge/Streamlit%20Mic%20Recorder-FF4B4B?style=for-the-badge&logo=microphone&logoColor=white)

## Architecture
```mermaid
graph TD

    A[Legal Assistant Application]

    A --> B[data/]
    A --> C[my_app/]
    A --> D[scripts/]
    A --> E[Core Files]

    %% Scripts
    D --> D1[ingest.py]
    D --> D2[pdf_txt.py]

    %% Core Application Files
    E --> E1[app.py]
    E --> E2[rag_core.py]
    E --> E3[llm_providers.py]
    E --> E4[prompts.py]
    E --> E5[accuracy.py]
    E --> E6[faq.py]
    E --> E7[affidavit_template.py]

    %% Database
    E --> F[(lawyers.db)]

    %% Testing
    E --> G[Testing]
    G --> G1[test_llm.py]
    G --> G2[test_retrival.py]

    %% Config
    E --> H[requirements.txt]
    E --> I[README.md]
    E --> J[.gitignore]

    %% Functional Flow
    D1 --> K[Document Processing]
    D2 --> K

    K --> E2

    E2 --> E3
    E2 --> E4

    E3 --> L[Hugging Face LLM]

    E2 --> M[Legal Knowledge Retrieval]

    M --> E1

    E6 --> E1
    E7 --> E1

    F --> N[Lawyer Registration]
    F --> O[Lawyer Search]

    N --> E1
    O --> E1

    E5 --> P[Accuracy Evaluation]
    P --> E3

    %% UI
    E1 --> Q[Streamlit / Web Interface]

    Q --> R[FAQ Generation]
    Q --> S[Affidavit Creation]
    Q --> T[RTI Assistance]
    Q --> U[Customer Dispute Support]
    Q --> V[Lawyer Recommendation]
```
---

## 🔑 Features  
- 🤖 **Legal Chatbot** – Provides instant answers to basic legal queries using NLP.  
- 📄 **Affidavit Generator** – Automatically generates structured affidavits.  
- 📝 **RTI & Consumer Dispute Generator** – Helps draft RTI applications & consumer complaints.  
- 📚 **Legal Summarizer** – Summarizes long legal documents into concise insights.  
- 👨‍⚖️ **Lawyer Directory** –  
  - Lawyers can **register** with details (specialization, experience, fees, location).  
  - Clients can **search & connect** with filters like specialization, fees, experience, rating.  

---

## 🛠️ Tech Stack  
- **Frontend / UI**: [Streamlit](https://streamlit.io/)  
- **Database**: [SQLite](https://www.sqlite.org/index.html)   
- **Version Control & Collaboration**: [GitHub](https://github.com/) 

---

## 🚀 Getting Started  

### Clone the Repository  
```bash
git clone https://github.com/your-username/LegiSense.git
```
### Set Up Virtual Environment
```
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate
```
### Install Dependencies
```
pip install -r requirements.txt
```

### Run the App
```
streamlit run my_app/streamlit_app.py
```
## 🌍 Vision

LegiSense aims to bridge the gap between citizens and legal help by combining AI automation with expert legal knowledge, empowering individuals to get the right assistance without unnecessary hurdles.

## 🌐 Connect with Me  and My team 
  
Meet the amazing team behind **LegiSense** 🚀  

| Name            | Role                          | LinkedIn |
|-----------------|-------------------------------|----------|
| Kashish Rana    | App Deployment                | [![LinkedIn](https://img.shields.io/badge/-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kashish-rana-6116691b5/) |
| Rahul Manchanda | Backend & Model Training      | [![LinkedIn](https://img.shields.io/badge/-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahul-manchanda-3959b120a/) |
| Tanishka Mukhi  | Data Preprocessing & Collection | [![LinkedIn](https://img.shields.io/badge/-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tanishka-mukhi09/) |


---




