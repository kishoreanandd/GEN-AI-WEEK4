import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.tools.rag_tool import CustomerSupportRAGTool


def main():

    tool = CustomerSupportRAGTool()

    question = "What is the return policy?"

    result = tool._run(question)

    print("\nQUESTION:")
    print(question)

    print("\nRAG RESULT:")
    print(result)


if __name__ == "__main__":
    main()