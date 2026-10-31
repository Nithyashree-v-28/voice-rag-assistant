from langchain_text_splitters import RecursiveCharacterTextSplitter

# Read cleaned syllabus text
with open("data/extracted_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split text into more meaningful chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_text(text)

print("Total chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0])