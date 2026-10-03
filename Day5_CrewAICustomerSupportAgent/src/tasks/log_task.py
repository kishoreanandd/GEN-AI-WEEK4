from crewai import Task


def create_log_task(agent):

    task = Task(

        description=(
            "Log the following customer support interaction.\n\n"

            "CUSTOMER QUESTION:\n"
            "{customer_query}\n\n"

            "ROUTE USED:\n"
            "{route}\n\n"

            "FINAL ANSWER:\n"
            "{final_answer}\n\n"

            "Use the Customer Activity Logger tool to save "
            "this interaction to the local activity log.\n\n"

            "Do not change the customer question, route, "
            "or final answer."
        ),

        expected_output=(
            "A confirmation that the customer interaction "
            "was successfully logged."
        ),

        agent=agent
    )

    return task