from collections import Counter

def create_movie(movie_title, genre, rating):
    if  genre== None  or  movie_title == None or  rating ==None:
        return None
    else:
        new_movie={
        "title": movie_title,
        "genre": genre,
        "rating": rating}
        return new_movie


def search_value(user_data,movie,search_for):
    if movie not in user_data[search_for]:
        user_data[search_for] += [movie]
    return user_data


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


def get_watched_avg_rating(user_data):
    length = len(user_data["watched"])
    lista = [value for value in user_data['watched']]
    list_ratings = []
    average = 0
    for item in range(length):
        list_ratings += [lista[item]['rating']]
    if len(list_ratings) !=0:
        average =  sum(list_ratings)/ len(list_ratings)
    return average


def most_frequent(list_value):
    count = Counter(list_value)
    return count.most_common(1)[0][0]


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None 
    else:
        length = len(user_data["watched"])
        lista_watched= [value for value in user_data['watched']]
        list_genre = []
        for item in range(length):
            list_genre += [lista_watched[item]['genre']]   
        popular_genre = most_frequent(list_genre)
        return popular_genre


def get_unique_watched(user_data):
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


def get_available_recs(user_data):
    friends_list = []
    recommendations = []
    user_list = [item['title'] for item in user_data['watched']]
    host_list = user_data['subscriptions']
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_list.append(value)  
    for i in friends_list:  
        if (i['title'] not in user_list and i['host'] in host_list) and (i not in recommendations):  
            recommendations.append(i)
        elif (not user_list and i['host'] in host_list) and (i not in recommendations): 
            recommendations.append(i)
    return recommendations


def get_new_rec_by_genre(user_data):
    friends_list = []
    genre_recom = []
    user_list_genre= [item['genre'] for item in user_data['watched']] #list of dictionaries
    user_list_title = [item['title'] for item in user_data['watched']] #list of dictionaries
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_list.append(value)  
    for i in friends_list:  
        if i['title'] not in user_list_title and i['genre'] in user_list_genre: 
            if i not in genre_recom:
                genre_recom.append(i)  
    return genre_recom


def get_rec_from_favorites(user_data):
    favorites = [item['title'] for item in user_data["favorites"]]
    friends_watched = []
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_watched.append(value['title']) 
    not_watched = set(favorites).difference(set(friends_watched))
    result= [{"title":item} for item in not_watched]
    return result