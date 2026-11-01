
import json
import faiss
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Load evaluation questions
with open("tests/eval_questions.json", "r", encoding="utf-8") as file:
    evaluation_questions = json.load(file)


# Load cleaned syllabus text
with open("data/extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()


# Recreate chunks using the same settings
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_text(text)


# Load embedding model and FAISS index
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("data/syllabus.index")


# Evaluate retrieval for every question
def evaluate_retrieval(top_k=7):

    for item in evaluation_questions:

        question = item["question"]
        question_embedding = model.encode([question])

        distances, indices = index.search(question_embedding, top_k)

        print("\n" + "=" * 70)
        print("Question ID:", item["id"])
        print("Type:", item["type"])
        print("Question:", question)

        for rank, idx in enumerate(indices[0]):

            if idx == -1:
                continue

            print(f"\n--- Result {rank + 1} ---")
            print("Distance:", distances[0][rank])
            print(chunks[idx])


if __name__ == "__main__":
    evaluate_retrieval()
