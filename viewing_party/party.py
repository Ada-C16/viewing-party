
def create_movie(movie_title, genre, rating):
    movie = {}
    if movie_title is None or genre is None or rating is None:
        return None
    else:
        movie["title"] = movie_title
        movie["genre"] = genre
        movie["rating"] = rating    
        return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(janes_data, movie_title):
    watched_movie = janes_data["watchlist"][0]
    for movie in watched_movie.values():
        if movie == movie_title:
            janes_data["watchlist"].remove(watched_movie)
            janes_data["watched"].append(watched_movie)
    return janes_data





# print(create_movie("Title A", "Horror", 4)) # test 1
# print(create_movie(None, "Horror", 3.5)) # test 2
# print(create_movie("Title A", None, 4)) # test 3
# print(create_movie("Title A", "Horror", None)) # test 4
