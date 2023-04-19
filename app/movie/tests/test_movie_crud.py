"""
"""

from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.movie_crud import MovieCrud
from src.movie_data import MovieData


class MovieCrudTestCase(TestCase):
    """
    """

    def setUp(self) -> None:
        """
        """
        self._name = "Avatar"
        self._production_company = "Lightstorm Entertainment"
        self._category = "Sci-Fi"
        self._year = 2009
        self._score = 10

        self._movie_data = MovieData(
            name=self._name,
            production_company=self._production_company,
            category=self._category,
            year=self._year,
            score=self._score,
        )

        self._movie_crud = MovieCrud()

    @patch("src.movie_crud.run_query")
    def test_should_create_new_movie(self, database_mock: MagicMock) -> None:
        """
        """
        # GIVEN INSERT QUERY AND MOVIE DATA
        query = '''
            INSERT INTO movies (name, production_company, category, year, score)
            VALUES (?, ?, ?, ?, ?);
        '''

        values = (
            self._name,
            self._production_company,
            self._category,
            self._year,
            self._score
        )

        # WHEN MOVIE CRUD CREATE IS CALLED
        self._movie_crud.create(self._movie_data)

        # THEN ASSERT DATABASE WAS CALLED
        database_mock.assert_called_once_with(query, values)

    @patch("src.movie_crud.run_query")
    def test_should_read_specific_movie_based_on_its_id(self, database_mock: MagicMock) -> None:
        """
        """
        # GIVEN SELECT QUERY AND MOVIE ID
        query = '''
            SELECT * FROM movies WHERE id = ?;
        '''

        movie_id = 1

        values = (movie_id,)

        # WHEN MOVIE CRUD READ IS CALLED
        database_mock.return_value = [
            self._name,
            self._production_company,
            self._category,
            self._year,
            self._score,
        ]

        movie = self._movie_crud.read(movie_id)

        # THEN ASSERT DATABASE WAS CALLED
        database_mock.assert_called_once_with(query, values)
        self.assertEqual(movie, self._movie_data)

    @patch("src.movie_crud.run_query")
    def test_should_try_to_read_specific_movie_based_on_its_id_but_no_record_was_found(self, database_mock: MagicMock) -> None:
        """
        """
        # GIVEN SELECT QUERY AND MOVIE ID
        query = '''
            SELECT * FROM movies WHERE id = ?;
        '''

        movie_id = 1

        values = (movie_id,)

        # WHEN MOVIE CRUD READ IS CALLED
        database_mock.return_value = []

        movie = self._movie_crud.read(movie_id)

        # THEN ASSERT DATABASE WAS CALLED
        database_mock.assert_called_once_with(query, values)
        self.assertIsNone(movie)

    @patch("src.movie_crud.run_query")
    def test_should_read_all_movies_and_return_three_movies_data(self, database_mock: MagicMock) -> None:
        """
        """
        # GIVEN SELECT QUERY
        query = '''
            SELECT * FROM movies;
        '''

        # WHEN MOVIE CRUD READ ALL IS CALLED
        database_mock.return_value = [
            [
                1,
                self._name,
                self._production_company,
                self._category,
                self._year,
                self._score,
            ],
            [
                2,
                self._name,
                self._production_company,
                self._category,
                self._year,
                self._score,
            ],
            [
                3,
                self._name,
                self._production_company,
                self._category,
                self._year,
                self._score,
            ]
        ]

        movies = self._movie_crud.read_all()

        # THEN ASSERT DATABASE WAS CALLED
        database_mock.assert_called_once_with(query)
        self.assertEqual(len(movies), 3)

    @patch("src.movie_crud.run_query")
    def test_should_read_all_movies_and_return_zero_movie_data(self, database_mock: MagicMock) -> None:
        """
        """
        # GIVEN SELECT QUERY
        query = '''
            SELECT * FROM movies;
        '''

        # WHEN MOVIE CRUD READ ALL IS CALLED
        database_mock.return_value = []

        movies = self._movie_crud.read_all()

        # THEN ASSERT DATABASE WAS CALLED
        database_mock.assert_called_once_with(query)
        self.assertIsNone(movies)

    @patch("src.movie_crud.run_query")
    def test_should_update_a_movie(self, database_mock: MagicMock) -> None:
        """
        """
        # GIVEN UPDATE QUERY AND MOVIE DATA
        query = '''
            UPDATE movies
            SET
                name=?,
                production_company=?,
                category=?,
                year=?,
                score=?
            WHERE id=?;
        '''

        movie_id = 1

        values = (
            self._name,
            self._production_company,
            self._category,
            self._year,
            self._score,
            movie_id
        )

        # WHEN MOVIE CRUD UPDATE IS CALLED
        self._movie_crud.update(movie_id, self._movie_data)

        # THEN ASSERT DATABASE WAS CALLED
        database_mock.assert_called_once_with(query, values)

    @patch("src.movie_crud.run_query")
    def test_should_delete_a_movie(self, database_mock: MagicMock) -> None:
        """
        """
        # GIVEN DELETE QUERY AND MOVIE DATA
        query = '''
            DELETE FROM movies WHERE id=?;
        '''

        movie_id = 1
        
        values = (movie_id,)

        # WHEN MOVIE CRUD DELETE IS CALLED
        self._movie_crud.delete(movie_id)

        # THEN ASSERT DATABASE WAS CALLED
        database_mock.assert_called_once_with(query, values)
