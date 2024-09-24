# Advance RAG

This project implements a Retrieval-Augmented Generation (RAG) system using Haystack, Qdrant, and OpenAI. It provides a Streamlit interface for document ingestion and question-answering.

## Prerequisites

- Python 3.8+
- Docker and Docker Compose

## Installation

1. Clone the repository:

2. Create a virtual environment and activate it: <venv\Scripts\activate>
3. Install the required packages: <pip install -r requirements.txt>
4. Set up environment variables:
Create a `.env` file in the project root and add the following:


## Running the Project

1. Start the Qdrant service using Docker Compose: <docker-compose up -d>
2. Run the Streamlit app: <streamlit run app.py>
3. Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

## Usage

1. Enter your OpenAI API key in the sidebar.
2. Upload a PDF document using the file uploader in the sidebar.
3. Once the document is processed, you can ask questions about its content in the chat interface.

## Project Structure

- `app.py`: Main Streamlit application
- `backend/`: Contains the core components of the RAG system
- `components/`: 
 - `config.py`: Configuration settings
 - `document_store.py`: Qdrant document store initialization
 - `ingestion.py`: Document ingestion pipeline
 - `retrieval.py`: Question-answering pipeline

## Notes

- The project uses OpenAI's API for embeddings and text generation. Make sure you have a valid API key.
- Each time a new document is uploaded, the existing Qdrant collection is deleted and a new one is created.


