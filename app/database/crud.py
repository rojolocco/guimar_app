# Import libraries
from dotenv import dotenv_values
from supabase import create_client, Client


config = dotenv_values(".env")

# Create Supabase client
url: str = config.get("SUPABASE_URL")
key: str = config.get("SUPABASE_KEY")
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