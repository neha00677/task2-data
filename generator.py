import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_prompt(query, retrieved_faqs):
    context = "\n\n".join(
        f"Q: {row['question']}\nA: {row['answer']}" for _, row in retrieved_faqs.iterrows()
    )
    return f"""You are a helpful assistant for Skies.
Use the following FAQs to answer the customer query accurately and avoid hallucinations.

FAQs:
{context}
Customer Query: {query}
Answer:"""

def generate_answer(prompt):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
    )
    return chat_completion.choices[0].message.content
