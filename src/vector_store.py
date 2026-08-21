import faiss
import numpy as np


def create_index(embeddings):

    embeddings = np.asarray(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index
def search(
    index,
    model,
    chunks,
    query,
    top_k=5
):

    query_embedding = model.encode(
        [query]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for distance, idx in zip(
        distances[0],
        indices[0]
    ):

        result = chunks[idx].copy()

        result["distance"] = float(distance)

        results.append(result)

    return results