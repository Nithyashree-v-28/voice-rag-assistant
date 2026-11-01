
import pymupdf
import re


def extract_pdf_text(pdf_path):
    """Extract text from all pages of the syllabus PDF."""
    document = pymupdf.open(pdf_path)

    all_text = ""

    for page in document:
        all_text += page.get_text() + "\n"

    document.close()
    return all_text


def clean_text(raw):
    """Normalize whitespace, join wrapped lines, and fix PDF bullets."""

    lines = [
        re.sub(r"[ \t]+", " ", line).strip()
        for line in raw.splitlines()
    ]

    merged = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Look past blank lines to detect a sentence continuation
        if not line:
            j = i + 1

            while j < len(lines) and not lines[j]:
                j += 1

            if (
                merged
                and merged[-1]
                and j < len(lines)
                and lines[j][0].islower()
                and not merged[-1].endswith((".", "!", "?", ":"))
            ):
                i = j
                continue

            merged.append("")
            i += 1
            continue

        # Join lowercase continuation lines
        if merged and merged[-1] and line[0].islower():
            merged[-1] += " " + line
        else:
            merged.append(line)

        i += 1

    text = "\n".join(merged)

    # Replace the PDF-specific bullet character
    text = text.replace("\uf0b7", "•")

    # Normalize excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


def main():
    pdf_path = "data/syllabus.pdf"
    output_path = "data/extracted_text.txt"

    all_text = extract_pdf_text(pdf_path)
    cleaned_text = clean_text(all_text)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(cleaned_text)

    print("PDF text extracted and cleaned successfully!")
    print("Original characters:", len(all_text))
    print("Cleaned characters:", len(cleaned_text))
    print("Saved to:", output_path)


if __name__ == "__main__":
    main()
