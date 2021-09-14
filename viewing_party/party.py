def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        new_movie = {"title": title, "genre": genre, "rating": rating,}
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            del user_data["watchlist"][i]
    return user_data
