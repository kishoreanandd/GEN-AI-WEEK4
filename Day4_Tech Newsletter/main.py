import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

load_dotenv()


# -----------------------------
# Tool
# -----------------------------

search_tool = SerperDevTool()


# -----------------------------
# Agent 1: Researcher
# -----------------------------

researcher = Agent(
    role="Tech News Researcher",

    goal=(
        "Find today's 3 most important technology news stories "
        "using reliable web sources."
    ),

    backstory=(
        "You are a technology news researcher who follows the latest "
        "developments in AI, software, gadgets, cybersecurity, startups, "
        "and major technology companies. You research carefully and give "
        "clean, factual information to a newsletter writer. "
        "You do not write a newsletter. You only provide research."
    ),

    tools=[search_tool],

    verbose=True
)


# -----------------------------
# Agent 2: Writer
# -----------------------------

writer = Agent(
    role="Tech Newsletter Writer",

    goal=(
        "Turn the research provided by the researcher into a clear, "
        "interesting 5-line technology newsletter."
    ),

    backstory=(
        "You are a concise technology newsletter writer. "
        "You write for busy readers who want to understand the most "
        "important technology news quickly. You do not perform web searches "
        "and you only use the research given to you."
    ),

    verbose=True
)


# -----------------------------
# Task 1: Research
# -----------------------------

research_task = Task(
    description=(
        "Search the web for today's top 3 technology news stories. "
        "Focus on important and recent developments. "
        "For each story, provide the headline, a short summary, "
        "and the source name."
    ),

    expected_output=(
        "Exactly 3 technology news stories. "
        "For each story provide:\n"
        "1. Headline\n"
        "2. 1-2 sentence summary\n"
        "3. Source name\n"
        "Keep the information factual and concise."
    ),

    agent=researcher
)


# -----------------------------
# Task 2: Newsletter
# -----------------------------

writer_task = Task(
    description=(
        "Using ONLY the research provided by the Researcher, "
        "write a technology newsletter with exactly 5 bullet-point lines. "
        "Cover all 3 news stories. "
        "Keep each line short, clear, and useful for a busy reader. "
        "Do not perform your own web search."
    ),

    expected_output=(
        "Exactly 5 bullet points. "
        "Each bullet must be one short sentence. "
        "Cover all 3 researched technology news stories. "
        "Do not add an introduction or conclusion. "
        "Do not include information that is not present in the research."
    ),

    agent=writer,

    context=[research_task]
)


# -----------------------------
# Crew
# -----------------------------

crew = Crew(
    agents=[researcher, writer],

    tasks=[research_task, writer_task],

    process=Process.sequential,

    verbose=True
)


# -----------------------------
# Run Crew
# -----------------------------

result = crew.kickoff()


# -----------------------------
# Print final newsletter
# -----------------------------

print("\n")
print("=" * 50)
print("TECH NEWSLETTER")
print("=" * 50)

print(result)