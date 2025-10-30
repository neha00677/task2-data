# Aurora Skies Airways Chatbot

A lightweight FAQ chatbot built with Streamlit and Groq’s model. It answers common airline questions using semantic search and real-time LLM responses.

## 🚀 Features
- Real-time answer generation via Groq API
- Clean Streamlit UI with instant response
- Easy CSV-based FAQ management

## 📸 Screenshot

![Chatbot Interface]()

## ⚙️ How to Run Locally
- Create a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

- Install dependencies
pip install -r requirements.txt

- Create a .env file:
GROQ_API_KEY=your-groq-api-key-here

- Run
  python -m streamlit run app.py

## 📝 Sample Questions
These are pulled directly from `data/airline_faq.csv`
