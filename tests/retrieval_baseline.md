# Baseline Retrieval Results

## Test question
What are the components of a Data Warehouse?

## Results

| Observation | k=3 | k=5 | k=7 |
|---|---|---|---|
| Number of chunks retrieved | 3 | 5 | 7 |
| Relevant chunks | | | |
| Partially relevant chunks | | | |
| Irrelevant chunks | | | |
| Expected components list retrieved? | | | |
| Notes | | | |

## Detailed observations

### k=3
Pending

### k=5
Pending

### k=7
Pending

# Updated Index Results
Question: What is the purpose of metadata in a data warehouse?

Top 5 results:
- Highly relevant: 5
- Partially relevant: 0
- Irrelevant: 0

Observation:
The updated index retrieves the definition, purpose, technical
metadata, business metadata, and metadata repository information.
The results provide sufficient context to construct a grounded answer.

Question: What are the differences between star schema and snowflake schema?

Top 5 results:
- Highly relevant: 3
- Relevant: 2
- Irrelevant: 0

Observation:
The index retrieves both schema definitions, but the information
is fragmented. The snowflake schema appears at rank 1, while
star schema characteristics appear in separate chunks.
A comparison answer requires combining multiple chunks.

RAG Answer Evaluation:
Question: What are the differences between star schema and snowflake schema?

Result: Successful

Strengths:
- Correctly compares normalization and redundancy.
- Explains structure and complexity.
- Combines information from multiple retrieved chunks.
- Produces a structured comparison.

Issues:
- Performance claims need careful qualification.
- Some awkward source wording is repeated.

Conclusion:
The RAG pipeline successfully combines fragmented retrieved
information into a coherent comparison. Minor source-quality
and answer-grounding improvements are still needed.

## Conclusion
Pending