t = open("data/extracted_text.txt", encoding="utf-8").read()

print(
    "paragraph breaks:", t.count("\n\n"),
    "| total lines:", t.count("\n")
)