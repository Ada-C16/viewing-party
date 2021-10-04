
def create_movie(movie_title, genre, rating):
    movie = {}
    if movie_title is None or genre is None or rating is None:
        return None
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

def watch_movie(user_data, watched_movie):
    for movie in user_data["watchlist"]:
        if movie == watched_movie or watched_movie == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

def get_watched_avg_rating(user_data):
    watched_ratings = []
    if not user_data["watched"]:
        return 0 
    for movie in user_data["watched"]: 
        watched_ratings.append(movie["rating"])
    sum_watched_ratings = sum(watched_ratings)
    avg_watched_rating = sum_watched_ratings/len(watched_ratings)
    return avg_watched_rating

def get_most_watched_genre(user_data):
    genres_dict = {}
    if not user_data["watched"]:
        return None
    for movie in user_data["watched"]:
        if movie["genre"] not in genres_dict:
            genres_dict[movie["genre"]] = 1
        elif movie["genre"] in genres_dict:
            genres_dict[movie["genre"]] += 1
    most_watched_genre = max(genres_dict, key=genres_dict.get)
    return most_watched_genre

# helper function
def get_friends_watched(user_data):
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)
    return friends_watched

def get_unique_watched(user_data):
    friends_watched = get_friends_watched(user_data)
    
    unique_watched = []
    for movie in user_data["watched"]:
        if movie not in friends_watched:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    friends_watched = get_friends_watched(user_data)

    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in user_data["watched"]:
            friends_unique_watched.append(movie)
    
    return friends_unique_watched

def get_available_recs(user_data):
    # creates a list of movies in user's friends watched lists
    friends_watched_mov = get_friends_watched(user_data)
    
    # creates a list of the services user's friends have
    friends_watched_serv = []
    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            if movie["host"] not in friends_watched_serv:
                friends_watched_serv.append(movie["host"])
    
    # adds movies to available recommendation list if user is subscribed to that service
    available_recs = []
    for service in friends_watched_serv:
        if service in user_data["subscriptions"]:
            for item in friends_watched_mov:
                if service == item["host"]:
                    available_recs.append(item)
    
    # removes movies from available recommendations if user has already watched them
    for movie in user_data["watched"]:
        for rec in available_recs:
            if movie["title"] in rec.values():
                available_recs.remove(rec)

    return available_recs

def get_new_rec_by_genre(user_data):
    friends_watched = get_friends_watched(user_data)
    sonyas_genres = [movie["genre"] for movie in user_data["watched"]]
    
    recommendations = []
    for movie in friends_watched:
        if movie["genre"] in sonyas_genres and movie not in user_data["watched"]:
            recommendations.append(movie)
    
    return recommendations

def get_rec_from_favorites(user_data):
    favorites = [movie for movie in user_data["favorites"]]
    friends_watched = get_friends_watched(user_data)
    
    # remove movie from favorites if a friend has already seen it
    for movie in friends_watched:
        if movie in favorites:
            favorites.remove(movie)
    
    return favorites