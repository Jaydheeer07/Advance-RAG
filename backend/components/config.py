# config.py
import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = st.secrets.get("QDRANT_URL", os.getenv("QDRANT_URL"))
QDRANT_API_KEY = st.secrets.get("QDRANT_API_KEY", os.getenv("QDRANT_API_KEY"))
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
DOCUMENT_STORE_INDEX = "Documents"
EMBEDDING_MODEL = "text-embedding-3-small"
GENERATION_MODEL = "gpt-4-1106-preview"
