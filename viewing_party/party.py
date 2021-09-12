# wave 1


def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data = add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data


# wave 2


def get_watched_avg_rating(user_data):
    ratings = [movie["rating"] for movie in user_data["watched"]]
    return sum(ratings) / len(ratings) if ratings else 0.0


def get_most_watched_genre(user_data):
    genres = [movie["genre"] for movie in user_data["watched"]]
    return max(set(genres), key=genres.count) if genres else None


# wave 3


def get_unique_watched(user_data):
    friends_watched = [
        movie["title"] for friend in user_data["friends"] for movie in friend["watched"]
    ]
    return [
        movie for movie in user_data["watched"] if movie["title"] not in friends_watched
    ]


def get_friends_unique_watched(user_data):
    friends_watched = dict()
    user_watched_titles = [movie["title"] for movie in user_data["watched"]]
    for friend in user_data["friends"]:
        friends_watched.update(
            {
                movie["title"]: movie
                for movie in friend["watched"]
                if movie["title"] not in user_watched_titles
            }
        )
    return friends_watched.values()


# wave 4


def get_available_recs(user_data):
    all_recs = get_friends_unique_watched(user_data)
    return [movie for movie in all_recs if movie["host"] in user_data["subscriptions"]]


# wave 5


def get_new_rec_by_genre(user_data):
    favg = get_most_watched_genre(user_data)
    all_recs = get_friends_unique_watched(user_data)
    return [movie for movie in all_recs if movie["genre"] is favg]


def get_rec_from_favorites(user_data):
    all_recs = get_unique_watched(user_data)
    user_favs = [movie["title"] for movie in user_data["favorites"]]
    return [movie for movie in all_recs if movie["title"] in user_favs]
