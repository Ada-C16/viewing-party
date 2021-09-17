##WAVE 01##
def create_movie(title,genre,rating):
    new_movie = {}
    empty = None
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return empty

def add_to_watched(user_data,movie):
    user_list = user_data["watched"]
    user_list.append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    watch_list = user_data["watchlist"]

    for movie in watch_list:
        if title in movie.values():
            watched_movie = watch_list.pop()
            user_data["watched"].append(watched_movie)
    return user_data


##WAVE 02##
def get_watched_avg_rating(user_data):
    ratings_list =[]
    avg_rating = 0
    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])
    if len(ratings_list) > 0:
        avg_rating = sum(ratings_list) / len(ratings_list)
    return float(avg_rating)

def get_most_watched_genre(user_data):
    genre_freq = {}
    for movie in user_data["watched"]:
        genre_key = movie["genre"]
        if genre_key in genre_freq:
            genre_freq[genre_key] += 1
        else:
            genre_freq[genre_key] = 1
    if len(genre_freq) > 0:
        most_watched = max(genre_freq, key=genre_freq.get)
        return most_watched

## WAVE 03 ##
def get_unique_watched(user_data):
    user_unique_movies =[]
    friends_watched = []
    user_watched = user_data["watched"]

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
    for movie in user_watched:
        if movie in friends_watched:
            continue
        user_unique_movies.append(movie)
    return user_unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies =[]
    friends_watched = []
    user_watched = user_data["watched"]

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
    for movie in friends_watched:
        if movie in user_watched:
            continue
        if movie not in friends_unique_movies:
            friends_unique_movies.append(movie)
    return friends_unique_movies