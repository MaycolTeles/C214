"""
"""

from src.repositories.repository import Repository
from src.repositories.in_memo import InMemoRepository
from src.repositories.sqlite import SQLiteRepository, create_database


def _get_sqlite_repository() -> SQLiteRepository:
    """
    """
    create_database()
    return SQLiteRepository()


def _get_in_memo_repository() -> InMemoRepository:
    """
    """
    return InMemoRepository()


def get_repository() -> Repository:
    """
    """
    repository = _get_sqlite_repository()
    return repository


REPOSITORY_INJECTION = get_repository()
