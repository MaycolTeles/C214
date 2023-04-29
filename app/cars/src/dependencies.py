"""
"""

from src.repositories import Repository, InMemoRepository, SQLiteRepository


def _get_sqlite_repository() -> SQLiteRepository:
    """
    """
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
