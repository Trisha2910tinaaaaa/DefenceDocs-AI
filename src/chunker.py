def chunk_documents(
    documents,
    chunk_size=800,
    overlap=100
):

    chunks = []

    for document in documents:

        for page in document["pages"]:

            text = page["text"]

            start = 0
            chunk_number = 0

            while start < len(text):

                end = start + chunk_size

                chunk_text = text[start:end].strip()

                if chunk_text:

                    chunks.append({
                        "chunk_id": (
                            f"{document['document_id']}"
                            f"-p{page['page_number']}"
                            f"-c{chunk_number}"
                        ),
                        "document_id": document["document_id"],
                        "file_name": document["file_name"],
                        "page_number": page["page_number"],
                        "extraction_method": page[
                            "extraction_method"
                        ],
                        "text": chunk_text
                    })

                start += chunk_size - overlap
                chunk_number += 1

    return chunks