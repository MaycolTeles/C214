"""
"""

import uvicorn
from fastapi import FastAPI

from src.api import fastapi_app


def main() -> FastAPI:
    """
    Main function.
    """
    app = fastapi_app

    return app


if __name__ == "__main__":
    uvicorn.run(app=main)
