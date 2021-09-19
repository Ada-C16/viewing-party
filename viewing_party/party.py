from statistics import mode
# The first four tests are going to test against this function:
def create_movie(title, genre, rating):
    """
    This function takes title, genre and ratings as keys and the input as their values. 
    """
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return None
    
# The next two tests are about this function:
def add_to_watched(user_data, movie):
    """
    Input: user data where usand movie 
    Output: 
    """
    already_watched_list = user_data["watched"]
    already_watched_list.append(movie)
    return user_data

# next two tests are about this function:
def add_to_watchlist(user_data, movie):
    """
    Adds movie dictionary info to users watchlist
    """
    to_watch = user_data["watchlist"]
    to_watch.append(movie)
    return user_data

# next three tests are about this function:
def watch_movie(user_data, title):
    """
    Compares a watchlist and watched movie collection. Once a movie is watched it is
    removed from users watchlist.
    """
    for movie in user_data["watchlist"]:
        for movie_key, movie_info in movie.items():
            if title == movie_info:
                user_data["watched"].append(movie)
                user_data["watchlist"].remove(movie)
                return user_data
    return user_data

#WAVE 2
# Two tests are for this function:
def get_watched_avg_rating(user_data):
    """
    This function calculates the average user rating from user_data input. 
    """
    list_of_ratings = []
    for rating in user_data["watched"]:
        list_of_ratings.append(rating["rating"])
    if len(list_of_ratings) == 0:
        return 0.0
    average_rating = sum(list_of_ratings)/len(list_of_ratings)
    return average_rating
    
# Three tests are for this function:
def get_most_watched_genre(user_data):
    """
    This function gathers the genres of all the watched movies from the user
    and returns the most watched genre from user. 
    """
    most_watched = user_data['watched']
    genres = []
    if len(most_watched) == 0:
        return None
    for movie in most_watched:
        genres.append(movie["genre"])

    return mode(genres)

# WAVE 3
# First two tests are for this function:
def get_unique_watched(user_data):
    """
    This function compares a list of watched movies from user and user's friends.
    The function returns movies that the user has watched but their friends have not watched. 
    """
    user_watched_movies = user_data["watched"]
    friends_watched_movies = user_data["friends"]
    
    friends_movie_titles = []
    for data in friends_watched_movies:
        for friend_titles in data["watched"]:
            friends_movie_titles.append(friend_titles["title"])

    unique_titles =[]
    for title in user_watched_movies:
        if title["title"] not in friends_movie_titles:
            unique_titles.append(title) 
    return unique_titles

# Next three tests are for this function:
def get_friends_unique_watched(user_data):
    """
    This function compares a list of watched movies from user and user's friends.
    The function returns movies that the at least one friend of the user has watched,
    but the user has not watched.  
    """
    user_watched_movies = user_data["watched"]
    friends_watched_movies = user_data["friends"]
    
    user_titles =[]       
    for title in user_watched_movies:
        user_titles.append(title) 
    
    unique_friends_movie_titles = []
    for data in friends_watched_movies:
        for friend_titles in data["watched"]:
            if friend_titles not in user_titles:
                if friend_titles not in unique_friends_movie_titles:
                    unique_friends_movie_titles.append(friend_titles)
    return unique_friends_movie_titles

    # WAVE 4
    # Next 4 tests are about this function:
def get_available_recs(user_data):
    """
    This function compares watched movies between user and user's friends.
    If the user has not watched the movie and have a subscription to the host, this function will
    return recommended movies along with the host/subscription. 
    """
    recommended_movies = [] 
    friends = user_data["friends"]
    
    # Collectd a list of titles the user has already watched to 
    # compare to friends watched later.
    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie["title"])
        
    for friend in friends:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched and movie["host"] in user_data["subscriptions"]:
                recommended_movies.append(movie)
                
    
    return recommended_movies

