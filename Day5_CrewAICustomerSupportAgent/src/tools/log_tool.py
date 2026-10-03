from pathlib import Path
from datetime import datetime, timezone
from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class LogActivityInput(BaseModel):
    user_query: str = Field(description="The customer's question.")
    route: str = Field(description="The route used: rag or web_search.")
    final_answer: str = Field(description="The final answer given to the customer.")


class CustomerActivityLogTool(BaseTool):

    name: str = "Customer Activity Logger"

    description: str = (
        "Log customer support activity to a local JSONL file. "
        "Use this tool to record the customer question, route used, "
        "and final answer."
    )

    args_schema: Type[BaseModel] = LogActivityInput

    def _run(
        self,
        user_query: str,
        route: str,
        final_answer: str
    ) -> str:

        base_dir = Path(__file__).resolve().parents[2]

        log_dir = base_dir / "src" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / "activity_log.jsonl"

        timestamp = datetime.now(timezone.utc).isoformat()

        log_entry = {
            "timestamp": timestamp,
            "user_query": user_query,
            "route": route,
            "final_answer": final_answer
        }

        import json

        with log_file.open("a", encoding="utf-8") as file:
            file.write(
                json.dumps(log_entry, ensure_ascii=False)
                + "\n"
            )

        return f"Activity logged successfully: {log_file}"