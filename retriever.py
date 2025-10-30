import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class SimpleFAQRetriever:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path).dropna(subset=["question", "answer"])
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(self.df["question"].tolist())

    def retrieve(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = similarities.argsort()[-top_k:][::-1]
        return self.df.iloc[top_indices]
