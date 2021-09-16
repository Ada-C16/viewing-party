def create_movie(movie_title, genre, rating):
    '''
    function builds a dictionary with three key value 
    pairs where each value is the relevant parameter for each movie
    '''
    if movie_title == None or genre == None or rating == None:
        return None
    new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
        }
    print(new_movie)
    return new_movie


def add_to_watched(user_data, movie):
    '''
    function adds a specific movie title to the users 
    list of watched movies
    '''
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    '''
    function adds a specific movie title to the users 
    list of movies to wacth
    '''
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    '''
    function checks if movie is in users watchlist. if so, adds 
    movie to users watched list and removes it from users watchlist. 
    returns updated user lists
    '''
    movies_to_remove = []
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            movies_to_remove.append(movie)

    if len(movies_to_remove) == 0:
        return user_data
    else:
        for movie in movies_to_remove:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data


def get_watched_avg_rating(user_data):
    '''
    function gets average rating for the movies that are in 
    users list fo watched movies
    '''
    ratings = []
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        for movie in user_data["watched"]:
            ratings.append(movie["rating"])
        num_of_movies = len(ratings)
        ratings_total = sum(ratings)
        avg_rating = ratings_total / num_of_movies
        return avg_rating


def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    popular_genres = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in popular_genres:
            popular_genres[movie["genre"]] = 1
        else:
            popular_genres[movie["genre"]] += 1
    popularity = 0
    for genre, popularity_value in popular_genres.items():
        if popularity_value > popularity:
            popularity = popularity_value
            most_popular_genre = genre
    return most_popular_genre


def get_unique_watched(user_data):
    '''
    function returns list of movies that are in users watched list
    but not in any of the users friends watched list. the movies
    in the returned list are unique to the user.
    '''
    friends_watched = get_friends_watched_list(user_data)
    unique_movies = []
    for movie in user_data["watched"]:
        if movie not in friends_watched:
            unique_movies.append(movie)
    return unique_movies


def get_friends_unique_watched(user_data):
    '''
    function returns list of movies that are in user's friends 
    watched list but not in the users watched list. the movies 
    in the returned list are unique to the user's friends.
    '''
    friends_watched = get_friends_watched_list(user_data)
    friends_unique_movies = []
    for movie in friends_watched:
        if movie not in user_data["watched"] and movie not in friends_unique_movies:
            friends_unique_movies.append(movie)
    return friends_unique_movies


def get_available_recs(user_data):
    '''
    functions gets movie recommendations for user based on the
    movies that the user's friends have watched. function checks if
    the movie is in a subscription that the user has and the user 
    has not watched the movie yet. returns list of recommendations.
    '''
    recommendations = []
    user_subscriptions = user_data["subscriptions"]
    friends_watched = get_friends_watched_list(user_data)
    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie["title"])

    for movie in friends_watched:
        if movie["host"] in user_subscriptions and \
        movie["title"] not in user_watched \
        and movie not in recommendations:
            recommendations.append(movie)
    return recommendations


def get_new_rec_by_genre(user_data):
    '''
    functions gets movie recommendations for user based on the
    genre of movies that the user has watched and the movies of that 
    specific genre that user's friends have watched. function checks if
    the movie is not in the users watched list.
    returns list of recommendations by genre.
    '''
    user_genre_watched = []
    recommendations = []

    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]:
            user_genre_watched.append(movie["genre"])
    else:
        return recommendations

    friends_watched = get_friends_watched_list(user_data)

    for movie in friends_watched:
        if movie["genre"] in user_genre_watched\
        and movie not in recommendations\
        and movie not in user_data["watched"]:
            recommendations.append(movie)
    return recommendations


def get_rec_from_favorites(user_data):
    '''
    functions gets movie recommendations for user based on the
    list of user favorites. function checks if the movie is not 
    in the user's friends watched list. returns list of 
    recommendations that are a user favorite and have not been 
    watched by user's frineds.
    '''
    user_favorites = []
    recommendations = []
    if len(user_data["favorites"]) > 0:
        for movie in user_data["favorites"]:
            user_favorites.append(movie)
    else:
        return recommendations
    
    friends_watched = get_friends_watched_list(user_data)

    for movie in user_favorites:
        if movie not in friends_watched:
            recommendations.append(movie)
    return recommendations

def get_friends_watched_list(user_data):
    '''
    function creates list of movies watched by user's friends. 
    returns list of dictionaries where key is title and value 
    is movie title.
    '''
    friends_watched = []

    for friend in user_data["friends"]:
        for item in friend["watched"]:
            friends_watched.append(item)
    return friends_watched