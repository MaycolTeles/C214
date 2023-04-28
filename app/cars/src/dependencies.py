"""
"""

import os

from src.repositories import Repository, InMemoRepository, SQLiteRepository


def get_repository() -> Repository:
    """
    """
    is_test_env = os.getenv("IS_TEST_ENV")

    if is_test_env:
        return InMemoRepository()

    return SQLiteRepository()


REPOSITORY_INJECTION = get_repository()
