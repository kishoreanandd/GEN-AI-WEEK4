from crewai import Task


def create_rag_task(agent):

    task = Task(
        description=(
            "Answer this customer question using the internal "
            "TechNova customer support knowledge base:\n\n"

            "{customer_query}\n\n"

            "You MUST use the Customer Support Knowledge Base tool "
            "before answering.\n\n"

            "Determine whether the retrieved information is sufficient "
            "to answer the customer's question accurately.\n\n"

            "If the knowledge base contains enough information, provide "
            "a concise customer-friendly answer.\n\n"

            "If the knowledge base does not contain enough information, "
            "do not guess. State that the knowledge base does not contain "
            "enough information.\n\n"

            "At the end of your response, provide exactly one of these "
            "values on a separate line:\n\n"

            "RELEVANCE: RELEVANT\n"
            "or\n"
            "RELEVANCE: NOT_RELEVANT"
        ),

        expected_output=(
            "A customer support answer followed by a relevance indicator. "
            "The final line must contain either "
            "'RELEVANCE: RELEVANT' or "
            "'RELEVANCE: NOT_RELEVANT'."
        ),

        agent=agent
    )

    return task