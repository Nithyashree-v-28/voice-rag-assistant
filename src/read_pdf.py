
import pymupdf
import re

document = pymupdf.open("data/syllabus.pdf")

all_text = ""

for page in document:
    all_text += page.get_text() + "\n"

document.close()

# Remove unnecessary extra spaces
cleaned_text = re.sub(r"[ \t]+", " ", all_text)

# Reduce multiple blank lines
cleaned_text = re.sub(r"\n{3,}", "\n\n", cleaned_text)

with open("data/extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("PDF text extracted and cleaned successfully!")
print("Original characters:", len(all_text))
print("Cleaned characters:", len(cleaned_text))
