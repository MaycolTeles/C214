"""
"""

from typing import Optional, Union
import sqlite3


_DB_FULL_NAME = "app/movie/movies.db"


def run_query(query: str, values: Optional[tuple[Union[str, int], ...]]=None):
    """
    """
    if values is None:
        values = ()

    connection = sqlite3.connect(_DB_FULL_NAME)
    cursor = connection.cursor()    

    cursor.execute(query, values)

    response = cursor.fetchall()

    connection.commit()
    connection.close()

    return response


def create_database() -> None:
    """
    """
    query = '''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            production_company TEXT,
            category TEXT, 
            year INTEGER,
            score INTEGER
        )
    '''

    run_query(query)
