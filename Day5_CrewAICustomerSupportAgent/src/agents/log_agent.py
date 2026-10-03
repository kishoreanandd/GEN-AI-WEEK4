from crewai import Agent

from src.tools.log_tool import CustomerActivityLogTool


def create_log_agent():

    log_tool = CustomerActivityLogTool()

    agent = Agent(
        role="Customer Activity Logging Agent",

        goal=(
            "Accurately record every customer support interaction "
            "in the local activity log."
        ),

        backstory=(
            "You are responsible for maintaining the customer "
            "support activity log. You record the customer's question, "
            "the route used to answer it, and the final answer. "
            "You must use the Customer Activity Logger tool and "
            "must not invent or modify the information being logged."
        ),

        tools=[log_tool],

        verbose=True,

        allow_delegation=False
    )

    return agent