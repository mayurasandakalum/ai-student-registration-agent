from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from .sub_agents.coordinator_agent.agent import coordinator_agent
from . import prompt

# The language agent is the main entry point and has the coordinator as its sub-agent
language_agent = LlmAgent(
    name="language_agent",
    description="An agent that translates user input and coordinates with other agents.",
    model="gemini-2.5-pro",
    instruction=prompt.LANGUAGE_PROMPT,
    tools=[
        AgentTool(coordinator_agent),
    ],
)

root_agent = language_agent
