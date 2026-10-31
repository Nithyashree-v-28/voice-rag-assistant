import faiss
from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS database
index = faiss.read_index("data/syllabus.index")

# Read original chunks
with open("data/extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunk_size = 500
overlap = 50

chunks = []
start = 0

while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    start += chunk_size - overlap

# Ask a sample question
question = "What are the topics covered in this syllabus?"

# Convert question into an embedding
question_embedding = model.encode([question])

# Search for the 3 most relevant chunks
distances, indices = index.search(question_embedding, 3)

print("Question:", question)

for i, idx in enumerate(indices[0]):
    print(f"\nResult {i + 1}")
    print("Distance:", distances[0][i])
    print("Content:", chunks[idx])