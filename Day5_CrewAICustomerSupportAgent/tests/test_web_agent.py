from src.agents.web_search_agent import create_web_search_agent
from src.tasks.web_search_task import create_web_search_task

from crewai import Crew, Process


def main():

    agent = create_web_search_agent()

    task = create_web_search_task(agent)

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    query = input("\nCustomer question: ")

    result = crew.kickoff(
        inputs={
            "customer_query": query
        }
    )

    print("\n" + "=" * 60)
    print("WEB SEARCH ANSWER")
    print("=" * 60)

    print(result)


if __name__ == "__main__":
    main()
    