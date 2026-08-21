from .vector_store import search


def retrieve_context(
    query,
    index,
    model,
    chunks,
    top_k=5
):

    results = search(
        index,
        model,
        chunks,
        query,
        top_k
    )

    context = []

    for result in results:

        context.append({
            "text": result["text"],
            "file_name": result["file_name"],
            "page_number": result["page_number"],
            "distance": result["distance"]
        })

    return context