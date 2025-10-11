from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

from . import prompt
from .tools import create_student_record

MODEL = "gemini-2.5-flash-lite"

student_registration_agent = LlmAgent(
    name="student_registration_agent",
    description="An agent that helps students register for classes.",
    model=MODEL,
    instruction=prompt.STUDENT_REGISTRATION_PROMPT,
    tools=[FunctionTool(create_student_record)],
)

root_agent = student_registration_agent
