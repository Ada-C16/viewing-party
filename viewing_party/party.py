import statistics


def create_movie(title, genre, rating):
    """
    Returns:
        new_movie (dict): A dictionary initialized with title (str), genre (str), and rating (float).
        Returns None if any parameters are falsy.
    """

    if title and genre and rating:
        new_movie = {"title": title, "genre": genre, "rating": rating}
        return new_movie
    return None


def add_to_watched(user_data, movie):
    """
    Returns:
        user_data (dict): Updated user_data with movie added to "watched".
    """

    user_data.get("watched").append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    """
    Returns:
        user_data (dict): Updated user_data with movie added to "watchlist".
    """

    user_data.get("watchlist").append(movie)
    return user_data


def watch_movie(user_data, title):
    """
    Returns:
        user_data (dict): The updated user_data with movie added to "watched" and movie removed from "watchlist".
    """

    watch_list = user_data.get("watchlist")
    for movie in watch_list:
        if title == movie.get("title"):
            user_data = add_to_watched(user_data, movie)
            watch_list.remove(movie)

    return user_data


def get_watched_avg_rating(user_data):
    """
    Returns:
        avg (float): The average rating of movies in "watched".
        0.0 returned if "watched" is empty.
    """

    if user_data["watched"]:
        ratings = [movie.get("rating") for movie in user_data.get("watched")]
        avg = statistics.mean(ratings)
        return avg
    return 0.0


def get_most_watched_genre(user_data):
    """
    Returns:
        most_watched (str): The most frequently occuring genre in "watched".
        None is returned if "watched" is empty.
    """

    if user_data.get("watched"):
        genres = [movie.get("genre") for movie in user_data.get("watched")]
        most_watched = statistics.mode(genres)
        return most_watched

    return None


def get_user_titles(user_data):
    """
    Returns:
        user_titles (set): A set containing all movie titles in user's "watched" list.
    """

    user_titles = set([movie.get("title") for movie in user_data.get("watched")])
    return user_titles


def get_friends_titles(user_data):
    """
    Returns:
        friends_titles (set): A set containing all movie titles in friends "watched" lists.
    """

    friends_titles = set()
    for friend in user_data.get("friends"):
        friends_titles.update(movie.get("title") for movie in friend.get("watched"))

    return friends_titles


def get_unique_watched(user_data):
    """
    Returns:
        unique_watched (list): A list containing the movie dictionaries that only the user has watched.
    """

    user_titles = get_user_titles(user_data)
    friends_titles = get_friends_titles(user_data)
    difference = user_titles.difference(friends_titles)

    unique_watched = [
        movie for movie in user_data.get("watched") if movie.get("title") in difference
    ]

    return unique_watched


def get_friends_unique_watched(user_data):
    """
    Returns:
        friends_unique_watched (list): A list containing the movie dictionaries that only
        the users friends have watched.
    """

    user_titles = get_user_titles(user_data)
    friends_titles = get_friends_titles(user_data)
    difference = friends_titles.difference(user_titles)

    friends_unique_watched = list()
    for friend in user_data["friends"]:
        for movie in friend.get("watched"):
            if movie.get("title") in difference and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)

    return friends_unique_watched


def get_available_recs(user_data):
    """
    Returns:
        recs (list): A list of recommended movies for the user.

    """

    friends_recs = get_friends_unique_watched(user_data)
    recs = [
        movie
        for movie in friends_recs
        if movie.get("host") in user_data.get("subscriptions")
    ]
    return recs


def get_new_rec_by_genre(user_data):
    """
    Returns:
        rec_by_genre (list): A list of recommened movies for user based off of the users
        most frequently watched genre.
    """

    user_genre = get_most_watched_genre(user_data)
    recs = get_friends_unique_watched(user_data)
    rec_by_genre = [rec for rec in recs if rec.get("genre") == user_genre]

    return rec_by_genre


def get_rec_from_favorites(user_data):
    """
    Returns:
        user_recommendations (list): A list of recommended movies from the users "favorites" list.
    """

    user_unique = get_unique_watched(user_data)
    user_recommendations = [
        movie for movie in user_unique if movie in user_data.get("favorites")
    ]

    return user_recommendations
