from crewai import Crew, Process

from src.agents.rag_agent import create_rag_agent
from src.tasks.rag_task import create_rag_task


def create_support_crew():

    rag_agent = create_rag_agent()

    rag_task = create_rag_task(rag_agent)

    crew = Crew(
        agents=[rag_agent],
        tasks=[rag_task],
        process=Process.sequential,
        verbose=True
    )

    return crew