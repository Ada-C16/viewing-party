def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data    

def watch_movie(user_data, title):
    new_watchlist = []
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
        else:
            new_watchlist.append(movie)
    user_data["watchlist"] = new_watchlist
    return user_data
