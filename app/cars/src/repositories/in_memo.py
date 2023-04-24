"""
"""

from typing import Dict, Optional

from models import Car
from repository import Repository


class InMemoRepository(Repository):
    """
    """
    _records: Dict[int, Car] = {}

    def create_car(self, car: Car) -> None:
        """
        """
        next_id = len(self._records) + 1
        car_id = next_id

        self._records[car_id] = car

    def read_all_cars(self) -> Optional[Dict[int, Car]]:
        """"""
        return self._records

    def read_car_by_id(self, car_id: int) -> Optional[Car]:
        """
        """
        car = self._records.get(car_id)

        return car
    
    def update_car(self, car_id: int, car: Car) -> bool:
        """
        """
        if car_id not in self._records:
            return False

        self._records[car_id] = car

        return True

    def delete_car(self, car_id: int) -> bool:
        """
        """
        response = self._records.pop(car_id, None)

        if response is None:
            return False

        return True
