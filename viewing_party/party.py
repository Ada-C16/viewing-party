# Wave 1
# -------------------

# first 4 tests
def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title 
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return None

# two tests
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

# two tests
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# three tests
def watch_movie(user_data, title):
# If the title is in a movie in the user's watchlist:
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
        
            # remove that movie from the watchlist
            user_data["watchlist"].remove(movie)
            # add that movie to watched
            user_data = add_to_watched(user_data, movie)
            # return the user_data
    # If the title is not a movie in the user's watchlist:
    # return the user_data
    return user_data

# WAVE 2

# two tests
def get_watched_avg_rating(user_data):
# Calculate the average rating of all movies in the watched list

    if user_data["watched"]:
        rating_values = 0.0
        for movie in user_data["watched"]:
            
            rating_values += movie["rating"]

        
        num_movies = len(user_data["watched"])
        average_rating = rating_values / num_movies
        return average_rating

# The average rating of an empty watched list is 0.0
    else:
        return 0.0

# three tests
def get_most_watched_genre(user_data):
# Determine which genre is most frequently occurring in the watched list
# return the genre that is the most frequently watched
    if user_data["watched"]:
        genre_list = []
        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])

        genre_dict = {}
        for genre in genre_list:
            genre_dict[genre] = genre_list.count(genre)

        popular_genre = ""
        max_frequency = 0
        for genre, frequency in genre_dict.items():
            if frequency > max_frequency:
                popular_genre = genre
                max_frequency = frequency
    else:
        popular_genre = None

    return popular_genre

# WAVE 3

# two tests
def get_unique_watched(user_data):
# Consider the movies that the user has watched, and consider 
# the movies that their friends have watched. Determine 
# which movies the user has watched, but none of their friends have watched.
# Return a list of dictionaries, that represents a list of movies

    friends_unique_movies = []
    friends_watched_list = [] 

    for friend in user_data["friends"]:
        friends_watched_list += friend["watched"]

    for user_movie in user_data["watched"]:
        if user_movie not in friends_watched_list:
            friends_unique_movies.append(user_movie)

    return friends_unique_movies

# three tests
def get_friends_unique_watched(user_data):

# Determine which movies at least one of the user's friends 
# have watched, but the user has not watched.
# Return a list of dictionaries, that represents a list 
# of movies
    friends_unique_movies = []
    friends_watched_list = [] 
    
    for friend in user_data["friends"]:
        friends_watched_list += friend["watched"]

    # compare friend list to user list and append those not in user list to new list

    for friend_movie in friends_watched_list:
        if friend_movie not in friends_unique_movies:
            if friend_movie not in user_data["watched"]:
                friends_unique_movies.append(friend_movie)
    
    return friends_unique_movies

# WAVE 4

# four tests
def get_available_recs(user_data):
# Determine a list of recommended movies. A movie should be added 
# to this list if and only if:

# The user has not watched it
# At least one of the user's friends has watched
# The "host" of the movie is a service that is in the user's 
# "subscriptions"
# Return the list of recommended movies 

    recommendations = []
    friends_watched_list = get_friends_watched_list_no_duplicates(user_data["friends"])
    
    user_watched_movie_title = []
    for user_movie in user_data["watched"]:
        user_watched_movie_title.append(user_movie["title"])
    
    for friend_movie in friends_watched_list:
        if friend_movie["host"] in user_data["subscriptions"]:
            if user_data["watched"]:
                if friend_movie["title"] not in user_watched_movie_title:
                        recommendations.append(friend_movie)
            else:
                recommendations.append(friend_movie) 

    return recommendations

# WAVE 5

# four tests
def get_friends_watched_list_no_duplicates(friends_list):
    friends_watched_list = []
    for friend in friends_list:
        for friend_movie in friend["watched"]:
            if friend_movie not in friends_watched_list:
                friends_watched_list.append(friend_movie)
    return friends_watched_list

def get_new_rec_by_genre(user_data):
# Consider the user's most frequently watched genre. 
# Then, determine a list of recommended movies. 
# A movie should be added to this list if and only if:

# The user has not watched it
# At least one of the user's friends has watched
# The "genre" of the movie is the same as the user's most frequent genre
# Return the list of recommended movies

    recommendations = []
    
    genre_list = []
    for user_movie in user_data["watched"]:
        genre_list.append(user_movie["genre"]) 

    user_genre_dict = {}
    for genre in genre_list:
        user_genre_dict[genre] = genre_list.count(genre)

    user_frequent_genre = ""
    max_frequency = 0
    for genre, genre_frequency in user_genre_dict.items():
        if genre_frequency > max_frequency:
            user_frequent_genre = genre
            max_frequency = genre_frequency

    friends_watched_list = get_friends_watched_list_no_duplicates(user_data["friends"])

    for friend_movie in friends_watched_list:
        if friend_movie not in user_data["watched"] and friend_movie["genre"] == user_frequent_genre:
            recommendations.append(friend_movie)
            
    return recommendations

# two tests
def get_rec_from_favorites(user_data):
# Then, determine a list of recommended movies. 
# A movie should be added to this list if and only if:

# The movie is in the user's "favorites"
# None of the user's friends have watched it
# Return the list of recommended movies  

    recommendations = []
    friends_watched_list = get_friends_watched_list_no_duplicates(user_data["friends"])

    for fav_movie in user_data["favorites"]:
        if fav_movie not in friends_watched_list:
            recommendations.append(fav_movie)

    return recommendations

