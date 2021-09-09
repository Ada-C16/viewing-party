from statistics import mode

#wave 1
def create_movie(title, genre, rating): 
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]

    for i in range(len(watchlist)):
        if title in watchlist[i].values():
            movie = watchlist.pop(i)
            add_to_watched(user_data, movie)
    
    return user_data

#wave 2
def get_watched_avg_rating(user_data):
    movies_watched = user_data["watched"]
    num_of_movies_watched = len(movies_watched)

    sum_of_ratings = 0

    for movie in movies_watched:
        sum_of_ratings += movie["rating"]

    if movies_watched:
        avg_rating = sum_of_ratings / num_of_movies_watched
    else:
        avg_rating = 0.0
    
    return avg_rating

def get_most_watched_genre(user_data):
    movies_watched = user_data["watched"]
    genres = []

    if movies_watched:
        for movie in movies_watched:
            genres.append(movie["genre"])

        most_watched_genre = mode(genres)
        return most_watched_genre

    else:
        return None

def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]

    friends_movie_titles = []
    for friend in friends_watched:
        for movie in friend["watched"]:
            friends_movie_titles.append(movie['title'])

    unique_watched = []
    for movie in user_watched:
        if movie['title'] not in friends_movie_titles:
            unique_watched.append(movie)
    
    return unique_watched

def get_friends_unique_watched(user_data):
    pass