"""
"""

from typing import Dict, Optional, Union
import os
import sqlite3

from src.models import Car
from .repository import Repository


def get_database_path() -> str:
    """"""
    current_module_path = os.path.abspath(__file__)
    current_package_path = os.path.dirname(current_module_path)
    src_dir = os.path.dirname(current_package_path)
    cars_dir = os.path.dirname(src_dir)
    db_path = os.path.join(cars_dir, 'cars.db')

    return db_path


def run_query(
    query: str,
    values: Optional[tuple[Union[str, int], ...]] = None,
    fetch_all: bool = True
):
    """
    """
    if values is None:
        values = ()

    db_path = get_database_path()

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()    

    cursor.execute(query, values)

    if fetch_all:
        response = cursor.fetchall()

    else:
        response = cursor.rowcount

    connection.commit()
    connection.close()

    return response


class SQLiteRepository(Repository):
    """
    """

    def __init__(self) -> None:
        """"""
        self._create_database()

    @staticmethod
    def _create_database() -> None:
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

        car_id = response[0][0]
        
        car_brand, car_model, car_year, car_color = response[0][1:]

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
