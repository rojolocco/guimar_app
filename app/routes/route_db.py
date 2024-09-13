# app/routes/route_db.py
from fastapi import APIRouter, HTTPException
from ..database.crud import get_all_data, insert_data
from ..database.crud import delete_data


router_db = APIRouter()


@router_db.get("/{table_name}")
async def fetch_data(table_name: str):
    """
    Fetches all data from the specified table.

    Args:
        table_name (str): The name of the table to fetch data from.

    Returns:
        list: A list of rows from the table.
    """
    try:
        res = get_all_data(table_name)
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router_db.post("/{table_name}")
async def new_data(table_name: str, data: dict):
    """
    Inserts new data into the specified table.

    Args:
        table_name (str): The name of the table to insert data into.
        data (dict): The data to insert.

    Returns:
        dict: A dictionary confirming the insertion status.
    """
    try:
        res = insert_data(table_name, data)
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router_db.delete("/{table_name}/{id}")
async def remove_data_id(table_name: str, id: int):
    """
    Deletes a specific item from the table by ID.

    Args:
        table_name (str): The name of the table to delete data from.
        id (int): The ID of the item to delete.

    Returns:
        dict: A dictionary confirming the deletion status.
    """
    try:
        res = delete_data(table_name, id)
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
