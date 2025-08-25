import os, json, pathlib
from dataclasses import dataclass
from typing import List, Tuple
from dotenv import load_dotenv
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

load_dotenv()

EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
TOP_K = int(os.getenv("TOP_K", 4))

@dataclass
class Chunk:
    text: str
    meta: dict

class VectorStore:
    def __init__(self, index_dir: str):
        self.index_dir = pathlib.Path(index_dir)
        self.index_dir.mkdir(parents=True, exist_ok=True)
        self.index_path = self.index_dir / "faiss.index"
        self.meta_path = self.index_dir / "meta.jsonl"
        self.model = SentenceTransformer(EMBED_MODEL)
        self.index = None
        self.metas: List[dict] = []
        self._load()

    def _load(self):
        if self.index_path.exists() and self.meta_path.exists():
            self.index = faiss.read_index(str(self.index_path))
            with open(self.meta_path, "r", encoding="utf-8") as f:
                self.metas = [json.loads(line) for line in f]

    def search(self, query: str, k: int = TOP_K) -> List[Chunk]:
        if self.index is None:
            raise RuntimeError("Index not found. Run scripts/ingest.py first.")
        q_emb = self.model.encode([query])
        D, I = self.index.search(np.array(q_emb, dtype="float32"), k)
        chunks = []
        for idx in I[0]:
            meta = self.metas[idx]
            chunks.append(Chunk(text=meta["text"], meta=meta))
        return chunks
