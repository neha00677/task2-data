import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

class FAQRetriever:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path).dropna(subset=["question", "answer"])
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(self.df["question"].tolist(), show_progress_bar=True)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def retrieve(self, query, top_k=3):
        query_vec = self.model.encode([query])
        _, indices = self.index.search(query_vec, top_k)
        return self.df.iloc[indices[0]]
