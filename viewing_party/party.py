# Wave 1
def create_movie(title, genre, rating):
    """
    This function returns a dictionary that gives information about a
    movie's title, genre and rating when all 3 parameters are truthy. 
    Otherwise, the function returns None.
    """
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = "Title A"
        new_movie["genre"] = "Horror"
        new_movie["rating"] = 3.5
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    """  
    The function returns a dictionary that gives information about the 
    movies that the user has watched. This function adds another 
    dictionary, movie, to the list of dictionaries in user_data. 
    """
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    The function returns a dictionary that gives information about a 
    user's watchlist. This function adds another dictionary, movie, 
    to the list of dictionaries in user_data.
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title): 
    """
    The function returns a dictionary that gives information about 
    movies that the user has watched and movies that are on the 
    user's watchlist. If the title is in the user's watchlist, 
    the function will remove the movie from the watchlist and add 
    it to the list of movies that the user has already watched. 
    Otherwise, the function will simply return user_data. 
    """
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data

# Wave 2
def get_watched_avg_rating(user_data):
    """
    The function calculates and returns the average rating from 
    a list of movies that the user has watched. The function 
    returns 0 if the user's watched list is empty.
    """
    watched_movies = user_data["watched"]
    sum = 0
    if len(watched_movies) > 0:
        for movie in watched_movies:
            sum += movie["rating"]
        avg_rating = sum/len(watched_movies)
        return avg_rating
    return 0

def get_most_watched_genre(user_data):
    """
    The function returns the genre that is most frequently watched 
    by the user from a list of movies that the user has watched. 
    The function returns None if the list of movies that the user 
    has watched is empty. 
    """
    genre_frequency = {}
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre not in genre_frequency:
            genre_frequency[genre] = 1
        else:
            genre_frequency[genre] += 1

    for genre, frequency in genre_frequency.items():
        if frequency  == max(genre_frequency.values()):
            return genre

# # Wave 3
# Helper function that will be used for waves 3-5
def get_friends_watched(user_data):
    """
    Depending on the parameter, the function returns
    different types of information about the movies that the
    user's friends have watched. 
    """
    friends_watched = []
    for watched_movies in user_data["friends"]:
        for title in watched_movies["watched"]:
            friends_watched.append(title)
    return friends_watched

def get_unique_watched(user_data):
    """
    This function returns a list of dictionaries that represents a 
    list of movies that the user has watched, but none of their 
    friends have watched. 
    """
    friends_watched = get_friends_watched(user_data)

    unique_watched = []
    for title in user_data["watched"]:
        if title not in friends_watched:
            if title not in unique_watched:
                unique_watched.append(title)
    return unique_watched

def get_friends_unique_watched(user_data):
    """
    This function returns a list of dictionaries that represents 
    a list of movies that the user's friends have watched, but the 
    user has not watched. 
    """
    friends_watched = get_friends_watched(user_data)

    friends_unique_watched = []
    for title in friends_watched:
        if title not in user_data["watched"]:
            if title not in friends_unique_watched:
                friends_unique_watched.append(title)
    return friends_unique_watched

# Wave 4
def get_available_recs(user_data):
    """
    This function returns a list of recommended movies that 
    the user has not watched but one of the user's friends has 
    watched. This list of recommended movies is only hosted by 
    a service that is in the user's subscriptions.
    """
    friends_watched = get_friends_watched(user_data)
    
    subscriptions_match = []
    for title_host in friends_watched:
        if title_host["host"] in user_data["subscriptions"]:
            if title_host not in subscriptions_match: 
                subscriptions_match.append(title_host)
    
    watched_titles_only = [movie["title"] for movie in user_data["watched"]]

    recommendations = []
    if not user_data["watched"]: 
        return subscriptions_match
    for title_host in subscriptions_match:
        if title_host["title"] not in watched_titles_only:
            recommendations.append(title_host)
    return recommendations

# Wave 5
def get_new_rec_by_genre(user_data):
    """
    This function returns a list of recommended movies that at
    least one of the user's friends has watched, but the user 
    has not watched. The list of movies also has the same genre
    as the user's most frequent genre.
    """
    recommendations = []
    if not user_data["watched"]: 
        return recommendations
    
    friends_unique_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data) 

    for movie in friends_unique_watched:
        if movie["genre"] == most_watched_genre:
            if movie not in recommendations:
                recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    """
    This function returns a list of recommended movies that 
    is in the user's favorites list. This list of movies only
    include movies that none of the user's friends have watched.
    """
    friends_watched = get_friends_watched(user_data)

    recommendations = []
    if not user_data["favorites"]:
        return recommendations
    for title in user_data["favorites"]:
        if title not in friends_watched:
            recommendations.append(title)
    return recommendations