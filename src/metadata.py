import pandas as pd


def build_metadata(documents):

    records = []

    for document in documents:

        total_characters = sum(
            len(page["text"])
            for page in document["pages"]
        )

        ocr_pages = sum(
            page["extraction_method"] == "ocr"
            for page in document["pages"]
        )

        records.append({
            "document_id": document["document_id"],
            "file_name": document["file_name"],
            "page_count": document["page_count"],
            "character_count": total_characters,
            "ocr_pages": ocr_pages
        })

    return pd.DataFrame(records)