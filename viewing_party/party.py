# ——— WAVE 01 ———
def create_movie(title, genre, rating):
    """Returns a dictionary with three key-value pairs. Returns None for invalid data."""
    new_movie = {}

    if isinstance(title, str):
        new_movie["title"] = title
    else:
        return None
    
    if isinstance(genre, str):
        new_movie["genre"] = genre
    else:
        return None

    if isinstance(rating, int) or isinstance(rating, float):
        new_movie["rating"] = rating
    else:
        return None

    return new_movie

def add_to_watched(user_data, movie):
    """
    Adds a movie (dictionary parameter with "title", "genre", and "rating" as keys) 
    to user's list of watched movies. Returns updated user_data.
    """
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    Adds a movie (dictionary parameter with "title", "genre", and "rating" as keys) 
    to user's watchlist, a list of dictionaries representing the movies the user wants to watch.
    Returns updated user_data.
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    Checks if a movie is in the user's watchlist. If so, adds the movie to the 
    list of watched movies, and removes the movie from watchlist.
    Returns updated user_data.
    """
    user_watchlist = user_data["watchlist"]
    user_watched = user_data["watched"]

    for movie_entry in user_watchlist:
        if movie_entry["title"] == title:
            user_watched.append(movie_entry)
            user_watchlist.remove(movie_entry)
    return user_data

# ——— WAVE 02 ———
def get_watched_avg_rating(user_data):
    """Calculates and returns the average rating of the movies in user's list of watched movies."""
    ratings = 0
    user_watched = user_data["watched"]

    if user_watched == []:
        return float(0)

    else:
        for movie_entry in user_watched:
            ratings += movie_entry["rating"] 

    return(ratings / len(user_watched))

def get_most_watched_genre(user_data):
    """
    Builds a frequency dict to determine a user's most watched genre according to their
    watched list, and returns the value as a string. Does not account for ties.
    """
    genre_frequencies = {}
    user_watched = user_data["watched"]
    
    # Counts the occurrences of each genre in the user's watched list in a dictionary, where the dict keys are the genres
    for movie_entry in user_watched:
        if movie_entry["genre"] not in genre_frequencies:
            genre_frequencies[movie_entry["genre"]] = 1
        else:
            genre_frequencies[movie_entry["genre"]] += 1

    # Iterate through genre frequency dictionary to determine largest value. Uses a counter to compare genre frequencies
    current_most_watched_genre = 0
    for genre, frequency in genre_frequencies.items():
        if frequency > current_most_watched_genre:
            current_most_watched_genre = frequency
            
    for genre, frequency in genre_frequencies.items(): # this could be refactored to not use two loops… 🤠
        if frequency == current_most_watched_genre:
            return genre

# ——— WAVE 03 ———
def get_unique_watched(user_data):
    """
    Returns a list of dictionaries that represents a list of movies that are in the user's watched list, 
    but are not in any of the user's friends watched lists. The movies are unique to the user.
    """
    not_unique_titles = []
    user_watched = user_data["watched"] 
    friends_watched = user_data["friends"]

    for movie in range(len(user_watched)):
        for x in range(len(friends_watched)): 
            for item in friends_watched[x]["watched"]:
                if user_watched[movie]["title"] in item.values():
                    not_unique_titles.append(item)

    for title in user_watched:
        for movie in not_unique_titles:
            if movie in user_watched:
                user_watched.remove(movie)
    return user_watched

def get_friends_unique_watched(user_data):
    """
    Returns a list of dictionaries that represents a list of movies that are in the user's 
    friends watched list(s), but are not in the user's watched list. Friend(s) have watched movie, user has not.
    """
    friends_watched_titles = []
    user_watched = user_data["watched"] 
    friends_watched = user_data["friends"]

    # Adds every movie in each friend's watched list to friends_watched_titles list
    for x in range(len(friends_watched)): 
        for item in friends_watched[x]["watched"]:
            if item not in friends_watched_titles:  # to not duplicate a movie already added in a previous iteration
                friends_watched_titles.append(item)

    # Removes a movie found in the user's watched list from the friends_watched_titles list
    for title in user_watched:
        for movie in friends_watched_titles:
            if title["title"] in movie.values():
                friends_watched_titles.remove(movie)
    return friends_watched_titles

# ——— WAVE 04 ———
def get_available_recs(user_data):
    """
    Returns a list of dictionaries that represents a user's recommended movies. Calls the get_friends_unique_watched function
    to get movies that the user has not watched, but at least one of the user's friends has watched. Checks if each movie is 
    available in a subscription service that the user has, and only includes these movies in the returned recommendations list.
    """
    recommendations = get_friends_unique_watched(user_data)

    for i in range(len(recommendations)):
        for recommendation in recommendations:
            if recommendation["host"] not in user_data["subscriptions"]:
                recommendations.remove(recommendation)
    return recommendations

# ——— WAVE 05 ———
def get_new_rec_by_genre(user_data):
    """
    Returns a list of dictionaries that represents a user's recommended movies based on the user's most watched genre, 
    and movies of that genre that user's friend(s) have watched but the user has not. 
    """
    fave_genre = get_most_watched_genre(user_data)
    recommendations = get_friends_unique_watched(user_data)

    if len(user_data["watched"]) == 0:
        return user_data["watched"]

    for recommendation in recommendations:
        if recommendation["genre"] != fave_genre:
            recommendations.remove(recommendation)
    return recommendations 

def get_rec_from_favorites(user_data):
    """
    Returns a list of dictionaries that represents recommended movies for user based on the user's
    favorites list. Checks for and does not return any movie that is in any of the user's friends' watched list(s).
    """
    user_favs = user_data["favorites"]
    friends_watched = user_data["friends"]
    friends_watched_titles = []

    # Adds every movie in each friend's watched list to friends_watched_titles list
    for x in range(len(friends_watched)):
        for item in friends_watched[x]["watched"]:
            friends_watched_titles.append(item)
    
    # Checks if a movie from user's favorites list has been watched by any friends, 
    # and removes from user's favorites list of dictionaries if so
    for item in friends_watched_titles:
        for title, name in item.items():
            for item in user_favs:
                if item["title"] == name:
                    user_favs.remove(item)
    return user_favs