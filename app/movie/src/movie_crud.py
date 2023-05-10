"""
"""
from typing import Optional

from src.database import run_query
from src.movie_data import MovieData


class MovieCrud:
    """
    """

    def create(self, movie_data: MovieData) -> None:
        """
        """
        name = movie_data.name
        production_company = movie_data.production_company
        category = movie_data.category
        year = movie_data.year
        score = movie_data.score

        query = '''
            INSERT INTO movies (name, production_company, category, year, score)
            VALUES (?, ?, ?, ?, ?);
        '''

        values = (
            name,
            production_company,
            category,
            year,
            score
        )

        run_query(query, values)

    def read(self, movie_id: int) -> Optional[MovieData]:
        """
        """
        query = '''
            SELECT * FROM movies WHERE id = ?;
        '''

        values = (movie_id,)

        response = run_query(query, values)

        if not response:
            return

        return MovieData(*response)

    def read_all(self) -> Optional[list[MovieData]]:
        """
        """
        query = '''
            SELECT * FROM movies;
        '''

        response = run_query(query)

        if not response:
            return

        movies: list[MovieData] = []

        for movie_record in response:
            movie = MovieData(*movie_record[1:])
            movies.append(movie)

        return movies

    def update(self, movie_id: int, movie_data: MovieData) -> None:
        """
        """
        name = movie_data.name
        production_company = movie_data.production_company
        category = movie_data.category
        year = movie_data.year
        score = movie_data.score

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

        data = (
            name,
            production_company,
            category,
            year,
            score,
            movie_id
        )

        run_query(query, data)

    def delete(self, movie_id: int) -> None:
        """
        """
        query = '''
            DELETE FROM movies WHERE id=?;
        '''

        data = (movie_id,)

        run_query(query, data)
