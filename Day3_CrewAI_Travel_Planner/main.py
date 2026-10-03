import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

load_dotenv()

# Get city from user
city = input("Enter a city: ")

# Create Travel Planner Agent
travel_planner = Agent(
    role="Travel Planner",
    
    goal="Suggest 3 useful and interesting places to visit in the given city.",
    
    backstory=(
        "You are an experienced travel planner who helps first-time visitors "
        "discover useful, interesting, and popular places in a city. "
        "You give practical recommendations in a simple and easy-to-read format. "
        "You avoid long explanations and focus only on the most useful information."
    ),
    
    verbose=True
)

# Create Task
travel_task = Task(
    description=(
        f"Create a short travel recommendation for {city}. "
        "Suggest exactly 3 places to visit. "
        "For each place, provide the place name and one short reason "
        "why a visitor should visit it."
    ),
    
    expected_output=(
        "Exactly 3 recommendations. "
        "For each recommendation include: "
        "1. Place name "
        "2. One short reason to visit. "
        "Do not write an introduction, conclusion, or long essay."
    ),
    
    agent=travel_planner
)

# Create Crew
crew = Crew(
    agents=[travel_planner],
    tasks=[travel_task],
    process=Process.sequential,
    verbose=True
)

# Run Crew
result = crew.kickoff()

# Print result
print("\n===== TRAVEL RECOMMENDATIONS =====")
print(result)