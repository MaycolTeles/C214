"""
"""

from typing import Optional

from src.database import create_database
from src.movie_crud import MovieCrud
from src.movie_data import MovieData


def main() -> None:
    """
    """
    create_database()

    crud = MovieCrud()

    # LISTING ALL MOVIES
    response = crud.read_all()
    _print_response_in_table_format(response)

    # CREATING MOVIE 1
    movie_data = MovieData(
        name="Avatar",
        production_company="Lightstorm Entertainment",
        category="Sci-Fi",
        year=2009,
        score=10
    )

    crud.create(movie_data)
    print("\n")
    print("MOVIE CREATED!")

    # CREATING MOVIE 2
    movie_data = MovieData(
        name="Justice League - Snyder Cut",
        production_company="Warner Bros",
        category="Action",
        year=2021,
        score=10
    )

    crud.create(movie_data)
    print("\n")
    print("MOVIE CREATED!")

    # LISTING ALL MOVIES AGAIN
    response = crud.read_all()
    _print_response_in_table_format(response)

    # UPDATING MOVIE 1
    movie_data = MovieData(
        name="Avatar The Way of Water",
        production_company="Lightstorm Entertainment",
        category="Sci-Fi",
        year=2022,
        score=10
    )

    crud.update(1, movie_data)
    print("\n")
    print("MOVIE 1 UPDATED")

    # LISTING ALL MOVIES AGAIN
    response = crud.read_all()
    _print_response_in_table_format(response)

    # DELETING MOVIE 2
    response = crud.delete(2)
    print("\n")
    print("MOVIE 2 DELETED")

    # LISTING ALL MOVIES AGAIN
    response = crud.read_all()
    _print_response_in_table_format(response)


def _print_response_in_table_format(response: Optional[list[MovieData]]) -> None:
    """
    """
    if not response:
        print("\n")
        print("NO MOVIES IN THE TABLE!")
        return

    print("\n")
    print("************************************************************************************")

    headers_string_format = \
        f"{'NAME':<30}{'PRODUCTION COMPANY':<30}{'CATEGORY':<10}{'YEAR':<7}{'SCORE':<7}"
    print(headers_string_format)

    for movie in response:
        movies_string_format = f"{movie.name:<30}{movie.production_company:<30}\
            {movie.category:<10}{movie.year:<7}{movie.score:<7}"
        print(movies_string_format)

    print("************************************************************************************")


if __name__ == "__main__":
    main()
