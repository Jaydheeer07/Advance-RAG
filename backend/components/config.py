import streamlit as st

QDRANT_URL = st.secrets.get("QDRANT_URL")
QDRANT_API_KEY = st.secrets.get("QDRANT_API_KEY")
DOCUMENT_STORE_INDEX = "Documents"
EMBEDDING_MODEL = "text-embedding-3-small"
GENERATION_MODEL = "gpt-4-1106-preview"
