
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

def watch_movie(janes_data, watched_movie):
    for movie in janes_data["watchlist"]:
        if movie == watched_movie or watched_movie == movie["title"]:
            janes_data["watched"].append(movie)
            janes_data["watchlist"].remove(movie)
    return janes_data

def get_watched_avg_rating(janes_data):
    watched_ratings = []
    if not janes_data["watched"]:
        return 0
    else: 
        for movie in janes_data["watched"]: 
            watched_ratings.append(movie["rating"])
        sum_watched_ratings = sum(watched_ratings)
        avg_watched_rating = sum_watched_ratings/len(watched_ratings)
        return avg_watched_rating


# print(create_movie("Title A", "Horror", 4)) # test 1
# print(create_movie(None, "Horror", 3.5)) # test 2
# print(create_movie("Title A", None, 4)) # test 3
# print(create_movie("Title A", "Horror", None)) # test 4
