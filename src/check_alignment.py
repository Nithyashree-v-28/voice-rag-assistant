import numpy as np
from src.rag_pipeline import model, index, chunks

print("vectors:", index.ntotal, "| chunks:", len(chunks))
print("embedding norm:", np.linalg.norm(model.encode(["test"])[0]))

for i in [0, len(chunks) // 2, len(chunks) - 1]:
    _, idx = index.search(model.encode([chunks[i]]), 1)
    print(i, "->", idx[0][0], "OK" if idx[0][0] == i else "MISMATCH")