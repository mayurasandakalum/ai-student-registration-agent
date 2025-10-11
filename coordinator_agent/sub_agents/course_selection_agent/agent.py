from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

from . import prompt
from .tools import (
    get_course_details,
    search_courses,
    get_courses_by_stream,
    get_available_streams_and_subjects,
    get_available_courses,
)

MODEL = "gemini-2.5-flash"

agent = LlmAgent(
    name="course_selection_agent",
    description="An agent that helps students select courses based on their preferences.",
    model=MODEL,
    instruction=prompt.COURSE_SELECTION_PROMPT,
    tools=[
        FunctionTool(get_available_courses),
        FunctionTool(get_course_details),
        FunctionTool(search_courses),
        FunctionTool(get_courses_by_stream),
        FunctionTool(get_available_streams_and_subjects),
    ],
)

root_agent = agent
