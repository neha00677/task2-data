import streamlit as st
from retriever import FAQRetriever
from generator import build_prompt, generate_answer

st.set_page_config(page_title="Aurora Skies Chatbot", layout="centered")
st.title("Aurora Skies Airways Chatbot")

query = st.text_input("Ask your question:")
if query:
    retriever = FAQRetriever("data/airline_faq.csv")
    faqs = retriever.retrieve(query)
    prompt = build_prompt(query, faqs)
    answer = generate_answer(prompt)
    st.markdown("### Answer")
    st.write(answer)
