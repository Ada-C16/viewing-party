

def create_movie(movie_title, genre, rating):
    #if any  value == None return None
    if  genre== None  or  movie_title == None or  rating ==None:
        return None
    else:
        new_movie={
        "title": movie_title,
        "genre": genre,
        "rating": rating}
        return new_movie


def add_to_watched(user_data, movie):
    #check if movie in the user_data
    #if not add the data to the list
    if movie not in user_data['watched']:
        user_data["watched"] += [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    # check if movie in the user_data
    #if not add the data to the list
    if movie not in user_data['watchlist']:
        user_data["watchlist"] += [movie]
    return user_data



def watch_movie(user_data, title):
    # if title in watchlist 
    # Movie the movie object to watched
    lenght_to_iterate = len(user_data["watchlist"])
    watchlist = [elem for elem in user_data["watchlist"]]
    for item in range(lenght_to_iterate):
        if title in watchlist[item]['title']:
            del user_data['watchlist'][item]
            user_data["watched"] +=[watchlist[item]]
    return user_data         






def get_watched_avg_rating(data_dic):
    pass

def get_most_watched_genre(data_dict):
    pass

def get_unique_watched(data_dic):
    pass

def get_friends_unique_watched(data_dict):
    pass

def get_available_recs(data_dict):
    pass

def get_new_rec_by_genre(data):
    pass

def get_rec_from_favorites(data):
    pass