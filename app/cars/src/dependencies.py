"""
"""

from repositories import Repository, InMemoRepository, SQLiteRepository


def get_repository() -> Repository:
    """
    """
    return InMemoRepository()


REPOSITORY_INJECTION = get_repository()
