from supabase import create_client, Client
import os
from dotenv import load_dotenv
from typing import Optional, List, Dict, Any

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


# Helper function to create a fresh client for each request
def _create_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def get_available_courses(
    subject: Optional[str] = None,
    stream: Optional[str] = None,
    level: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Retrieves available courses based on filters.

    Args:
        subject (str, optional): The subject to filter by (e.g., 'Physics', 'Combined Mathematics').
        stream (str, optional): The stream to filter by (e.g., 'Physical Science', 'Biological Science').
        level (str, optional): The level to filter by (e.g., 'Year 12', 'Year 13', 'Revision').

    Returns:
        list: A list of available courses with their details or an error message.
    """
    try:
        supabase_client = _create_supabase_client()
        params = {}
        if subject is not None:
            params["p_subject"] = subject
        if stream is not None:
            params["p_stream"] = stream
        if level is not None:
            params["p_level"] = level

        response = supabase_client.rpc("f_get_available_courses", params).execute()
        return response.data if response.data else []
    except Exception as e:
        return [{"error": str(e)}]


def get_course_details(
    course_id: Optional[int] = None, course_code: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieves detailed information about a specific course.

    Args:
        course_id (int, optional): The ID of the course.
        course_code (str, optional): The course code (e.g., 'PHY-Y12-SAT-PM').

    Returns:
        dict: Detailed course information or an error message.
    """
    try:
        supabase_client = _create_supabase_client()
        params = {}
        if course_id is not None:
            params["p_course_id"] = course_id
        if course_code is not None:
            params["p_course_code"] = course_code

        response = supabase_client.rpc("f_get_course_details", params).execute()
        return response.data[0] if response.data else {"error": "Course not found"}
    except Exception as e:
        return {"error": str(e)}


def search_courses(keyword: str) -> List[Dict[str, Any]]:
    """
    Searches for courses by keyword in course name, subject, instructor, or course code.

    Args:
        keyword (str): The search keyword.

    Returns:
        list: A list of matching courses or an error message.
    """
    try:
        supabase_client = _create_supabase_client()
        response = supabase_client.rpc(
            "f_search_courses", {"p_keyword": keyword}
        ).execute()
        return response.data if response.data else []
    except Exception as e:
        return [{"error": str(e)}]


def get_courses_by_stream(stream: str) -> List[Dict[str, Any]]:
    """
    Retrieves all courses for a specific stream.

    Args:
        stream (str): The stream name (e.g., 'Physical Science', 'Biological Science').

    Returns:
        list: A list of courses in the specified stream or an error message.
    """
    try:
        supabase_client = _create_supabase_client()
        response = supabase_client.rpc(
            "f_get_courses_by_stream", {"p_stream": stream}
        ).execute()
        return response.data if response.data else []
    except Exception as e:
        return [{"error": str(e)}]


def get_available_streams_and_subjects() -> Dict[str, Any]:
    """
    Retrieves all available streams, subjects, and levels in the institute.

    Returns:
        dict: A dictionary containing lists of available streams, subjects, and levels or an error message.
    """
    try:
        supabase_client = _create_supabase_client()
        response = supabase_client.rpc("f_get_available_streams_and_subjects").execute()
        return response.data[0] if response.data else {"error": "No data found"}
    except Exception as e:
        return {"error": str(e)}
