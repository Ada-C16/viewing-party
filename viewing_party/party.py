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
    for movie in filter(lambda m: m["title"] == title, user_data["watchlist"]):
        user_data["watchlist"] = [
            m for m in user_data["watchlist"] if m["title"] != title
        ]
        user_data["watched"].append(movie)
        break  # prevent multiple matches
    return user_data


# wave 2


def get_watched_avg_rating(user_data):
    ratings = [m["rating"] for m in user_data["watched"]]
    return sum(ratings) / len(ratings) if ratings else 0.0


def get_most_watched_genre(user_data):
    genres = [m["genre"] for m in user_data["watched"]]
    return max(set(genres), key=genres.count) if genres else None


# wave 3


def get_unique_watched(user_data):
    friends_watched = set()
    for friend in user_data["friends"]:
        friends_watched.update([m["title"] for m in friend["watched"]])
    return [m for m in user_data["watched"] if m["title"] not in friends_watched]


def get_friends_unique_watched(user_data):
    friends_watched = dict()
    user_watched_titles = [m["title"] for m in user_data["watched"]]
    for friend in user_data["friends"]:
        friends_watched.update(
            {
                m["title"]: m
                for m in friend["watched"]
                if m["title"] not in user_watched_titles
            }
        )
    return friends_watched.values()


# wave 4


def get_available_recs(user_data):
    all_recs = get_friends_unique_watched(user_data)
    return [m for m in all_recs if m["host"] in user_data["subscriptions"]]


# wave 5


def get_new_rec_by_genre(user_data):
    favg = get_most_watched_genre(user_data)
    all_recs = get_friends_unique_watched(user_data)
    return [m for m in all_recs if m["genre"] is favg]


def get_rec_from_favorites(user_data):
    all_recs = get_unique_watched(user_data)
    user_favs = [m["title"] for m in user_data["favorites"]]
    return [m for m in all_recs if m["title"] in user_favs]
