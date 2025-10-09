from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

from . import prompt

MODEL = "gemini-2.5-flash-lite"

agent = LlmAgent(
    name="course_selection_agent",
    description="An agent that helps students select courses based on their preferences.",
    model=MODEL,
    instruction=prompt.COURSE_SELECTION_PROMPT,
)

root_agent = agent
