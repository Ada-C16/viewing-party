################ WAVE 1 ##############

#wave 1, part 1

def create_movie(title, genre, rating):
    """Takes 3 values, returns a dictionary."""

    if ((bool(title) is True) and \
        (bool(genre) is True) and \
        (bool(rating) is True)):
            movie_dict = {
                "title" : title,
                "genre" : genre,
                "rating" : rating
            }
            return movie_dict
    else:
        return None

  
#wave 1, part 2

def add_to_watched(user_data, movie):
    """Takes dict, adds it to list. Returns list."""

    user_data["watched"].append(movie) 
    return user_data


#wave 1, part 3

def add_to_watchlist(user_data, movie):
    """Takes dict, adds it to list. Returns list."""

    user_data["watchlist"].append(movie)
    return user_data


#wave 1, part 4
def watch_movie(user_data, title):
    """Moves title from watchedlist to watched if in watchedlist.
    Returns dict."""

    for movie_list in user_data["watchlist"]:
            if title in movie_list["title"]:
                user_data["watched"].append(movie_list)
                user_data["watchlist"].remove(movie_list)

    return user_data





################ WAVE 2 ##############


#wave 2, part 1
def get_watched_avg_rating(user_data):
    """Calculates avd movie rating and returns."""

    rating_sum = 0.0
    rating_avg = 0.0
    
    if len(user_data["watched"]) == 0:
        return rating_avg

    for movie_dict in user_data["watched"]:
        rating_sum += movie_dict["rating"]

    rating_avg = rating_sum / (len(user_data["watched"]))
    return rating_avg


#wave 2, part 2
def get_most_watched_genre(user_data):
    """Decides most popular genre from watched list. Returns string."""

    genre_list = []
    fantasy_count = 0
    action_count = 0
    intrigue_count = 0

    if len(user_data["watched"]) == 0:
        return None

    for movie_dict in user_data["watched"]:
        genre_list.append(movie_dict["genre"])

    fantasy_count = genre_list.count("Fantasy")
    action_count = genre_list.count("Action")
    intrigue_count = genre_list.count("Intrigue")

    if (fantasy_count > action_count) and (fantasy_count > intrigue_count):
        return "Fantasy"
    elif (action_count > fantasy_count) and (action_count > intrigue_count):
        return "Action"
    else: 
        return "Intrigue"








################ WAVE 3 ##############

#wave 3, part 1
def get_unique_watched(user_data):
    """Takes dict, returns list of dicts that only user has seen."""
    
    only_user_watched = []
    user_watched_set = set()
    friends_watched_set = set()
    only_user_watched_set = set()

    for movie_user_watched in user_data["watched"]:
        user_watched_set.add(movie_user_watched["title"])
        for friends_watched_lists in user_data["friends"]:
            for movies_friends_watched_list in friends_watched_lists.values():
                for indiv_dict in movies_friends_watched_list:
                    friends_watched_set.add(indiv_dict["title"])

    only_user_watched_set = user_watched_set.difference(friends_watched_set)

    for item in only_user_watched_set:
        only_user_watched.append({"title" : item})

    return only_user_watched
                    
    

#wave 3, part 2
def get_friends_unique_watched(user_data):
    """Takes dict, returns list of dicts that only friends have seen."""

    user_watched_set = set()
    friends_watched_set = set()
    only_friends_watched_set = set()
    only_friends_watched = []

    for movie_user_watched in user_data["watched"]:
        user_watched_set.add(movie_user_watched["title"])
        
    for friends_watched_lists in user_data["friends"]:
        for movies_friends_watched_list in friends_watched_lists.values():
            for indiv_dict in movies_friends_watched_list:
                friends_watched_set.add(indiv_dict["title"])

    only_friends_watched_set = friends_watched_set.difference(user_watched_set)

    for item in only_friends_watched_set:
        only_friends_watched.append({"title" : item})

    return only_friends_watched




################ WAVE 4 ##############

def get_available_recs(user_data):
    """Takes dict, returns list of movie recommendations."""

    friends_watched_list = get_friends_unique_watched(user_data)
    friends_watched_list_titles = []
    rec_list = []
    
    for item in friends_watched_list:
        friends_watched_list_titles.append(item["title"])

    for watched_lists in user_data["friends"]:
        for watched_dict in watched_lists["watched"]:
            if (watched_dict["host"] in user_data["subscriptions"]) \
                and (watched_dict not in rec_list) \
                and (watched_dict["title"] in friends_watched_list_titles):
                    rec_list.append(watched_dict)
    
    return rec_list





################ WAVE 5 ##############

#wave 5, part 1
def get_new_rec_by_genre(user_data):
    """Takes dict, returns list of recs that match most pop genre."""

    recs_by_genre_list = []
    fav_genre = get_most_watched_genre(user_data)
   
    for items in user_data["friends"]:
        for movie_dict in items["watched"]:
            if ((movie_dict["title"] not in user_data["watched"]) \
            and (movie_dict["genre"] == fav_genre) \
            and (movie_dict not in recs_by_genre_list)):
                recs_by_genre_list.append(movie_dict)

    return recs_by_genre_list


#wave 5, part 2
def get_rec_from_favorites(user_data):
    """Takes dict, returns list of recommendations."""
  
    movie_recs = []
    friends_watched_set = set()
  
    for friends_watched_lists in user_data["friends"]:
        for movies_friends_watched_list in friends_watched_lists.values():
            for indiv_dict in movies_friends_watched_list:
                friends_watched_set.add(indiv_dict["title"])
    
    for movie in user_data["favorites"]:
        if movie["title"] not in friends_watched_set:
            movie_recs.append(movie)
    
    return movie_recs






        


    











