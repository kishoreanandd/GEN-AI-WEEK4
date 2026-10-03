import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
os.environ.setdefault("PYTHONIOENCODING", "utf-8")

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

from src.support_workflow import run_support_workflow


def main():

    if len(sys.argv) > 1:
        customer_query = " ".join(sys.argv[1:])
    else:
        try:
            customer_query = input("\nCustomer question: ")
        except EOFError:
            print("\nNo customer question provided. Exiting.")
            return

    if not customer_query.strip():
        print("\nNo customer question provided. Exiting.")
        return

    final_answer = run_support_workflow(
        customer_query
    )

    print("\n" + "=" * 60)
    print("FINAL CUSTOMER ANSWER")
    print("=" * 60)

    print(final_answer)


if __name__ == "__main__":
    main()