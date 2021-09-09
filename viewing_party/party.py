
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
    titlesearch = list(filter(lambda m: m["title"] == title, user_data["watchlist"]))
    if titlesearch:
        movie = titlesearch[0] # assume unique title
        user_data["watchlist"] = list(filter(lambda m: m["title"] != title, user_data["watchlist"]))
        user_data["watched"].append(movie)
    return user_data

