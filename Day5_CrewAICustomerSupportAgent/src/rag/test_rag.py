from rag_engine import search_rag


query = "How long do customers have to return a product?"

results = search_rag(query)


print("\n===== RAG RESULTS =====\n")

for i, document in enumerate(results, start=1):
    print(f"--- Result {i} ---")
    print(document.page_content)
    print()