from collections import Counter

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
    lenght = len(user_data["watchlist"])
    watchlist = [elem for elem in user_data["watchlist"]]
    for item in range(lenght):
        if title in watchlist[item]['title']:
            del user_data['watchlist'][item]
            user_data["watched"] +=[watchlist[item]]
    return user_data         


def get_watched_avg_rating(user_data):
    # Access all rating values and store in a list named rating_list
    # SUM all values using sum() and divide by the len(rating_list)
    lenght = len(user_data["watched"])
    lista = [value for value in user_data['watched']]
    list_ratings = []
    average = None
    for item in range(lenght):
        list_ratings += [lista[item]['rating']]

    if len(list_ratings) !=0:
        average =  sum(list_ratings)/ len(list_ratings)
    else:
        return 0.0
    return average

def most_frequent(list_value):
    count = Counter(list_value)
    return count.most_common(1)[0][0]

def get_most_watched_genre(user_data):

    if not user_data["watched"]:
        return None 
    else:
        lenght = len(user_data["watched"])
        lista_watched= [value for value in user_data['watched']]
        list_genre = []
        for item in range(lenght):
            list_genre += [lista_watched[item]['genre']]   
        popular_genre = most_frequent(list_genre)
        return popular_genre

def get_unique_watched(user_data):
    #ITERATE OVER THE DICTIONARY AND:
    #CREATE A LIST WITH AMANDA'S MOVIES
    #CREATE A LIST WITH FRIEND'S MOVIES
    # COMPARE THOSE 2 LISTS
    #USE SET ATTRIBUTES TO FIND UNIQUE VALUES FROM AMANDA'S
    #Create a IF STATEMENT IN CASE THERE NO VALUE IN WATCHED LIST -none
    user_watched_list = []
    friends_watched_list =[]
    for item  in user_data['watched']:
        user_watched_list += [item['title']]
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_watched_list += [value['title']]
    unique_in_user = set(user_watched_list).difference(set(friends_watched_list))
    result =  [{"title":item} for item in unique_in_user]
    return result

def get_friends_unique_watched(user_data):
    user_watched_list = []
    friends_watched_list =[]
    for item  in user_data['watched']:
        user_watched_list += [item['title']]
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_watched_list += [value['title']]
    unique_in_friends = set(friends_watched_list).difference(set(user_watched_list))
    result =  [{"title":item} for item in unique_in_friends]
    return result

def get_available_recs(data_dict):
    pass

def get_new_rec_by_genre(data):
    pass

def get_rec_from_favorites(data):
    pass