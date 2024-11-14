# AI-Powered Chatbot with Document Retrieval and Embedding

This repository contains a tutorial for building an AI-powered chatbot that can retrieve relevant information from documents and generate contextual responses. It combines **Retrieval-Augmented Generation (RAG)** with document embedding and vector database storage to enable the chatbot to answer questions based on specific document content. The system uses ChromaDB for storing embeddings, making it possible to search for and retrieve the most relevant information efficiently.

## Table of Contents
- [AI-Powered Chatbot with Document Retrieval and Embedding](#ai-powered-chatbot-with-document-retrieval-and-embedding)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Setup](#setup)
    - [Running the Chatbot](#running-the-chatbot)
  - [Classes and Functions](#classes-and-functions)
  - [Detailed Code Explanation](#detailed-code-explanation)
    - [1. ChromaDB Initialization](#1-chromadb-initialization)
    - [2. Document Processing](#2-document-processing)
    - [3. Embedding and Storage](#3-embedding-and-storage)
    - [4. Contextual Response Generation](#4-contextual-response-generation)
  - [Troubleshooting](#troubleshooting)
  - [Contributing](#contributing)
  - [License](#license)
  - [Disclaimer](#disclaimer)

## Introduction

This project serves as an introduction to building AI-powered chatbots that use **natural language understanding** and **contextual responses** based on document data. With the help of ChromaDB, the chatbot can search through embedded documents to retrieve relevant content and generate accurate answers. The system relies on pre-trained models for text embeddings and contextual language models to produce responses based solely on the retrieved information.

## Features
- **Document Processing**: Load, split, and process documents (PDF and Excel) into manageable chunks.
- **Embedding and Storage**: Generate text embeddings and store them in ChromaDB, a vector database optimized for similarity searches.
- **Contextual Chatbot**: Generate responses based on the retrieved context, ensuring answers remain relevant to the document data.
- **Error Handling**: Includes error handling to manage cases like missing documents or connection failures.

## Requirements
- Python 3.8+
- Libraries:
  - `requests`
  - `json`
  - `pandas`
  - `os`
  - `time`
  - `langchain` (for document loading and text splitting)
  - `chromadb`
  - Additional libraries used in the tutorial: `UnstructuredPDFLoader`, `RecursiveCharacterTextSplitter`

## Installation

To set up the project, you need to install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

## Usage

### Setup

1. **Initialize the ChromaDB Client**: The `get_chroma_client()` function initializes a persistent ChromaDB client where document embeddings will be stored.
2. **Load and Process Documents**: The `RAG` class provides methods to load and process documents (e.g., Excel or PDF files) and prepare them for embedding.
3. **Start Chatting**: Once the documents are loaded and processed, the chatbot can retrieve relevant information to answer questions.

### Running the Chatbot

To run the chatbot, follow these steps:

1. **Load Documents**: Use the `load_and_process_xlsx()` or `load_and_process_pdf()` method in the `RAG` class to load your document.
2. **Add to ChromaDB**: After processing, add document chunks to ChromaDB with the `add_to_chromadb()` method.
3. **Start a Chat Session**: Use the `ChatAssistant` and `RAG` class methods to interact with the chatbot and answer user queries based on retrieved document information.

## Classes and Functions

This tutorial covers the following main classes and functions:

- **get_chroma_client()**: Initializes a persistent ChromaDB client to store embeddings.
- **chunk_list()**: Splits a list into smaller chunks, useful for batching API calls.
- **EmbeddingAPI**: Handles embedding generation for text input via an external API.
  - `encode(input_text: str)`: Sends a request to the embedding API and retrieves embeddings for the given text.
- **ChatAssistant**: Manages chat responses based on user queries and retrieved context.
  - `get_chat_response(query: str, retrieved_docs: str)`: Generates a chat response based on the query and provided document context.
- **RAG (Retrieval-Augmented Generation)**: Manages document retrieval, processing, and embedding.
  - `init_collection()`: Initializes or retrieves a collection in ChromaDB.
  - `validate_xlsx(df)`: Validates the required columns in an Excel file.
  - `load_and_process_xlsx(filepath)`: Loads and processes Excel files containing Q&A pairs.
  - `load_and_process_pdf(pdf_path)`: Loads and processes PDF files for embedding.
  - `chunk_text(content)`: Splits large texts into chunks for embedding and retrieval.
  - `get_embeddings_in_chunks(texts, chunk_size=20)`: Batches embedding generation for lists of texts.
  - `add_to_chromadb(chunks)`: Adds processed document chunks to ChromaDB.
  - `search_document(query)`: Searches ChromaDB for relevant document chunks based on a query.
  - `delete_collection()`: Deletes a collection from ChromaDB for cleanup or reset.

## Detailed Code Explanation

### 1. ChromaDB Initialization
The `get_chroma_client()` function sets up ChromaDB with a specified directory for persistent storage, ensuring embeddings are saved across sessions.

### 2. Document Processing
The `RAG` class includes methods for loading and processing Excel and PDF files. The `load_and_process_xlsx()` and `load_and_process_pdf()` methods help convert documents into chunks that can be embedded and stored in ChromaDB.

### 3. Embedding and Storage
The `EmbeddingAPI` class interacts with an external embedding API to generate embeddings, while `add_to_chromadb()` in the `RAG` class stores these embeddings in ChromaDB. The system splits text into smaller chunks to ensure embeddings can be processed effectively.

### 4. Contextual Response Generation
The `ChatAssistant` class leverages retrieved document chunks to generate context-based responses. This ensures that responses are accurate and relevant to the content in the documents.

## Troubleshooting

- **Connection Errors**: Ensure that the ChromaDB server and embedding API are running and accessible.
- **Missing Columns in Excel**: If loading an Excel file, confirm it includes the required `question` and `answer` columns.
- **PDF Loading Issues**: Ensure the PDF files are correctly formatted; some PDFs may have embedded images or other content that cannot be processed as text.

## Contributing

Contributions to this project are welcome. If you have any suggestions or would like to report an issue, please submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer

The Documentation is AI generated. It can be partially correct.
