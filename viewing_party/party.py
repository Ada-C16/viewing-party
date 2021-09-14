import operator

# Wave 1 
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_to_watch = {
                "title" : title,
                "genre" : genre,
                "rating" : rating 
                }    
        return movie_to_watch      

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    list_of_watchlist = user_data["watchlist"]
    for movie_to_watch in list_of_watchlist:
        if movie_to_watch["title"] == title:
            add_to_watched(user_data, movie_to_watch)
            list_of_watchlist.remove(movie_to_watch)
            return user_data
    return user_data

# Wave 2 
def get_watched_avg_rating(user_data):
    sum_rating = 0 
    avg_rating = 0 
    list_of_watched = user_data["watched"]
    if list_of_watched:
        for movie_watched in list_of_watched:          
            sum_rating += movie_watched["rating"]
        avg_rating = sum_rating / len(list_of_watched)
    return avg_rating

def get_most_watched_genre(user_data):
    list_of_watched = user_data["watched"]
    if list_of_watched:
        dict_genre_to_count = {}
        for movie_watched in list_of_watched:
            movie_watched_genre = movie_watched["genre"] 
            if movie_watched_genre in dict_genre_to_count:
                dict_genre_to_count[movie_watched_genre] = dict_genre_to_count.get(movie_watched_genre) + 1
            else:
                dict_genre_to_count[movie_watched_genre] = 1

    # get the most genre 
        max_count_genre = max(dict_genre_to_count, key = dict_genre_to_count.get)
        return max_count_genre
        
    #  Alternative approach 
        # cur_most_genre = list_of_watched[0]["genre"] # this is a var to store temp value
        # count_cur_most_genre = dict_genre_to_count[cur_most_genre]
        # for key_value_genre_count in dict_genre_to_count:
        #     if key_value_genre_count.values() > count_cur_most_genre:
        #         count_cur_most_genre = key_value_genre_count.values()
        
        # # get the key
        # for key_genre in dict_genre_to_count:
        #     if dict_genre_to_count[key_genre] == count_cur_most_genre:
        #         return key_genre

        # how about if there are more than one genre with the same most count?
        

# Wave 3
def get_unique_watched(user_data):
    list_unique_movie_user_watched = []
    set_user_watched = set()
    set_friends_watched = set()

    # to add movie title in set_user_watched
    helper_func_add_movie_title_to_set(set_user_watched,user_data)

    # to add movie title in set_friends_watched
    for friends_data in user_data["friends"]:
        helper_func_add_movie_title_to_set(set_friends_watched,friends_data)

    # find the difference between sets
    set_unique_user_watched = set_user_watched - set_friends_watched

    # add unique movie into result_list 
    for unique_movie in set_unique_user_watched:
        for movie in user_data["watched"]:
            if movie["title"] == unique_movie:
                list_unique_movie_user_watched.append(movie)
    return list_unique_movie_user_watched


    # Alternative Approach 

    # list_unique_movie_user_watched = []
    
    # set_user_watched = set()
    # for movie_user_watched in user_data["watched"]:
    #     movie_userdict_value_hashable = frozendict(movie_user_watched)
    #     if movie_userdict_value_hashable not in set_user_watched:                 # put dict_value in set How to add mutable elements to set?
    #         set_user_watched.add(movie_userdict_value_hashable)

    # set_friends_watched = set()
    # for friends_data in user_data["friends"]:
    #     for movie in friends_data["watched"]:
    #         movie_friendsdict_value_hashable = frozendict(movie) 
    #         set_friends_watched.add(movie_friendsdict_value_hashable)

    # # find the difference between sets
    # set_unique_user_watched = set_user_watched - set_friends_watched
    # return list(set_unique_user_watched)


def get_friends_unique_watched(user_data):
    set_user_watched = set()
    set_friends_watched = set()
    list_unique_friends_watched = []

    for friends_data in user_data["friends"]:
        helper_func_add_movie_title_to_set(set_friends_watched,friends_data)

    helper_func_add_movie_title_to_set(set_user_watched,user_data)
    
    set_unique_friends_watched = set_friends_watched - set_user_watched

    #append dict into list 
    for unique_movie in set_unique_friends_watched:
        for friends_data in user_data["friends"]:
            for movie in friends_data["watched"]:
                if movie["title"] == unique_movie and movie not in list_unique_friends_watched:         # & ? and??
                    list_unique_friends_watched.append(movie)
    return list_unique_friends_watched



# Wave 4
def get_available_recs(user_data):
    list_recommended_movies = []
    list_unique_friends_watched = get_friends_unique_watched(user_data)

    for unique_movie in list_unique_friends_watched:
        for service_provider in user_data["subscriptions"]:
            if unique_movie["host"] == service_provider:
                list_recommended_movies.append(unique_movie)
    return list_recommended_movies


# Wave 5
def get_new_rec_by_genre(user_data):
    list_recommended_movies = []
    list_unique_friends_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)

    for unique_movie in list_unique_friends_watched:
        if unique_movie["genre"] == most_watched_genre:   # helper function possible to combine with below func?
            list_recommended_movies.append(unique_movie)
    return list_recommended_movies

def get_rec_from_favorites(user_data):
    list_recommended_movies = []                                
    list_unique_user_watched = get_unique_watched(user_data) 

    for movie in user_data["favorites"]:   
        for unique_movie in list_unique_user_watched:                
            if unique_movie == movie:                               
                list_recommended_movies.append(unique_movie)
    return list_recommended_movies                              


# helper functions 
def helper_func_add_movie_title_to_set(set_to_be_added, dict_value_movie_is_stored, ):
    for movie in dict_value_movie_is_stored["watched"]:
        set_to_be_added.add(movie["title"])


# self reference (not working)
# def helper_iterator_unique_watched_list(watched_list, comparison_obj, recommended_movies, genre=None):
#     if genre is None:
#         for unique_movie in watched_list:                
#                 if unique_movie == comparison_obj:                               
#                     recommended_movies.append(unique_movie)   
#     else:
#         for unique_movie in watched_list:                
#                 if unique_movie[genre] == comparison_obj:                               
#                     recommended_movies.append(unique_movie)   

# Audrey's version on Wave 3 for learning list comprehension 
# def get_friends_unique_watched(user_data):
#     if not user_data:
#         return None 

#     watched = user_data["watched"]
#     friends = user_data["friends"]

#     friends_movies = [movie for friend in friends for movie in friend["watched"]]
    
#     unique_friends_movies = {
#         movies['title']:movies for movies in friends_movies
#     }.values()
    
#     unique_movies = [ movie for movie in unique_friends_movies if movie not in watched]
#     return unique_movies