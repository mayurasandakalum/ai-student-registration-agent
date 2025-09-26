from google.adk.agents import LlmAgent

from . import prompt

MODEL = "gemini-2.5-pro"

agent = LlmAgent(
    name="student_registration_agent",
    description="An agent that helps students register for classes.",
    model=MODEL,
    instruction=prompt.STUDENT_REGISTRATION_PROMPT,
)

root_agent = agent
