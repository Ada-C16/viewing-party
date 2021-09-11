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
    return user_data dictionary with movie dictionary added to "watched" list
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
            user_data = add_to_watched(user_data, item)

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


# wave 3
def get_unique_watched(user_data):
    """
    returns list of movies user has watched and friends have not watched
    """
    friends_watched_titles = []

    # create list of movie titles friends have watched
    for friend in user_data["friends"]:
        friends_watched_titles += [movie["title"]
                                   for movie in friend["watched"]]

    # build a list of movies only the user has seen
    unique_movies = [movie for movie in user_data["watched"]
                     if movie["title"] not in friends_watched_titles]
    return unique_movies


def get_friends_unique_watched(user_data):
    """
    returns a list of movies the friends have seen but the user has not
    """
    friends_watched = {}
    user_watched_titles = [movie["title"] for movie in user_data["watched"]]
    for friend in user_data["friends"]:
        # create a dictionary of movies in the format title: movie dictionary
        # duplicate movies will get overridden due to the key, so there will be no duplicates
        friends_watched.update(
            {movie["title"]: movie for movie in friend["watched"] if movie["title"] not in user_watched_titles})
    # convert dictionary to a list of dictionaries
    unique_movies = list(friends_watched.values())
    return unique_movies


# wave 4
def get_available_recs(user_data):
    """
    returns list of movie dictionaries the user has not watched but has the subscription for
    """
    friends_watched = get_friends_unique_watched(user_data)
    recs = [movie for movie in friends_watched if movie["host"]
            in user_data["subscriptions"]]
    return recs


# wave 5
def get_new_rec_by_genre(user_data):
    """
    returns list of movie dictionaries the user has not watched that match the user's most watched genre
    """
    friends_watched = get_friends_unique_watched(user_data)
    genre = get_most_watched_genre(user_data)

    recs = [movie for movie in friends_watched if movie["genre"] == genre]
    return recs


def get_rec_from_favorites(user_data):
    """
    returns list of movie dictionaries that are in the user's favorites and none of their friends have watched
    """
    user_watched = get_unique_watched(user_data)
    recs = [movie for movie in user_watched if movie in user_data["favorites"]]
    return recs
