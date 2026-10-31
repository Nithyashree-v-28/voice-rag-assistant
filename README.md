# Voice-Enabled RAG Assistant

## Overview

An AI-powered assistant that answers questions
using information retrieved from PDF documents.

## Planned Features

- PDF document loading
- Text chunking
- Embedding generation
- Vector similarity search
- Retrieval-Augmented Generation using Gemini
- FastAPI integration
- Speech-to-text input
- Text-to-speech output

## Technology Stack

- Python
- LangChain
- FAISS
- Gemini API
- FastAPI
- Git

### Retrieval Experiment

| Number of chunks (k) | Observation |
|---|---|
| 2 | Retrieved partially relevant information for the components question |
| 3 | Retrieved the exact architecture and core components sections |

Conclusion: Retrieving 3 chunks improved context coverage for this question.