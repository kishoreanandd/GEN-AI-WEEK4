from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


# Load .env
BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")


# Check API key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY was not found.")


# ChromaDB path
CHROMA_PATH = BASE_DIR / "src" / "data" / "chroma_db"

print("Chroma path:")
print(CHROMA_PATH)


# Create embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# Connect to existing ChromaDB
vectorstore = Chroma(
    collection_name="technova_support",
    persist_directory=str(CHROMA_PATH),
    embedding_function=embeddings,
)


# Check document count
collection = vectorstore._collection

print("\nNumber of documents:")
print(collection.count())


# Test similarity search
print("\nTesting search...")

results = vectorstore.similarity_search(
    "What is the return policy?",
    k=4
)

print(f"Results found: {len(results)}")


for i, result in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(result.page_content)