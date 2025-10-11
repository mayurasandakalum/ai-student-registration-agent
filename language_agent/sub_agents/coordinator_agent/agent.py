# 📁 language_agent/sub_agents/coordinator_agent/agent.py (Corrected)

from google.adk.agents import LlmAgent

# Import the prompt from the local directory
from . import prompt
from .sub_agents.course_selection_agent.agent import course_selection_agent
from .sub_agents.student_registration_agent.agent import student_registration_agent


coordinator_agent = LlmAgent(
    name="coordinator_agent",
    description="An agent that coordinates multiple specialized agents to accomplish complex tasks.",
    model="gemini-2.5-flash",
    # Add the missing instruction prompt
    instruction=prompt.COORDINATOR_PROMPT,
    sub_agents=[
        course_selection_agent,
        student_registration_agent,
    ],
)

root_agent = coordinator_agent
