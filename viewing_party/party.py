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