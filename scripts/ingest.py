import os
import glob
from pathlib import Path
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# ---------------------------
# Configuration
# ---------------------------
RAW_DIR = "data/raw"
INDEX_DIR = "data/index"
EMBEDDING_MODEL = "all-mpnet-base-v2"  # stronger legal semantic model
CHUNK_SIZE = 800  # number of words per chunk

os.makedirs(INDEX_DIR, exist_ok=True)

# ---------------------------
# Helper Functions
# ---------------------------
def read_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def chunk_text(text, chunk_size=CHUNK_SIZE):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# ---------------------------
# Collect All TXT Files Only
# ---------------------------
all_files = glob.glob(f"{RAW_DIR}/**/*.txt", recursive=True)
print(f"Found {len(all_files)} TXT files to process.")

# ---------------------------
# Initialize Embedding Model
# ---------------------------
embedder = SentenceTransformer(EMBEDDING_MODEL)

# ---------------------------
# Process Files & Create Chunks
# ---------------------------
all_chunks = []
metadata = []

for file_path in all_files:
    text = read_txt(file_path)
    chunks = chunk_text(text)
    all_chunks.extend(chunks)
    metadata.extend([{"source": file_path}] * len(chunks))

print(f"Created {len(all_chunks)} chunks.")

# ---------------------------
# Generate Embeddings
# ---------------------------
embeddings = embedder.encode(all_chunks, show_progress_bar=True, convert_to_numpy=True)

# ---------------------------
# Build FAISS Index
# ---------------------------
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and metadata
faiss.write_index(index, f"{INDEX_DIR}/faiss_index.bin")
with open(f"{INDEX_DIR}/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print("FAISS index and metadata saved successfully.")
