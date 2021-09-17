from collections import Counter


def create_movie(title, genre, rating):
    if title is None:
        return None
    if genre is None:
        return None
    if rating is None:
        return None

    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            add_to_watched(user_data, movie)
    return user_data


def get_watched_avg_rating(user_data):
    ratings_list = []

    if len(user_data["watched"]) == 0:
        return 0.0

    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])

    average_rating = sum(ratings_list) / len(ratings_list)
    return average_rating


def get_most_watched_genre(user_data):
    genre_list = []

    if user_data["watched"] == []:
        return None

    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])

    occurence_count = Counter(genre_list)
    return occurence_count.most_common(1)[0][0]


def get_unique_watched(user_data):
    user_set = set()
    friends_set = set()
    user_list = []

    for movie in user_data["watched"]:
        user_set.add(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_set.add(movie["title"])

    user_watched_movies_not_by_friends = user_set - friends_set

    for movie in user_watched_movies_not_by_friends:
        user_list.append({"title": movie})
    return user_list


def get_friends_unique_watched(user_data):
    user_set = set()
    friends_set = set()
    friends_list = []

    for movie in user_data["watched"]:
        user_set.add(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_set.add(movie["title"])

    friends_watched_movies_not_by_user = friends_set - user_set

    for movie in friends_watched_movies_not_by_user:
        friends_list.append({"title": movie})
    return friends_list


def get_available_recs(user_data):
    recommended_movies_list = []
    user_watched_set = set()
    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])

    subscription_set = set(user_data["subscriptions"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_set\
                    and movie["host"] in subscription_set\
                    and movie not in recommended_movies_list:
                recommended_movies_list.append(movie)

    return recommended_movies_list


def get_new_rec_by_genre(user_data):
    recommended_movies_list = []
    user_watched_set = set()
    most_watched_genre = get_most_watched_genre(user_data)

    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_set\
                and movie not in recommended_movies_list\
                    and movie["genre"] == most_watched_genre:
                recommended_movies_list.append(movie)

    return recommended_movies_list


def get_rec_from_favorites(user_data):
    recommended_movies_list = []
    user_favorite_movie_set = set()
    friends_watched_set = set()

    for movie in user_data["favorites"]:
        user_favorite_movie_set.add(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_set.add(movie["title"])

    for movie in user_data["watched"]:
        if movie["title"] in user_favorite_movie_set and movie["title"] not in friends_watched_set:
            recommended_movies_list.append(movie)

    return recommended_movies_list
