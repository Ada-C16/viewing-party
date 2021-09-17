#  WAVE 1 #
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else: 
        return None

def add_to_watched(user_data, movie):
    if "watched" in user_data.keys():
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = [movie]

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    
    return user_data

def watch_movie(user_data, title):

    count = 0
    
    for item in user_data["watchlist"]:
        count += 1
        if item["title"] == title:
            watched_movie = user_data["watchlist"][count-1]
            user_data["watchlist"].remove(watched_movie)
            user_data["watched"].append(watched_movie)
        else: 
            pass

    return user_data

# WAVE 2 #
def get_watched_avg_rating(user_data):
    """
    calculates the avg ratings of all movies in watchlist
    if watchlist is empty, the average rating is 0.0
    """
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
    """
    check to see which value in frequency dict are highest and return the genre with the highest number
    does not account for two genres with a tie
    """
    frequency_dict = {}
    watched_list = user_data["watched"]
    for item in watched_list:
        genre_name = item["genre"]
        # item["genre"] is the specific genre name
        if genre_name not in frequency_dict:
            frequency_dict[genre_name] = 1
        else:
            frequency_dict[genre_name] += 1
    try: 
        # use 'max' function to return highest value
        # .get() is used to get the value
        most_frequent = str(max(frequency_dict, key=frequency_dict.get))
    except ValueError:
        return None
    return most_frequent

# WAVE 3 #
def get_unique_watched(user_data):
    # create an empty list to hold the movie dictionaries
    unique_user_list = []
    friend_watched_list = []

    # get list of user's watched movies
    user_watched_list = user_data["watched"]
    # get friends' watched dictionaries
    friends_watched_dict = user_data["friends"]
    
    # iterate through friend dictionaries and append each movie dict to friends_watched_list
    for friend_dict in friends_watched_dict:
        for item in friend_dict["watched"]:
            friend_watched_list.append(item)

    # compare lists
    # add dicts that are in user_watched but not friend_watched_list to unique_friend_list
    # cannot have duplicates 
    for item in user_watched_list:
        if item not in friend_watched_list:
            if item not in unique_user_list:
                unique_user_list.append(item)

    return unique_user_list

def get_friends_unique_watched(user_data):
    # create an empty list to hold the movie dictionaries
    unique_friend_list = []
    friend_watched_list = []
    user_title_list = []


    # get list of user's watched movies
    user_watched_list = user_data["watched"]

    # make a list of titles that the user has watched
    for dict in user_watched_list:
        user_title_list.append(dict["title"])

    # get friends' watched dictionaries
    friends_watched_dict = user_data["friends"]
    
    # iterate through friend dictionaries and append each movie dict to friends_watched_list
    for friend_dict in friends_watched_dict:
        for item in friend_dict["watched"]:
            friend_watched_list.append(item)

    # check to see if title in friend dict is in the user title list or alreay in the unique list
    for friend_dict in friend_watched_list:
        if friend_dict["title"] in user_title_list:
            continue 
        elif friend_dict not in unique_friend_list:
            unique_friend_list.append(friend_dict)
            
    return unique_friend_list

# WAVE 4 # 
def get_available_recs(user_data):
    unique_friend_list = get_friends_unique_watched(user_data)
    rec_list = []
    # iterate through unique_friend_list and see the host company is one of subscriptions in user_data
    # if it is, append to rec_list
    for dict in unique_friend_list:
        if dict["host"] in user_data["subscriptions"]:
            rec_list.append(dict)

    return rec_list

# WAVE 5 #
def get_new_rec_by_genre(user_data):
    # if fav_genre is = to the genre in unique friend list, append the movie dict to a list and return it
    fav_genre = get_most_watched_genre(user_data)
    # returns fav genre, which is a string
    unique_friends_watched = get_friends_unique_watched(user_data)
    # returns list of dictionaries

    # initialize a list to hold recs 
    new_rec = []

    # iterate through unique watched and see if the genre is equal to fav genre
    # if it is, add movie dict to new_rec
    for movie_dict in unique_friends_watched:
        if movie_dict["genre"] == fav_genre:
            new_rec.append(movie_dict)
    
    return new_rec

def get_rec_from_favorites(user_data):
    unique_user_list = get_unique_watched(user_data)
    # if dicts in users_unique_list are in favorites, append to recs_from_favs_list
    rec_from_fav_list = []

    for dict in unique_user_list:
        if dict in user_data["favorites"]:
            rec_from_fav_list.append(dict)

    return rec_from_fav_list