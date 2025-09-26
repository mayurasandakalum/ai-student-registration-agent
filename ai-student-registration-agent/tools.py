from supabase import create_client, Client
import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)


def create_student_record(student_name: str, mobile_number: Optional[str]) -> dict:
    """
    Creates a new record in the tbl_students table.

    Args:
        student_name (str): The name of the student (required).
        mobile_number (str, optional): The mobile number of the student.

    Returns:
        dict: The inserted record data or an error message.
    """
    try:
        data = {"student_name": student_name}
        if mobile_number is not None:
            data["mobile_number"] = mobile_number

        response = supabase_client.table("tbl_students").insert(data).execute()
        return response.data[0] if response.data else {"error": "Insertion failed"}
    except Exception as e:
        return {"error": str(e)}
