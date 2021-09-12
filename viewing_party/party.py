# Wave 1
def create_movie(title, genre, rating):
    """
    This function returns a dictionary that gives information about a
    movie's title, genre and rating when all 3 parameters are truthy. 
    Otherwise, the function returns None.
    """
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = "Title A"
        movie_dict["genre"] = "Horror"
        movie_dict["rating"] = 3.5
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    """  
    The function returns a dictionary, user_data, that gives information 
    about the movies that the user has watched. This function adds another 
    dictionary, movie, to the list of dictionaries in the user_data
    dictionary (the value paired with the key, "watched)
    """
    list_of_watched_dict = user_data["watched"]
    list_of_watched_dict.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    The function returns a dictionary, user_data, that gives information 
    about a user's watchlist. This function adds another dictionary, movie, 
    to the list of dictionaries in the user_data dictionary (the value paired 
    with the key, "watchlist")
    """
    list_of_watchlsit_dict = user_data["watchlist"]
    list_of_watchlsit_dict .append(movie)
    return user_data

def watch_movie(user_data, title): 
    """
    The function returns a dictionary, user_data, that gives information 
    about movies that the user has watched and movies that are on the 
    user's watchlist. If the title, a string, is in the user's watchlist, 
    the function will remove the movie from the watchlist and add it to 
    the list of movies that the user has already watched. Otherwise, 
    the function will simply return user_data. 
    """
    list_of_watchlist_dict = user_data["watchlist"]
    list_of_watched_dict = user_data["watched"]

    for watchlist_dict in list_of_watchlist_dict:
        if watchlist_dict["title"] == title:
            list_of_watchlist_dict.remove(watchlist_dict)
            list_of_watched_dict.append(watchlist_dict)
            return user_data
    return user_data

# Wave 2
def get_watched_avg_rating(user_data):
    """
    The function calculates and returns a float as the average rating 
    from a list of movie dictionaries that the user has watched. The 
    function returns 0.0 if the user's watched list is empty.
    """
    # Intialize empty list to later append ratings to for calculations
    ratings_list = [] 

    list_of_watched_dict = user_data["watched"]
    if len(list_of_watched_dict) > 0:
        for watched_dict in list_of_watched_dict:
            ratings_list.append(watched_dict["rating"])
        avg_rating = sum(ratings_list)/len(ratings_list)
        return avg_rating
    return 0

def get_most_watched_genre(user_data):
    """
    The function returns a string as the genre that is most frequently 
    watched from a list of movie dictionaries that the user has watched. 
    The function returns None if the user's watched list is empty. 
    """
    # Initialize empty dictionary to later track genre and frequencty
    genre_dict = {}

    # Assign key as genre and its respective value as frequency
    list_of_watched_dict = user_data["watched"]
    if len(list_of_watched_dict) > 0:
        for watched_dict in list_of_watched_dict:
            genre_key = watched_dict["genre"]
            if genre_key not in genre_dict:
                genre_dict[genre_key] = 1
            else:
                genre_dict[genre_key] += 1
    else:
        return None

    max_genre_frequency = max(genre_dict.values())

    # Loop through key-value pairs to return genre with highest frequency
    for genre, genre_frequency in genre_dict.items():
        if genre_frequency  == max_genre_frequency:
            return genre
