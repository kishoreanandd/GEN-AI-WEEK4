from crewai import Agent

from src.tools.rag_tool import CustomerSupportRAGTool


def create_rag_agent():

    rag_tool = CustomerSupportRAGTool()

    agent = Agent(
        role="Customer Support Knowledge Agent",

        goal=(
            "Answer customer questions accurately using the "
            "TechNova customer support knowledge base."
        ),

        backstory=(
            "You are a customer support specialist for TechNova. "
            "You use the company's internal knowledge base to answer "
            "customer questions. You must not invent information. "
            "If the knowledge base does not contain enough information "
            "to answer the question, clearly say that the information "
            "is not available."
        ),

        tools=[rag_tool],

        verbose=True,

        allow_delegation=False
    )

    return agent