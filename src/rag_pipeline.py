
import os
import httpx
import faiss
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Load environment variables
load_dotenv()

# Connect to Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS database
index = faiss.read_index("data/syllabus.index")
print("Total vectors in FAISS:", index.ntotal)

# Load extracted syllabus text
with open("data/extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Create chunks using the same settings as create_vector_db.py
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_text(text)

print("Total chunks loaded:", len(chunks))


def ask_question(question):

    # Convert question into embedding
    question_embedding = model.encode([question])

    # Retrieve 3 relevant chunks
    distances, indices = index.search(question_embedding, 3)

    retrieved_text = ""

    for i, idx in enumerate(indices[0]):
        print(f"\n--- Retrieved Chunk {i + 1} ---")
        print(chunks[idx])

        retrieved_text += chunks[idx] + "\n"

    # Prepare prompt for Gemini
    prompt = f"""
    Answer the question using ONLY the syllabus context below.

    If the answer is not available in the context,
    clearly say that the syllabus does not provide this information.

    Syllabus Context:
    {retrieved_text}

    Question:
    {question}
    """

    # Generate answer
    import time

    start = time.time()
    answer = None
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            answer = response.text
            break

        except errors.APIError as e:
            print(f"Attempt {attempt + 1} failed:", e)


            if attempt < 2:
                time.sleep(5)
            
        except httpx.ReadError as e:
            print(f"Connection interrupted on attempt {attempt + 1}:", e)

            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                print("Gemini quota exceeded. Stopping retries.")
                    break
            if attempt < 2:
                time.sleep(5)

    print("Gemini response time:", round(time.time() - start, 2), "seconds")

    if answer is None:
        return "Gemini is temporarily unavailable. Please try again later."

    return answer

# Test the RAG pipeline
question = "What is the purpose of a Data Warehouse?"


answer = ask_question(question)

print("\nQuestion:", question)
print("\nAnswer:", answer)
