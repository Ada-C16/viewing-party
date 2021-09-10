import stat
import statistics


# wave 1
def create_movie(movie_title, genre, rating):
    """
    return movie dictionary if all parameters included
    """
    if movie_title and genre and rating:
        movie = {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }

        return movie


def add_to_watched(user_data, movie):
    """
    return user_data dictionary with movie dictionaryh added to "watched" list
    """
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    """
    returns user_data dictionary with movie dictionary added to "watchlist" list
    """
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie):
    """
    returns user_data dictionary with movie moved to "watched" list from "watchlist" list
    """
    for item in user_data["watchlist"]:
        if item["title"] == movie:
            user_data["watchlist"].remove(item)
            user_data["watched"].append(item)

    return user_data


# wave 2
def get_watched_avg_rating(user_data):
    """
    returns average rating of movies in watched list
    """
    ratings = [movie["rating"] for movie in user_data["watched"]]
    avg = statistics.mean(ratings) if ratings else 0
    return avg


def get_most_watched_genre(user_data):
    """
    returns most watched genre from user_data
    """
    genres = [movie["genre"] for movie in user_data["watched"]]
    most_watched = statistics.mode(genres) if genres else None
    return most_watched
