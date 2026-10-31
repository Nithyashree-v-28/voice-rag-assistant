import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Read cleaned syllabus text
with open("data/extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Create improved chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_text(text)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings for the new chunks
embeddings = model.encode(chunks)

# Convert embeddings to the format FAISS expects
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Store embeddings
index.add(embeddings)

# Save the updated database
faiss.write_index(index, "data/syllabus.index")

print("Updated FAISS database successfully!")
print("Total chunks:", len(chunks))
print("Total vectors stored:", index.ntotal)