"""
"""

import uvicorn

from src.api import fastapi_app


app = fastapi_app


if __name__ == "__main__":
    uvicorn.run("main:app")
