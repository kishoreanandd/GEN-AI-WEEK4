from crewai import Crew, Process

from src.agents.rag_agent import create_rag_agent
from src.tasks.rag_task import create_rag_task

from src.agents.web_search_agent import create_web_search_agent
from src.tasks.web_search_task import create_web_search_task

from src.agents.log_agent import create_log_agent
from src.tasks.log_task import create_log_task


def run_support_workflow(customer_query):

    # =========================================================
    # STEP 1: RAG AGENT
    # =========================================================

    print("\n" + "=" * 60)
    print("STEP 1: RAG AGENT")
    print("=" * 60)

    rag_agent = create_rag_agent()
    rag_task = create_rag_task(rag_agent)

    rag_crew = Crew(
        agents=[rag_agent],
        tasks=[rag_task],
        process=Process.sequential,
        verbose=True
    )

    rag_result = rag_crew.kickoff(
        inputs={
            "customer_query": customer_query
        }
    )

    rag_text = str(rag_result)

    print("\nRAG RESULT:")
    print(rag_text)

    # =========================================================
    # STEP 2: CHECK RAG RELEVANCE
    # =========================================================

    if "RELEVANCE: RELEVANT" in rag_text:

        route = "rag"
        final_answer = rag_text

        print("\nRAG answer is relevant.")
        print("Web Search Agent is NOT required.")

    else:

        # =====================================================
        # STEP 3: WEB SEARCH AGENT
        # =====================================================

        route = "web_search"

        print("\nRAG answer is not relevant.")
        print("Starting Web Search Agent...")

        web_agent = create_web_search_agent()
        web_task = create_web_search_task(web_agent)

        web_crew = Crew(
            agents=[web_agent],
            tasks=[web_task],
            process=Process.sequential,
            verbose=True
        )

        web_result = web_crew.kickoff(
            inputs={
                "customer_query": customer_query
            }
        )

        final_answer = str(web_result)

    # =========================================================
    # STEP 4: LOG AGENT
    # =========================================================

    print("\n" + "=" * 60)
    print("STEP 4: LOG AGENT")
    print("=" * 60)

    log_agent = create_log_agent()
    log_task = create_log_task(log_agent)

    log_crew = Crew(
        agents=[log_agent],
        tasks=[log_task],
        process=Process.sequential,
        verbose=True
    )

    log_crew.kickoff(
        inputs={
            "customer_query": customer_query,
            "route": route,
            "final_answer": final_answer
        }
    )

    print("\nActivity successfully logged.")

    # =========================================================
    # RETURN FINAL CUSTOMER ANSWER
    # =========================================================

    return final_answer