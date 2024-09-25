# retrieval.py
from haystack import Pipeline
from haystack.components.builders import PromptBuilder
from haystack.components.embedders import OpenAITextEmbedder
from haystack.components.generators import OpenAIGenerator
from haystack_integrations.components.retrievers.qdrant import QdrantEmbeddingRetriever

from .config import EMBEDDING_MODEL, GENERATION_MODEL


def create_retrieval_pipeline(document_store, openai_api_key):
    prompt_template = """
    Given these documents, answer the question.
    Documents:
    {% for doc in documents %}
        {{ doc.content }}
    {% endfor %}

    Question: {{query}} 
    Answer:
    """

    prompt = PromptBuilder(prompt_template)
    retriever = QdrantEmbeddingRetriever(document_store=document_store)
    embedder = OpenAITextEmbedder(
        api_key=openai_api_key,
        model=EMBEDDING_MODEL,
    )
    generator = OpenAIGenerator(
        api_key=openai_api_key,
        model=GENERATION_MODEL,
        generation_kwargs={"max_tokens": 300, "temperature": 0},
    )

    pipeline = Pipeline()
    pipeline.add_component("retriever", retriever)
    pipeline.add_component("embedder", embedder)
    pipeline.add_component("generator", generator)
    pipeline.add_component("prompt", prompt)

    pipeline.connect("embedder.embedding", "retriever.query_embedding")
    pipeline.connect("retriever.documents", "prompt.documents")
    pipeline.connect("prompt", "generator")

    return pipeline


def query_documents(pipeline, question):
    result = pipeline.run(
        {
            "embedder": {"text": question},
            "retriever": {"top_k": 1},
            "prompt": {"query": question},
        }
    )
    return result["generator"]["replies"][0]
