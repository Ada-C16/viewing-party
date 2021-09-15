#
#Robot invasion wave 1
#
from typing import Counter
from statistics import mode

def create_movie(title,genre,rating):
    if bool(title) and bool(genre) and  bool(rating):
        movie= {"title": title, "genre":genre, "rating": rating}
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie) 
    return user_data
  
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):

    for i,dct in enumerate(user_data["watchlist"]):
        if title == dct["title"]:
                watched_movie_dct = user_data["watchlist"].pop(i)
                user_data["watched"].append(watched_movie_dct)
                return user_data
    return user_data
    
#
#Robot invasion Wave 2
#
def get_watched_avg_rating(user_data):
    sum=0
    if user_data["watched"]==[]:
        return 0
    
    for dct in user_data["watched"]:
        sum += dct["rating"]
    return sum/len(user_data["watched"])

def get_most_watched_genre(user_data):
    most_watched_lst=[]

    if user_data["watched"]==[]:
        return None
    for mvie in user_data["watched"]:
        most_watched_lst.append(mvie["genre"])
    genre_cnt = Counter(most_watched_lst)
    top_genre= genre_cnt.most_common(1)
    return top_genre[0][0]
#
# Robot invasion wave 3
# we ran out of drinks, please send taro boba tea
#
def get_unique_watched(user_data):
    listof_watched_dct=[]
    a_lst=[]
    b_lst=[]
    ab_lst=[]
    user_movie_lst=[]
    friends_movie_lst=[]
    new_movie_lst=[]
    #This for loop creates a new list with all the movies that the user watched
    for dct in user_data["watched"]:
        user_movie_lst.append(dct)

    #This for loop creates two lists of movies that friends watched
    for dct in user_data["friends"]:
        for lst in dct:
            listof_watched_dct.append(dct[lst])
    a_lst= (listof_watched_dct[0])
    b_lst= (listof_watched_dct[1])
    ab_lst= a_lst+b_lst

    for i in ab_lst:
        if i not in friends_movie_lst:
            friends_movie_lst.append(i)

    #This for loop creates a new movie list
    for i in user_movie_lst:
        if i not in friends_movie_lst:
            new_movie_lst.append(i)
    return new_movie_lst

def get_friends_unique_watched(user_data):
    listof_watched_dct=[]
    a_lst=[]
    b_lst=[]
    ab_lst=[]
    user_movie_lst=[]
    friends_movie_lst=[]
    new_movie_lst=[]
    #This for loop creates a new list with all the movies that the user watched
    for dct in user_data["watched"]:
        user_movie_lst.append(dct)

    #This for loop creates two lists of movies that friends watched
    for dct in user_data["friends"]:
        for lst in dct:
            listof_watched_dct.append(dct[lst])
    a_lst= (listof_watched_dct[0])
    b_lst= (listof_watched_dct[1])
    ab_lst= a_lst+b_lst

    for mvie in ab_lst:
        if mvie not in friends_movie_lst:
            friends_movie_lst.append(mvie)

    #This for loop creates a new movie list
    for mvie in friends_movie_lst:
        if mvie not in user_movie_lst:
            new_movie_lst.append(mvie)
    return new_movie_lst

#
# Robot invasion wave 4
# sip your tea and hold your hat, we are
# going for a wild ride
#
def get_available_recs(user_data):

    a_lst=[]
    b_lst=[]
    ab_lst=[]
    friends_data_lst=[]


#this section creates only one list of the movies that friends watched
    a_lst=user_data["friends"][0]["watched"]
    b_lst=user_data["friends"][1]["watched"]
    ab_lst=a_lst+b_lst

    for mvie in ab_lst:
        if mvie not in friends_data_lst:
            friends_data_lst.append(mvie)

    watched_lst=[]
    for mvie in user_data["watched"]:
        if mvie not in watched_lst:
            watched_lst.append(mvie)

    #This for loop iterates through the dictionaries in the super list of friends data to create a list of movies with the subscription services the user is subscribed.

    unique_mvies=[]

    for dct in friends_data_lst:
        for idx in range(0,(len(user_data["subscriptions"]))):
            if user_data["subscriptions"][idx] in dct.values():
                unique_mvies.append(dct)

    for i in watched_lst:
        title= i["title"]
        for x,dct in enumerate(unique_mvies):
            if title == dct["title"]:
                unique_mvies.pop(x)
    if unique_mvies != 0:
        return unique_mvies
    else:
        return 0
#
#
#Robot Invasion Wave 5
#We are winning
#Still thirsty
#she protec she atac but
#more importantly she snac
#
def get_new_rec_by_genre(user_data):
    watched_lst=[]
    mvie_by_genre_lst=[]
    friends_watched_lst=[]

    if len(user_data["watched"]) == 0:
        return mvie_by_genre_lst

    for dct in  user_data["friends"]:
        if [dct][0]["watched"] not in friends_watched_lst:
            friends_watched_lst.append([dct][0]["watched"])

    for mvie in user_data["watched"]:
        watched_lst.append(mvie["genre"])

    temp = [wrd for sub in watched_lst for wrd in sub.split()]
    res=mode(temp)

    for wtcd,dct in  enumerate(friends_watched_lst):
        for mvie in dct:
            if res in mvie["genre"]:
                mvie_by_genre_lst.append(mvie)
    return mvie_by_genre_lst
def get_rec_from_favorites(user_data):
    friends_watched_lst=[]
    favorites_lst=[]
    recommended_lst=[]

    if len(user_data["watched"]) == 0:
        return recommended_lst
  
    for mvie in user_data["favorites"]:
        favorites_lst.append(mvie)
    new_lst=[]
    for dct in  user_data["friends"]:
        if [dct][0]["watched"] not in new_lst:
            new_lst.append([dct][0]["watched"])

    for lst in new_lst:
        for dct in lst:
            friends_watched_lst.append(dct)

    for i in favorites_lst:
        if i  not in friends_watched_lst:
            recommended_lst.append(i)
    return recommended_lst
