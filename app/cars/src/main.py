"""
"""

from models import Car
from dependencies import REPOSITORY_INJECTION as repository

from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.get("/")
def index():
    """"""
    return {"message": "Cars API"}


@app.get("/cars")
def get_all_cars():
    """"""
    cars = repository.read_all_cars()

    if not cars:
        return {"error": "No car found in database yet. Try adding some before retrieving any."}

    return {"cars": cars}


@app.get("/cars/{car_id}")
def get_car_by_id(car_id: int):
    """"""
    car = repository.read_car_by_id(car_id)

    if car is None:
        status_code = 404
        message = f"Car not found for id {car_id}"

        raise HTTPException(status_code=status_code, detail=message)
 
    return {"car": car}


@app.post("/cars")
def insert_car(car: Car):
    """"""
    car_id = repository.create_car(car)

    response = f"Car with id #{car_id} added into database"
    return {"response": response}


@app.put("/cars/{car_id}")
def update_car(car_id: int, car: Car):
    """
    """
    car_was_updated = repository.update_car(car_id, car)

    if not car_was_updated:
        status_code = 404
        message = f"Car not found for id {car_id}"

        raise HTTPException(status_code=status_code, detail=message) 

    response = f"Car with id ${car_id} updated in database." 
    return {"response": response}


@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    """"""
    car_was_deleted = repository.delete_car(car_id)

    if not car_was_deleted:
        status_code = 404
        message = f"Car not found for id {car_id}"

        raise HTTPException(status_code=status_code, detail=message) 

    response = f"Car with id #{car_id} deleted from database"
    return {"response": response}