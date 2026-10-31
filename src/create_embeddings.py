from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read the extracted text
with open("data/extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split text into chunks
chunk_size = 500
overlap = 50

chunks = []
start = 0

while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    start += chunk_size - overlap

# Generate embeddings
embeddings = model.encode(chunks)

print("Total chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)
print("First embedding:", embeddings[0][:5])