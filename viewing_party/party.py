#  WAVE 1 #

# ********************
    # PART ONE #
# ********************

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else: 
        return None


# ********************
    # PART TWO #
# ********************

def add_to_watched(user_data, movie):
    if "watched" in user_data.keys():
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = [movie]

    return user_data

# ********************
    # PART THREE #
# ********************

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    
    return user_data

# ********************
    # PART FOUR #
# ********************

def watch_movie(user_data, title):

    count = 0
    movie_watched = False
    
    for item in user_data["watchlist"]:
        count += 1
        if item["title"] == title:
            watched_movie = user_data["watchlist"][count-1]
            user_data["watchlist"].remove(watched_movie)
            user_data["watched"].append(watched_movie)
            movie_watched = True
            return user_data
        else: 
            pass

    if movie_watched == False:
        return user_data

# WAVE 2 #

def get_watched_avg_rating(user_data):
    # calculate the avg ratings of all movies in watchlist
    # if watchlist is empty, the average rating is 0.0
    # the data structure is a dictionary where the keys include "watched", etc, and the values are a list of dictionaries
    sum = 0.0
    num_of_ratings = 0
    for watched in user_data["watched"]:
        if user_data["watched"] == []:
            return 0.0
        for key, value in watched.items():
            if key == "rating":
                sum += value
                num_of_ratings += 1

    if num_of_ratings > 0:
        average = sum / num_of_ratings
        return average
    else: 
        return 0.0

def get_most_watched_genre(user_data):
    frequency_dict = {}
    watched_list = user_data["watched"]
    for item in watched_list:
        genre_name = item["genre"]
        # item["genre"] is the specific genre name
        if genre_name not in frequency_dict:
            frequency_dict[genre_name] = 1
        else:
            frequency_dict[genre_name] += 1

    # check to see which value(s) in frequency dict are highest and return the genre(s) with the highest number

    # the way I am approaching it does not account for two genres with a tie

    try: 
        most_frequent = str(max(frequency_dict, key=frequency_dict.get))
    except ValueError:
        return None
    return most_frequent

# WAVE 3 #

def get_unique_watched(user_data):
    # create an empty list to hold the movie dictionaries
    user_unique_list = []
    user_movie_set = set()
    friend_movie_set = set()

    # access movie dictionaries
    user_watched_list = user_data["watched"]
    friends_watched = user_data["friends"]


    # loop through user's movies and add them to a set
    for movie_dict in user_watched_list:
        users_movie_titles = movie_dict["title"]
        user_movie_set.add(users_movie_titles)

    # loop through friends' movies and add to set
    for friend_dict in friends_watched:
        for item in friend_dict["watched"]:
            friend_movie_titles = item["title"]
            friend_movie_set.add(friend_movie_titles)
    # difference of two sets is a new set composed of all of the elements of the first set except for any elements that overlap with the second set
    unique_user_set = user_movie_set - friend_movie_set
    
    # iterate through unique user set and add values with the key "title" to dictionary, then append dict to list
    for title in unique_user_set:
        unique_movie = {}
        unique_movie["title"] = title
        user_unique_list.append(unique_movie)
    
    return user_unique_list

def get_friends_unique_watched(user_data):
    # create an empty list to hold the movie dictionaries
    unique_friend_list = []
    user_movie_set = set()
    friend_movie_set = set()

    # access movie title names, so that you can compare them
    user_watched_list = user_data["watched"]
    friends_watched = user_data["friends"]

    # loop through user's movies and add them to a set
    for movie_dict in user_watched_list:
        users_movie_titles = movie_dict["title"]
        user_movie_set.add(users_movie_titles)

    # loop through friends' movies and add to set
    for friend_dict in friends_watched:
        for item in friend_dict["watched"]:
            friend_movie_titles = item["title"]
            friend_movie_set.add(friend_movie_titles)
    # difference of two sets is a new set composed of all of the elements of the first set except for any elements that overlap with the second set
    unique_friend_set = friend_movie_set - user_movie_set
    
    # iterate through unique friend set and add values with the key "title" to dictionary, then append dict to list
    for title in unique_friend_set:
        unique_movie = {}
        unique_movie["title"] = title
        unique_friend_list.append(unique_movie)
    
    return unique_friend_list
               

