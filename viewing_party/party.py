def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    return {
        "title": title,
        "genre": genre,
        "rating": rating,
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if movie["title"] == title:
            watched_from_watchlist = movie
            break
        watched_from_watchlist = None
    if watched_from_watchlist:
        watchlist.remove(watched_from_watchlist)
        user_data["watched"].append(watched_from_watchlist)
    return user_data

