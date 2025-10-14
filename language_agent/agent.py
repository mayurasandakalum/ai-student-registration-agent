from google.adk.agents import LlmAgent
from .sub_agents.coordinator_agent.agent import coordinator_agent
from . import prompt

# The language agent is the main entry point and has the coordinator as its sub-agent
language_agent = LlmAgent(
    name="language_agent",
    description="An agent that translates user input and coordinates with other agents.",
    model="gemini-2.5-flash",
    instruction=prompt.LANGUAGE_PROMPT,
    sub_agents=[coordinator_agent],
)

root_agent = language_agent
