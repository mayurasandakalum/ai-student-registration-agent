from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

# Import the prompt from the local directory
from . import prompt
from .sub_agents.course_selection_agent.agent import course_selection_agent
from .sub_agents.student_registration_agent.agent import student_registration_agent


coordinator_agent = LlmAgent(
    name="coordinator_agent",
    description="An agent that coordinates multiple specialized agents to accomplish complex tasks.",
    model="gemini-2.5-pro",
    instruction=prompt.COORDINATOR_PROMPT,
    tools=[
        AgentTool(course_selection_agent),
        AgentTool(student_registration_agent),
    ],
)

root_agent = coordinator_agent
