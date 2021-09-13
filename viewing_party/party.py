#from Collections import Counter

# WAVE 1 FUNCTIONS:

# function to create new movie dictionary object
def create_movie(movie_title, genre, rating):
    if (movie_title and genre and rating):
        return { "title":movie_title, "genre":genre, "rating":rating}
    return None

# function to add movie to 'watched' movie list
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    
# function to add movie to 'watchlist'
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# function moves movies from 'watchlist' to 'watched'
def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            #remove the movie from watchlist
            user_data["watchlist"].remove(movie)
    return user_data




# WAVE 2 FUNCTIONS:

# function that returns average of 'watched' movie ratings
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]):
        my_ratings = []
        for movie in user_data["watched"]:
            my_ratings.append(movie["rating"])
        avg = sum(my_ratings) / len(my_ratings)
        return avg
    return 0.0

# function returns the most frequently watched genre

# QUESTION: AM I ALLOWED TO IMPORT COUNTER FROM COLLECTIONS?
# def get_most_watched_genre(user_data):
#     genre_frequency = []
#     for movie in user_data["watched"]:
#         genre_frequency.append(movie["genre"])
#     genre_counter = Counter(genre_frequency)
#     most_frequent_genre = max(genre_counter, key=genre_counter.get)
#     return most_frequent_genre

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    # create a new dictionary with genre and count values
    genre_frequency = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_frequency:
            genre_frequency[movie["genre"]] += 1
        else:
            genre_frequency[movie["genre"]] = 1
    most_frequent_genre = max(genre_frequency, key=genre_frequency.get)   
    return most_frequent_genre

# WAVE 3 FUNCTIONS

# get a list of watched movies unique to user (and not friend)
def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = []
    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched.append(movie)
    unique_user_movies = []
    for item in user_watched:
        if item not in friends_watched:
            unique_user_movies.append(item)
    return unique_user_movies

# get a list of unique movies watched by friends
def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = []
    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched.append(movie)
    unique_user_movies = []
    for item in friends_watched:
        if (item not in user_watched and item not in unique_user_movies):
            unique_user_movies.append(item)
    return unique_user_movies


# WAVE 4 FUNCTIONS

# function that returns recommendations from friends based on available subs
def get_available_recs(user_data):
    subscriptions = user_data["subscriptions"]
    recommendations = [] 
    watched = []
    for item in user_data["watched"]:
        watched.append(item['title'])
    for item in user_data["friends"]:
        for movie in item["watched"]:
            if (movie["host"] in subscriptions and 
                movie not in recommendations and 
                movie["title"] not in watched):
                    recommendations.append(movie)
    return recommendations


# WAVE 5 FUNCTIONS

# function that returns recommendations based on fave genre and friends' viewing
def get_new_rec_by_genre(user_data):
# it seems like I will return recommendations of what friends watched \
#    but only in the user's favorite genre
    genre = get_most_watched_genre(user_data)
    user_watched = user_data["watched"] # list of dictionaries
    friends_watched = [] # make a list of dictionaries of friends' data
    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched.append(movie)
    recommendations = []
    for item in friends_watched:
        if (item not in user_watched and item not in recommendations and
            item["genre"] == genre):
                recommendations.append(item)
    return recommendations

# function that gives a recommendation from user's favorites that friends \
#       haven't already seen
def get_rec_from_favorites(user_data):
    user_favorites = user_data["favorites"] # list of dictionaries, optional variable
    friends_watched = [] # make a list of dictionaries of friends' data
    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched.append(movie)
    recommendations = []
    for item in user_favorites:
        if (item not in recommendations and item not in friends_watched):
            recommendations.append(item)
    return recommendations





    