def create_movie(movie_title, genre, rating):
    """
    This function appends movie medadata to a new movie dictionary, metadata needs to be complete
    in order to return the value
    """
    new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }
    for value in new_movie.values():
        if value == None:
            return None
    return new_movie

def add_to_watched(user_data, movie):
    """
    This function ammends the user_data "watched" key with new movie information
    """
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    This function ammends the user_data "watchlist" key with new movie information
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    This function takes a movie title, reviews user_data "watchlist", if movie matches a title in watchlist
    the function will move movie to "watched" and remove from "watchlist"
    """
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in watchlist:
        if movie["title"] == title:
            watched.append(movie)
            watchlist.remove(movie)
    return user_data

def get_watched_avg_rating(user_data):
    """
    This function will return the average rating for a "watched" movies in user_data, 
    will return 0.0 if nothing contained in "watchlist"
    """
    sum_rating = 0
    average_rating = 0.0
    watched = user_data["watched"]
    if len(watched) == 0:
        return average_rating
    else:
        for movie in watched:
            sum_rating += movie["rating"]
            average_rating = sum_rating / len(watched)
    return average_rating

def get_most_watched_genre(user_data):
    """
    This function will return the most watched genre in user_data "watched" data.
    """
    genre_dict = {}
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie in user_data["watched"]:
            if movie["genre"] not in genre_dict:
                genre_dict[movie["genre"]] = 1
            else:
                genre_dict[movie["genre"]] += 1
        popular_genre = max(genre_dict, key=genre_dict.get)
        return popular_genre
    # max_freq = 0
    # max_genre = None
    # for genre, freq in genre_dict.items():
    #     if freq > max_freq:
    #         max_freq = freq
    #         max_genre = genre
    # I commmented this section out because I used max(, key.get) first, but I don't know if I fully understand it

def get_unique_watched(user_data):
    """
    Given a user_data "watched", this function will compare to friend's "watched" data and return
    unique values of user_data
    """
    user_watched = user_data["watched"]
    unique_watched = []
    for movie_title in user_watched:
        if movie_title not in merge_friend_watch_lists(user_data):
            unique_watched.append(movie_title)
    return(unique_watched)

def merge_friend_watch_lists(user_data):
    """
    This function combines multiple values of user_data friend's "watched" movies into a master list
    """
    friend_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_watched:
                friend_watched.append(movie)
    return friend_watched

def get_friends_unique_watched(user_data):
    """
    Given a user_data "watched", this function will compare to friend's "watched" data and return
    unique values of friend's "watched"
    """
    user_watched = user_data["watched"]
    unique_watched = []
    for movie_title in merge_friend_watch_lists(user_data):
        if movie_title not in user_watched:
            unique_watched.append(movie_title)
    return(unique_watched)

def get_available_recs(user_data):
    """
    Given the friend's "watched" movies in user_data, this function will review movies not in 
    user_data "watched" for subscriptions user has, will append to recommendations list
    """
    friend_watched_list = merge_friend_watch_lists(user_data)
    subscriptions = user_data["subscriptions"]
    user_watched = create_a_list_of_only_user_data_watched_titles(user_data)
    recommendations = []
    for movie in friend_watched_list:
        if movie["title"] not in user_watched:
            if movie["host"] in subscriptions:
                recommendations.append(movie)
    return recommendations

def create_a_list_of_only_user_data_watched_titles(user_data):
    """
    This function creates a list of just movie titles from user_data "watched"
    """
    user_watched = user_data["watched"]
    user_watched_list = []
    for movie in user_watched:
        user_watched_list.append(movie["title"])
    return user_watched_list

def get_new_rec_by_genre(user_data):
    """
    This function creates a recommendation list based on unique values from
    user_data friend's "watched" movies
    """
    friend_watched_list = merge_friend_watch_lists(user_data)
    user_watched_title = create_a_list_of_only_user_data_watched_titles(user_data)
    recommendations = []
    if len(user_watched_title) == 0:
        return recommendations
    else:  
        for movie in friend_watched_list:
            if movie["title"] not in user_watched_title:
                recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    """
    This function generates a recommendation list based on unique values on user_data "watched" movies user_data
    favorite genres
    """
    friend_watched_titles = create_a_list_of_only_friend_watched_titles(user_data)
    user_favorite_title = create_a_list_of_only_user_data_favorite_titles(user_data)
    user_watched_title = user_data["watched"]
    recommendations = []
    if len(user_favorite_title) == 0:
        return recommendations
    else:  
        for movie in user_watched_title:
            if movie["title"] in user_favorite_title:
                if movie["title"] not in friend_watched_titles:
                    recommendations.append(movie)
    return recommendations

def create_a_list_of_only_friend_watched_titles(user_data):
    """
    This function creates a list of only movie titles from user_data friends "watched" movies
    """
    friend_watched = merge_friend_watch_lists(user_data)
    friend_watched_list = []
    for movie in friend_watched:
        friend_watched_list.append(movie["title"])
    return friend_watched_list

def create_a_list_of_only_user_data_favorite_titles(user_data):
    """
    This function creates a list of only movie titles from user_data "favorites"
    """
    user_watched = user_data["favorites"]
    user_watched_list = []
    for movie in user_watched:
        user_watched_list.append(movie["title"])
    return user_watched_list