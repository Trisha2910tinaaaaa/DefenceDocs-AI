import os
from google import genai


client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)


def generate_answer(query, context):

    context_text = "\n\n".join(
        [
            f"""
SOURCE: {item['file_name']}
PAGE: {item['page_number']}

{item['text']}
"""
            for item in context
        ]
    )

    prompt = f"""
You are a document question-answering assistant.

Answer the user's question ONLY using the provided
document context.

If the answer is not present in the context,
say that the information was not found in the
provided documents.

Do not invent facts.

USER QUESTION:
{query}

DOCUMENT CONTEXT:
{context_text}

Provide a concise answer and mention the
relevant document and page numbers.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text