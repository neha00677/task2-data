import streamlit as st
from retriever import SimpleFAQRetriever
from generator import build_prompt, generate_answer
import pandas as pd

faq_df = pd.read_csv("data/airline_faq.csv").dropna(subset=["question", "answer"])
popular_questions = faq_df["question"].tolist()
if "user_query" not in st.session_state:
    st.session_state.user_query = ""
st.set_page_config(page_title="Aurora Skies Chatbot", layout="centered")
st.title("Aurora Skies Airways Chatbot")

query = st.text_input("Ask your question:", key="user_query")

if query:
    retriever = SimpleFAQRetriever("data/airline_faq.csv")
    faqs = retriever.retrieve(query)
    prompt = build_prompt(query, faqs)
    answer = generate_answer(prompt)
    st.markdown("### Answer")
    st.write(answer)
with st.sidebar:
    st.markdown("### Random Questions")

    def inject_question(q):
        st.session_state.user_query = q

    for q in popular_questions:
        st.button(q, on_click=inject_question, args=(q,))
