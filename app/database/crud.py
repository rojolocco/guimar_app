# app/database/crud.py
import os
from dotenv import dotenv_values
from supabase import create_client, Client
from typing import Any, Dict, List


# Attempt to fetch environment variables from the system (used in production)
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")


# If the environment variables are not set, try loading them from the .env file (used in development)
if not url or not key:
    config = dotenv_values(".env")
    url = config.get("SUPABASE_URL")
    key = config.get("SUPABASE_KEY")


# Check if the variables were successfully retrieved
if not url or not key:
    raise ValueError("SUPABASE_URL or SUPABASE_KEY are not defined.")


# Initialize the Supabase client
supabase: Client = create_client(url, key)


# CRUD Operations for Supabase

def get_all_data(table: str) -> List[Dict[str, Any]]:
    """
    Fetches all rows from the specified table.

    Args:
        table (str): The name of the table to fetch data from.

    Returns:
        List[Dict[str, Any]]: A list of rows from the table.
    """
    response = supabase.table(table).select('*').execute()
    return response


def insert_data(table: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Inserts a new row into the specified table.

    Args:
        table (str): The name of the table to insert data into.
        data (Dict[str, Any]): The data to insert as a row.

    Returns:
        Dict[str, Any]: The inserted row's data.
    """
    response = supabase.table(table).insert(data).execute()
    return response


def delete_data(table: str, row_id: str) -> Dict[str, Any]:
    """
    Deletes a row by ID from the specified table.

    Args:
        table (str): The name of the table to delete data from.
        row_id (str): The ID of the row to delete.

    Returns:
        Dict[str, Any]: A dictionary confirming the deletion.
    """
    response = supabase.table(table).delete().eq('id', row_id).execute()
    return response
