# Import libraries
import os
from dotenv import dotenv_values
from supabase import create_client, Client


# Primero intenta obtener las variables de entorno del sistema (usado en producción)
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Si las variables no están definidas, intenta cargarlas desde el archivo .env (desarrollo)
if not url or not key:
    config = dotenv_values(".env")
    url = config.get("SUPABASE_URL")
    key = config.get("SUPABASE_KEY")

# Verifica si las variables se obtuvieron correctamente
if not url or not key:
    raise ValueError("SUPABASE_URL o SUPABASE_KEY no están definidas.")

supabase: Client = create_client(url, key)

# Create CRUD operations for Supabase service
# Create a function to get all data from a table
def get_all_data(table: str):
    return supabase.table(table).select('*').execute()

# Create a function to insert data into a table
def insert_data(table: str, data: dict):
    return supabase.table(table).insert(data).execute()

# Create a function to delete data from a table
def delete_data(table: str, id: str):
    return supabase.table(table).delete().eq('id', id).execute()

# Create a function to delete all data from a table

def delete_all_data(table: str):
    return supabase.table(table).delete().execute()