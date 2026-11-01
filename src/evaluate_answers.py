import json
from src.rag_pipeline import ask_question

# Load evaluation questions
with open("tests/eval_questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

# Store generated answers
results = []

for item in questions:
    question = item["question"]

    print("\n" + "=" * 70)
    print("Question ID:", item["id"])
    print("Question:", question)

    answer = ask_question(question)

    print("\nGenerated Answer:")
    print(answer)

    results.append({
        "id": item["id"],
        "question": question,
        "answer": answer
    })

# Save answers
with open("tests/generated_answers.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)

print("\nEvaluation completed!")
print("Answers saved to tests/generated_answers.json")