
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

def get_available_recs(amandas_data):
    # creates a list of movies in user's friends watched lists
    friends_watched_mov = []
    for friends in amandas_data["friends"]:
        for movie in friends["watched"]:
            if movie not in friends_watched_mov:
                friends_watched_mov.append(movie)
    
    # creates a list of the services user's friends have
    friends_watched_serv = []
    for friends in amandas_data["friends"]:
        for movie in friends["watched"]:
            if movie["host"] not in friends_watched_serv:
                friends_watched_serv.append(movie["host"])
    
    # adds movies to available recommendation list if user is subscribed to that service
    available_recs = []
    for service in friends_watched_serv:
        if service in amandas_data["subscriptions"]:
            for item in friends_watched_mov:
                if service == item["host"]:
                    available_recs.append(item)
    
    # removes movies from available recommendations if user has already watched them
    for movie in amandas_data["watched"]:
        for rec in available_recs:
            if movie["title"] in rec.values():
                available_recs.remove(rec)

    return available_recs

def get_new_rec_by_genre(sonyas_data):
    # consider making this a helper function - it's used 3 times accross difference functions
    friends_watched = []
    for friend in sonyas_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)
    
    sonyas_genres = []
    for movie in sonyas_data["watched"]:
        if movie["genre"] not in sonyas_genres:
            sonyas_genres.append(movie["genre"])
    
    recommendations = []
    for movie in friends_watched:
        if movie["genre"] in sonyas_genres and movie not in sonyas_data["watched"]:
            recommendations.append(movie)
    
    return recommendations

def get_rec_from_favorites(sonyas_data):
    favorites = []
    for movie in sonyas_data["favorites"]:
        if movie not in favorites:
            favorites.append(movie)

    friends_watched = []
    for friend in sonyas_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)
    
    # remove movie from favorites if a friend has already seen it
    for movie in friends_watched:
        if movie in favorites:
            favorites.remove(movie)
    
    return favorites



