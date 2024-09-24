# document_store.py
from haystack.utils import Secret
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from qdrant_client.http.exceptions import UnexpectedResponse

from .config import DOCUMENT_STORE_INDEX, QDRANT_API_KEY, QDRANT_URL


def initialize_document_store(recreate=False):
    try:
        return QdrantDocumentStore(
            url=QDRANT_URL,
            api_key=Secret.from_token(QDRANT_API_KEY),
            index=DOCUMENT_STORE_INDEX,
            recreate_index=recreate,
            return_embedding=True,
            wait_result_from_api=True,
            embedding_dim=1536,
            timeout=60,
        )
    except UnexpectedResponse:
        return QdrantDocumentStore(
            url=QDRANT_URL,
            api_key=Secret.from_token(QDRANT_API_KEY),
            index=DOCUMENT_STORE_INDEX,
            recreate_index=True,
            return_embedding=True,
            wait_result_from_api=True,
            embedding_dim=1536,
            timeout=60,
        )
