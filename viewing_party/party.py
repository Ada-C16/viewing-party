
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

def get_most_watched_genre(janes_data):
    genres_dict = {}
    if not janes_data["watched"]:
        return None
    else: 
        for movie in janes_data["watched"]:
            if movie["genre"] not in genres_dict:
                genres_dict[movie["genre"]] = 1
            elif movie["genre"] in genres_dict:
                genres_dict[movie["genre"]] += 1
        most_watched_genre = max(genres_dict, key=genres_dict.get)
        return most_watched_genre

def get_unique_watched(amandas_data):
    friends_watched = []
    for friends in amandas_data["friends"]:
        for movie in friends["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)
    
    unique_watched = []
    for movie in amandas_data["watched"]:
        if movie not in friends_watched:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(amandas_data):
    friends_watched = []
    for friends in amandas_data["friends"]:
        for movie in friends["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)

    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in amandas_data["watched"]:
            friends_unique_watched.append(movie)
    
    return friends_unique_watched