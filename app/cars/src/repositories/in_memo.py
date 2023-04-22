"""
"""

from typing import Dict, Optional

from models import Car


class InMemoRepository:
    """
    """
    _records: Dict[int, Car] = {}

    def create_car(self, car: Car) -> int:
        """
        """
        next_id = len(self._records) + 1
        car_id = next_id

        self._records[car_id] = car

        return car_id

    def read_all_cars(self) -> Dict[int, Car]:
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

    def delete_car(self, car_id: int) -> Optional[Car]:
        """
        """
        response = self._records.pop(car_id, None)
        return response
