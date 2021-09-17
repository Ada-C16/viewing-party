from collections import Counter

'''
    wave 1 
'''
def create_movie(movie_title, genre, rating):
    if  genre== None  or  movie_title == None or  rating ==None:
        return None
    else:
        new_movie={
        "title": movie_title,
        "genre": genre,
        "rating": rating}
        return new_movie


def add_to_watched(user_data, movie):
    search_for = 'watched'
    return search_value(user_data, movie, search_for)


def add_to_watchlist(user_data, movie):
    search_for = 'watchlist'
    return search_value(user_data, movie, search_for)


def watch_movie(user_data, title):
    length = len(user_data["watchlist"])
    watchlist = [elem for elem in user_data["watchlist"]]
    for item in range(length):
        if title in watchlist[item]['title']:
            del user_data['watchlist'][item]
            user_data["watched"] +=[watchlist[item]]
    return user_data         

'''
    wave 2
'''


def get_watched_avg_rating(user_data):
    average_result = 0
    outer_key = "watched"
    inner_key = "rating"
    list_ratings =  get_dict_value(user_data, outer_key, inner_key)
    if list_ratings:
        average_result =  average(list_ratings)
    return average_result


def get_most_watched_genre(user_data):
    popular_genre = None
    if user_data["watched"]: 
        outer_key = "watched"
        inner_key = "genre"
        list_genre = get_dict_value(user_data, outer_key, inner_key)
        popular_genre = most_frequent(list_genre)
    return popular_genre

'''
    wave 3
'''

def get_unique_watched(user_data):
    user_watched_list = []
    friends_watched_list =[]
    create_user_watched_list(user_data, user_watched_list)
    create_friends_watched_list(user_data,friends_watched_list)  
    unique_in_user = set(user_watched_list).difference(set(friends_watched_list))
    result =  [{"title":item} for item in unique_in_user]
    return result


def get_friends_unique_watched(user_data):
    user_watched_list = []
    friends_watched_list =[]
    create_user_watched_list(user_data, user_watched_list)
    create_friends_watched_list(user_data,friends_watched_list)  
    unique_in_friends = set(friends_watched_list).difference(set(user_watched_list))
    result =  [{"title":item} for item in unique_in_friends]
    return result

'''
    wave 4
'''

def get_available_recs(user_data):
    friends_list = []
    recommendations = []
    user_list = [item['title'] for item in user_data['watched']]
    host_list = user_data['subscriptions']
    create_friends_list(user_data,friends_list) 
    for i in friends_list:  
        if (i['title'] not in user_list and i['host'] in host_list) and (i not in recommendations):  
            recommendations.append(i)
        elif (not user_list and i['host'] in host_list) and (i not in recommendations): 
            recommendations.append(i)
    return recommendations

'''
    wave 5
'''


def get_new_rec_by_genre(user_data):
    friends_list = []
    genre_recom = []
    user_list_genre= [item['genre'] for item in user_data['watched']] #list of dictionaries
    user_list_title = [item['title'] for item in user_data['watched']] #list of dictionaries  
    create_friends_list(user_data,friends_list)
    for i in friends_list:  
        if i['title'] not in user_list_title and i['genre'] in user_list_genre: 
            if i not in genre_recom:
                genre_recom.append(i)  
    return genre_recom


def get_rec_from_favorites(user_data):
    favorites = [item['title'] for item in user_data["favorites"]]
    friends_list = [] 
    create_friends_watched_list(user_data,friends_list)     
    not_watched = set(favorites).difference(set(friends_list))
    result= [{"title":item} for item in not_watched]
    return result

''' 
    helper functions
'''
def search_value(user_data,movie,search_for):
    if movie not in user_data[search_for]:
        user_data[search_for] += [movie]
    return user_data


def most_frequent(list_value):
    count = Counter(list_value)
    return count.most_common(1)[0][0]


def create_friends_list(user_data,friends_list):
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_list.append(value) 
    return friends_list


def create_user_watched_list(user_data, user_watched_list):
    for item  in user_data['watched']:
        user_watched_list += [item['title']]
    return user_watched_list


def create_friends_watched_list(user_data,friends_list):
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_list.append(value['title']) 
    return friends_list

def get_dict_value(user_data, user_data_key, inner_key):
    length = len(user_data[user_data_key])
    list_watched = [value for value in user_data[user_data_key]]
    list_values = []
    for item in range(length):
        list_values += [list_watched[item][inner_key]]
    return list_values

    
def average(list_number):
    return sum(list_number)/len(list_number)