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
# Comment

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_watched = movie
            break
    else: 
        return user_data  
    user_data["watched"].append(user_watched)
    user_data["watchlist"].remove(user_watched)
   
    return user_data