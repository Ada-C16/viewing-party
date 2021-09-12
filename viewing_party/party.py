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

def get_watched_avg_rating(user_data):
    ratings = make_avg_rating_list(user_data)
    num_ratings = len(ratings)
    if num_ratings > 0:
        avg_rating = sum(ratings)/num_ratings
        return avg_rating
    else:
        return 0.0

def make_avg_rating_list(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    return ratings

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    else:
        watched_genres = make_watched_genre_list(user_data)
        most_watched_genre = max(watched_genres, key = watched_genres.count)
        return most_watched_genre

def make_watched_genre_list(user_data):
    watched_genres = []
    for movie in user_data["watched"]:
        watched_genres.append(movie["genre"])
    return watched_genres

