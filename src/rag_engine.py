import json

from sentence_transformers import SentenceTransformer

from .vector_store import create_index


with open(
    "data/processed/chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

embeddings = model.encode(
    [chunk["text"] for chunk in chunks],
    show_progress_bar=True
)

index = create_index(embeddings)