import argparse, os, json, pathlib, re
import faiss, numpy as np
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

EMBED_MODEL = os.environ.get("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")


def read_txt(path: str) -> str:
    return pathlib.Path(path).read_text(encoding="utf-8", errors="ignore")


def read_pdf(path: str) -> str:
    reader = PdfReader(path)
    texts = []
    for page in reader.pages:
        try:
            texts.append(page.extract_text() or "")
        except Exception:
            pass
    return "\n".join(texts)


def chunk_text(text: str, chunk: int, overlap: int) -> list:
    text = re.sub(r"\s+", " ", text).strip()
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start + chunk)
        chunks.append(text[start:end])
        start = end - overlap
        if start < 0:
            start = 0
        if start >= len(text):
            break
    return [c for c in chunks if c.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--chunk", type=int, default=800)
    ap.add_argument("--overlap", type=int, default=120)
    args = ap.parse_args()

    src = pathlib.Path(args.source)
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    model = SentenceTransformer(EMBED_MODEL)
    metas = []
    embeddings = []

    for path in src.rglob("*"):
        if path.is_dir():
            continue
        if path.suffix.lower() in {".txt"}:
            text = read_txt(str(path))
        elif path.suffix.lower() in {".pdf"}:
            text = read_pdf(str(path))
        else:
            continue
        for i, ch in enumerate(chunk_text(text, args.chunk, args.overlap)):
            meta = {"source": str(path.name), "chunk_id": i, "text": ch}
            metas.append(meta)
            embeddings.append(model.encode(ch))

    if not embeddings:
        print("No documents found. Put PDFs/TXTs in data/raw/")
        return

    mat = np.array(embeddings, dtype="float32")
    index = faiss.IndexFlatIP(mat.shape[1])
    faiss.normalize_L2(mat)
    index.add(mat)

    faiss.write_index(index, str(out / "faiss.index"))
    with open(out / "meta.jsonl", "w", encoding="utf-8") as f:
        for m in metas:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    print(f"Indexed {len(metas)} chunks → {out}")


if __name__ == "__main__":
    main()
