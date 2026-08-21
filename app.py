import streamlit as st
import requests

st.set_page_config(
    page_title="DefenceDocs AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ DefenceDocs AI")
st.caption("AI-powered knowledge assistant for defence policy and veteran welfare documents")

st.divider()

question = st.text_input(
    "Ask a question about the uploaded defence documents",
    placeholder="e.g. What is the definition of an ex-serviceman?"
)

if st.button("Search Documents"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        with st.spinner("Searching defence documents..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={"question": question},
                    timeout=120
                )

                response.raise_for_status()

                result = response.json()

                st.subheader("Answer")

                st.write(result["answer"])

                st.divider()

                st.subheader("Sources")

                for source in result.get("sources", []):

                    st.write(
                        f"📄 {source['file_name']} "
                        f"— Page {source['page_number']}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Could not connect to FastAPI. "
                    "Make sure the backend is running on port 8000."
                )

            except Exception as e:

                st.error(f"Error: {e}")