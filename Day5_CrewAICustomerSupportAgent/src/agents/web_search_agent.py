from crewai import Agent
from crewai_tools import SerperDevTool


def create_web_search_agent():

    search_tool = SerperDevTool()

    agent = Agent(
        role="Web Research Customer Support Agent",

        goal=(
            "Find reliable and relevant information from the web "
            "when the internal customer support knowledge base "
            "does not contain enough information."
        ),

        backstory=(
            "You are a customer support research specialist. "
            "You search the web to find current and reliable information. "
            "You must distinguish verified information from uncertain "
            "information and must never invent facts."
        ),

        tools=[search_tool],

        verbose=True,

        allow_delegation=False
    )

    return agent