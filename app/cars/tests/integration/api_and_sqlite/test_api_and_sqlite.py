"""
Module containing the APIAndSQLiteTestCase Class.
"""

from typing import Dict, Union
from unittest import TestCase
from unittest.mock import patch

from fastapi.testclient import TestClient

from src.api import fastapi_app
from src.models import Car
from src.repositories.sqlite import SQLiteRepository, create_database, drop_database


class APIAndSQLiteTestCase(TestCase):
    """
    Class to test the API endpoints using the SQLite repository.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        """
        cls._client = TestClient(fastapi_app)
        cls._patch_repository_to_sqlite()
        cls._patch_database_name_to_test()

    @classmethod
    def tearDownClass(cls) -> None:
        """"""
        cls._repository_injection_patcher.stop()
        cls._database_path_patcher.stop()

    def setUp(self) -> None:
        """
        """
        self._create_test_db()

    def tearDown(self) -> None:
        """"""
        self._drop_test_db()

    @classmethod
    def _patch_repository_to_sqlite(cls) -> None:
        """
        """
        cls._repository_injection_patcher = patch(
            "src.dependencies.REPOSITORY_INJECTION", SQLiteRepository()
        )
        cls._repository_injection_patcher.start()

    @classmethod
    def _patch_database_name_to_test(cls) -> None:
        """
        """
        cls._database_path_patcher = patch(
            "src.repositories.sqlite.DATABASE_NAME", "test_cars.db"
        )
        cls._database_path_patcher.start()

    def _create_test_db(self) -> None:
        """
        """
        create_database()

    def _drop_test_db(self) -> None:
        """
        """
        drop_database()

    def _build_car(self, brand: str, model: str, year: int, color: str) -> Car:
        """
        Private Method to build a car.
        """
        car = Car(
            brand=brand,
            model=model,
            year=year,
            color=color
        )

        return car

    def _car_to_json(self, car: Car) -> Dict[str, Union[str, int]]:
        """
        Private method to convert the car to JSON format.
        """
        json = {
            "brand": car.brand,
            "model": car.model,
            "year": car.year,
            "color": car.color,
        }
        return json

    def test_should_get_all_cars_but_none_is_retrieved_since_db_is_empty(self) -> None:
        """
        Method to assert the api has a get method endpoint to retrieve all cars
        even though there are none in the sqlite database.
        """
        response = self._client.get("/cars")

        actual_status_code = response.status_code
        expected_status_code = 200

        actual_response_data = response.json()
        expected_response_data = {
            "cars": "No car found in database yet. Try adding some before retrieving any."
        }

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertEqual(actual_response_data, expected_response_data)

    def test_should_insert_a_car_then_retrieve_only_it(self) -> None:
        """
        Method to assert the api has a post method endpoint to insert car into
        sqlite database and then retrieve only it from a get method endpoint.
        """
        test_car_id = 1
        test_car = self._build_car("Fiat", "Cronos", 2023, "Black")
        test_params = self._car_to_json(test_car)

        response = self._client.post("/cars", json=test_params)

        actual_status_code = response.status_code
        expected_status_code = 201

        actual_response_data = response.json()
        expected_response_data = {"response": "Car added into the database."}

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertEqual(actual_response_data, expected_response_data)

        response = self._client.get(f"/cars/{test_car_id}")

        actual_status_code = response.status_code
        expected_status_code = 200

        actual_response_data = response.json()
        expected_response_data = {
            "car": self._car_to_json(test_car)
        }

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertDictEqual(actual_response_data, expected_response_data)

    def test_should_insert_three_cars_then_retrieve_only_the_first_inserted(self) -> None:
        """
        Method to assert the api has a post method endpoint to insert three cars into
        sqlite database and then retrieve only the first that was inserted
        from a get method endpoint.
        """
        test_car_one_id = 1
        test_car_one = self._build_car("Fiat", "Cronos", 2023, "Black")
        test_car_two = self._build_car("Tesla", "S Plaid", 2023, "White")
        test_car_three = self._build_car("Hyundai", "Santa Fe", 2020, "Black")

        test_cars = [test_car_one, test_car_two, test_car_three]

        expected_status_code = 201
        expected_response_data = {"response": "Car added into the database."}

        for car in test_cars:
            parameters = self._car_to_json(car)
            response = self._client.post("/cars", json=parameters)

            actual_status_code = response.status_code
            actual_response_data = response.json()

            self.assertEqual(actual_status_code, expected_status_code)
            self.assertEqual(actual_response_data, expected_response_data)

        response = self._client.get(f"/cars/{test_car_one_id}")

        actual_status_code = response.status_code
        expected_status_code = 200

        actual_response_data = response.json()
        expected_response_data = {
            "car": self._car_to_json(test_car_one)
        }

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertDictEqual(actual_response_data, expected_response_data)

    def test_should_insert_three_cars_then_retrieve_them(self) -> None:
        """
        Method to assert the api has a post method endpoint to insert 3 cars into
        sqlite database and then retrieve them all from a get method endpoint.
        """
        test_car_one = self._build_car("Fiat", "Cronos", 2023, "Black")
        test_car_two = self._build_car("Tesla", "S Plaid", 2023, "White")
        test_car_three = self._build_car("Hyundai", "Santa Fe", 2020, "Black")

        test_cars = [test_car_one, test_car_two, test_car_three]

        expected_status_code = 201
        expected_response_data = {"response": "Car added into the database."}

        for car in test_cars:
            parameters = self._car_to_json(car)
            response = self._client.post("/cars", json=parameters)

            actual_status_code = response.status_code
            actual_response_data = response.json()

            self.assertEqual(actual_status_code, expected_status_code)
            self.assertEqual(actual_response_data, expected_response_data)

        response = self._client.get("/cars")

        actual_status_code = response.status_code
        expected_status_code = 200

        actual_response_data = response.json()
        expected_response_data = {
            "cars": {
                "1": self._car_to_json(test_car_one),
                "2": self._car_to_json(test_car_two),
                "3": self._car_to_json(test_car_three),
            }
        }

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertDictEqual(actual_response_data, expected_response_data)

    def test_should_insert_a_car_then_update_it(self) -> None:
        """
        Method to assert the api has a post method endpoint to insert a car into
        sqlite database and then update it from a put method endpoint.
        """
        test_car_id = 1
        test_car = self._build_car("Fiat", "Cronos", 2023, "Black")

        parameters = self._car_to_json(test_car)
        response = self._client.post("/cars", json=parameters)

        actual_status_code = response.status_code
        expected_status_code = 201

        actual_response_data = response.json()
        expected_response_data = {"response": "Car added into the database."}

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertEqual(actual_response_data, expected_response_data)

        test_new_car = self._build_car("Tesla", "S Plaid", 2024, "White")

        new_car_parameters = self._car_to_json(test_new_car)
        response = self._client.put(f"/cars/{test_car_id}", json=new_car_parameters)

        actual_status_code = response.status_code
        expected_status_code = 200

        actual_response_data = response.json()
        expected_response_data = {
            "response": f"Car with id #{test_car_id} updated in database."
        }

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertDictEqual(actual_response_data, expected_response_data)

    def test_should_insert_a_car_then_delete_it(self) -> None:
        """
        Method to assert the api has a post method endpoint to insert a car into
        sqlite database and then delete it from a delete method endpoint.
        """
        test_car_id = 1
        test_car = self._build_car("Fiat", "Cronos", 2023, "Black")

        parameters = self._car_to_json(test_car)
        response = self._client.post("/cars", json=parameters)

        actual_status_code = response.status_code
        expected_status_code = 201

        actual_response_data = response.json()
        expected_response_data = {"response": "Car added into the database."}

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertEqual(actual_response_data, expected_response_data)

        response = self._client.delete(f"/cars/{test_car_id}")

        actual_status_code = response.status_code
        expected_status_code = 200

        actual_response_data = response.json()
        expected_response_data = {
            "response": f"Car with id #{test_car_id} deleted from database."
        }

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertDictEqual(actual_response_data, expected_response_data)
