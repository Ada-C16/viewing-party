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

def get_available_recs(user_data):
    #   loop through dic and find movies that friends have watched and Amanda did not!!
    #   The movies need to be supportted by the user's subscription - 
    #   if 'host' not in user subscription do not recommend movie
    #   return a dictionary with recommended movie and host(provider)eg:. {"title": "Title A", "host": "Service A"}
    friends_list = []
    user_list = [item['title'] for item in user_data['watched']] #list of dictionaries
    host_list = user_data['subscriptions'] #list
    recommendations = []
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_list.append(value)  
    for i in friends_list:  
        if i['title'] not in user_list and i['host'] in host_list:  
            if  i not in recommendations:
                recommendations.append(i)
        elif user_list == [] and i['host'] in host_list:
            if i not in recommendations:
                recommendations.append(i)
    return recommendations


def get_new_rec_by_genre(user_data):
    # Recommend movies based on the genre 
    #if friends have watched movies that are the same genre that user likes(has movies watched) - recommend the movie
        #if user haven't seen the movie yet
    friends_list = [] #list od dic
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
# return value from favorites that friends have not watched yet
# loop through friends movies title and store in list
# store favorites in a list
#create a variable  to store the result
    favorites = [item['title'] for item in user_data["favorites"]]
    friends_watched = []
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_watched.append(value['title']) 
    not_watched = set(favorites).difference(set(friends_watched))
    result= [{"title":item} for item in not_watched]
    return result