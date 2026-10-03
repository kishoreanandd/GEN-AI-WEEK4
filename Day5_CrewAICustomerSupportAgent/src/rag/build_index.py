from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Project paths
BASE_DIR = Path(__file__).resolve().parents[2]

PDF_PATH = BASE_DIR / "src" / "data" / "customer_support.pdf"
CHROMA_PATH = BASE_DIR / "src" / "data" / "chroma_db"


def build_rag_index():

    print("Loading PDF...")

    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()

    print(f"Loaded {len(documents)} page(s).")

    # Split documents into smaller chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    # Create OpenAI embeddings
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    print("Creating embeddings and storing in ChromaDB...")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_PATH),
        collection_name="technova_support"
    )

    print("RAG index created successfully.")
    print(f"ChromaDB location: {CHROMA_PATH}")


if __name__ == "__main__":
    build_rag_index()