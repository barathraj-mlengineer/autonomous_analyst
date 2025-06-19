import os
from supabase import create_client, Client
import pandas as pd

# Initialize Supabase client
supabase_url = "https://hgffusbghrfrguigttru.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhnZmZ1c2JnaHJmcmd1aWd0dHJ1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk2NTExMjksImV4cCI6MjA2NTIyNzEyOX0.Cpwk5m0-ccLT11OeFUiF6XkrCWMc96TtWda4kh_Ow4s"
supabase: Client = create_client(supabase_url, supabase_key)

def fetch_supabase_data(student, filters=None):
    """
    Fetch data from a Supabase table.
    
    Args:
        table_name (str): The table to query.
        filters (dict): Optional filter dictionary. Example: {"column": "value"}

    Returns:
        pd.DataFrame: Fetched data as a DataFrame.
    """
    query = supabase.table(student).select("*")

    # Apply filters if provided
    if filters:
        for key, value in filters.items():
            query = query.eq(key, value)

    response = query.execute()

    # Convert response to DataFrame
    data = response.data
    return pd.DataFrame(data)
