import os
import shutil
from pathlib import Path

from crewai.tools import BaseTool
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


class CustomerSupportRAGTool(BaseTool):

    name: str = "Customer Support Knowledge Base"

    description: str = (
        "Search the TechNova customer support knowledge base. "
        "Use this tool to find information about orders, shipping, "
        "returns, refunds, warranty, payments, accounts, and other "
        "customer support topics."
    )

    def _run(self, query: str) -> str:

        base_dir = Path(__file__).resolve().parents[2]
        load_dotenv(base_dir / ".env")

        if not os.getenv("OPENAI_API_KEY"):
            return "OpenAI API key is not configured."

        chroma_path = base_dir / "src" / "data" / "chroma_db"
        pdf_path = base_dir / "src" / "data" / "customer_support.pdf"
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

        try:
            vectorstore = Chroma(
                collection_name="technova_support",
                persist_directory=str(chroma_path),
                embedding_function=embeddings,
            )
            results = vectorstore.similarity_search(query, k=4)
        except BaseException:
            if chroma_path.exists():
                shutil.rmtree(chroma_path)

            if not pdf_path.exists():
                return "Knowledge base PDF not found."

            loader = PyPDFLoader(str(pdf_path))
            documents = loader.load()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=800,
                chunk_overlap=150,
            )
            chunks = splitter.split_documents(documents)

            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=embeddings,
                persist_directory=str(chroma_path),
                collection_name="technova_support",
            )
            results = vectorstore.similarity_search(query, k=4)

        if not results:
            return (
                "No relevant information was found "
                "in the customer support knowledge base."
            )

        formatted_results = []
        for i, document in enumerate(results, start=1):
            formatted_results.append(f"Result {i}:\n{document.page_content}")

        return "\n\n".join(formatted_results)