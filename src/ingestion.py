from pathlib import Path

from .pdf_extractor import extract_text_from_pdf
from .cleaner import clean_text


def ingest_documents(raw_directory):

    raw_directory = Path(raw_directory)

    documents = []

    for pdf_path in sorted(raw_directory.glob("*.pdf")):

        print(f"Processing: {pdf_path.name}")

        pages = extract_text_from_pdf(pdf_path)

        for page in pages:
            page["text"] = clean_text(page["text"])

        documents.append({
            "document_id": pdf_path.stem,
            "file_name": pdf_path.name,
            "page_count": len(pages),
            "pages": pages
        })

    return documents