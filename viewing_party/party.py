# Wave 1
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating,
             }
        return movie_dict
    else:
        return None


def add_to_watched(user_data, movie):
    if movie:
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = []
    return user_data


def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
    else:
        user_data["watchlist"] = []
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    
    for movie in watchlist:
        if title in movie["title"]:
            watchlist.remove(movie)
            watched.append(movie)
            break
    return user_data


# Wave 2
def get_watched_avg_rating(user_data):
    watched = user_data["watched"]

    if len(watched) > 0:
        rating_sum = 0.0
        for movie in watched:
            for key, value in movie.items():
                if key == "rating":
                    rating_sum += value
                average_rating = rating_sum / len(movie)
    if len(watched) == 0:
        average_rating = 0.0
    
    return average_rating


def get_most_watched_genre(user_data):
    pass
    # determined most_watched
    # return most_watched


# Wave 3
# Wave 4
# Wave 5


