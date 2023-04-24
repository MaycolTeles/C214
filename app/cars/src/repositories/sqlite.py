"""
"""

from typing import Dict, Optional, Union
import sqlite3

from models import Car
from repository import Repository


_DB_FULL_NAME = "cars.db"


def run_query(query: str, values: Optional[tuple[Union[str, int], ...]]=None, fetch_all: bool = True):
    """
    """
    if values is None:
        values = ()

    connection = sqlite3.connect(_DB_FULL_NAME)
    cursor = connection.cursor()    

    cursor.execute(query, values)

    if fetch_all:
        response = cursor.fetchall()

    else:
        response = cursor.rowcount

    connection.commit()
    connection.close()

    return response


def create_database() -> None:
    """
    """
    query = '''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT,
            model TEXT,
            year INTEGER,
            color TEXT
        )
    '''

    run_query(query)


class SQLiteRepository(Repository):
    """
    """

    def __init__(self) -> None:
        """"""
        create_database()

    def create_car(self, car: Car) -> None:
        """
        """
        query = '''
            INSERT INTO cars (brand, model, year, color)
            VALUES (?, ?, ?, ?);
        '''

        values = (
            car.brand,
            car.model,
            car.year,
            car.color
        )

        run_query(query, values)

    def read_car_by_id(self, car_id: int) -> Optional[Car]:
        """
        """
        query = '''
            SELECT * FROM cars WHERE id = ?;
        '''

        values = (car_id,)

        response = run_query(query, values)

        if not response:
            return

        car_id = response[0]
        
        car_brand, car_model, car_year, car_color = response[1:]

        car = Car(
            brand=car_brand,
            model=car_model,
            year=car_year,
            color=car_color
        )

        return car

    def read_all_cars(self) -> Optional[Dict[int, Car]]:
        """
        """
        query = '''
            SELECT * FROM cars;
        '''

        response = run_query(query)

        if not response:
            return

        cars: Dict[int, Car] = {}

        for car_record in response:
            car_id = car_record[0]
            
            car_brand, car_model, car_year, car_color = car_record[1:]

            car = Car(
                brand=car_brand,
                model=car_model,
                year=car_year,
                color=car_color
            )
            cars[car_id] = car

        return cars

    def update_car(self, car_id: int, car: Car) -> bool:
        """
        """
        query = '''
            UPDATE cars
            SET
                brand=?,
                model=?,
                year=?,
                color=?
            WHERE id=?;
        '''

        values = (
            car.brand,
            car.model,
            car.year,
            car.color,
            car_id
        )

        response = run_query(query, values, fetch_all=False)

        if response == 0:
            return False
        
        return True

    def delete_car(self, car_id: int) -> bool:
        """
        """
        query = '''
            DELETE FROM cars WHERE id=?;
        '''
        
        values = (car_id,)

        response = run_query(query, values, fetch_all=False)

        if response == 0:
            return False

        return True
