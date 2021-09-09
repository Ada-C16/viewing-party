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
    titlesearch = list(filter(lambda m: m["title"] == title, user_data["watchlist"]))
    if titlesearch:
        movie = titlesearch.pop() # assume unique title
        user_data["watchlist"] = list(filter(lambda m: m["title"] != title, user_data["watchlist"]))
        user_data["watched"].append(movie)
    return user_data

# wave 2

def get_watched_avg_rating(user_data):
    ratings = [m["rating"] for m in user_data["watched"]]
    return sum(ratings)/len(ratings) if ratings else 0.0

def get_most_watched_genre(user_data):
    genres = [m["genre"] for m in user_data["watched"]]
    return max(set(genres), key=genres.count) if genres else None


