import faiss
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load syllabus text
with open("data/extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Create chunks using the same settings
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_text(text)

# Load embedding model and FAISS index
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("data/syllabus.index")

def search_syllabus(question):

    question_embedding = model.encode([question])

    distances, indices = index.search(question_embedding, 3)

    print("\nQuestion:", question)

    for i, idx in enumerate(indices[0]):
        print(f"\n--- Result {i + 1} ---")
        print("Distance:", distances[0][i])
        print(chunks[idx])


# Test one question
search_syllabus("What are the components of a Data Warehouse")