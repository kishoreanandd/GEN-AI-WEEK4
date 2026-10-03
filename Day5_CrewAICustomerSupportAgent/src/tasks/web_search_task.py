from crewai import Task


def create_web_search_task(agent):

    task = Task(
        description=(
            "The internal customer support knowledge base did not "
            "provide a reliable answer to this customer question:\n\n"

            "{customer_query}\n\n"

            "Search the web for relevant and reliable information. "
            "Use the search tool. "
            "Prefer official or authoritative sources when possible. "
            "Do not invent information."
        ),

        expected_output=(
            "A clear customer support answer based on relevant "
            "web search results. Mention uncertainty when reliable "
            "information cannot be found."
        ),

        agent=agent
    )

    return task