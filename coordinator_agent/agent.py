from google.adk.agents import LlmAgent

from .sub_agents.course_selection_agent import course_selection_agent
from .sub_agents.student_registration_agent import student_registration_agent

coordinator_agent = LlmAgent(
    name="Coordinator Agent",
    description="An agent that coordinates multiple specialized agents to accomplish complex tasks.",
    model="gemini-2.5-flash",
    sub_agents=[
        course_selection_agent,
        student_registration_agent,
    ],
)

root_agent = coordinator_agent
