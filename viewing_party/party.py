def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        new_movie = {
            "title": movie_title,
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

def watch_movie(user_data, movie_to_watch):
    for movie_data in user_data["watchlist"]:
        if movie_data["title"] == movie_to_watch:
            user_data["watched"].append(movie_data)
            user_data["watchlist"].remove(movie_data)
    
    return user_data

def get_watched_avg_rating(user_data):
    average_data = []
    for movie_data in user_data["watched"]:
        average_data.append(movie_data["rating"])
    
    return sum(average_data)/len(average_data)

