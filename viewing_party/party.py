import statistics
from statistics import mode
def create_movie(title, genre, rating):
    if title and genre and rating :
        create_movie_dict = {'title': title, 'genre': genre, 'rating': rating}
        return create_movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    #add movie into user_data dict
    #user_data has a key which is 'watched'
    #need to access the value of 'watched' which is a list of dicts 
    #and add the new dict 'movie' to that list using list function append
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #this function accomplishes the exact same thing as add_to_watched function
    #but for a different key, 'watchlist'
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    #need to compare 'title' with the value of 'watchlist' key
    #'watchlist' value is a list of dictionaries
    #access 'watchlist' value, iterate through each dictionary 
    #and compare that dict 'title' value with 'title' string
    for dictionary in user_data['watchlist']:
    #dictionary is the iterating value
        if dictionary['title']== title:
    #need to return the index of the dict if it meets the condition
    #so can use that index for the pop function. use index() function
            dict_index = user_data['watchlist'].index(dictionary)
    #now use .pop method and index of list to remove the correct dict
    #pop will store the value in memory so it can be added to 'watched'
            user_data['watchlist'].pop(dict_index)
            user_data['watched'].append(dictionary)
            
        else:
            pass
    return user_data

def get_watched_avg_rating(user_data):
#need to access each rating value in each dictionary in the list
    avg_rating = []
    for dictionary in user_data['watched']:
#append the value of each 'rating' key (which is a float) to avg_rating list    
        avg_rating.append(dictionary['rating'])
#return average of the avg_rating list
    if len(avg_rating)==0:
        return 0
    else:
        return sum(avg_rating)/len(avg_rating)

def get_most_watched_genre(user_data):
    genre_list = []
    for dictionary in user_data['watched']:
        genre_list.append(dictionary['genre'])
    if len(genre_list)==0:
        return None
    else:
        return mode(genre_list)

def get_unique_watched(user_data):
    # #unique_list = []
    # sacrifical_user_data = user_data
    # for watched_dictionary in sacrifical_user_data['watched']:
    #     for friend_dictionary in sacrifical_user_data['friends']:
    #         for inner_dictionary in friend_dictionary['watched']:
    #             if watched_dictionary['title']== inner_dictionary['title']:
    #                 dict_index = sacrifical_user_data['watched'].index(watched_dictionary)
    #                 del sacrifical_user_data['watched'][dict_index]
                    
    # return sacrifical_user_data['watched']
    
    #this list will store all the movies from user (as dicts) in a list so they are more 
    #easily compared
    user_data_movie_list =[]
    for watched_dictionary in user_data['watched']:
        user_data_movie_list.append(watched_dictionary)
    #this list will store all the movies (as dicts) from the 2 inner dicts from 'friends'
    friends_watched_movie_list =[]
    for watched_dictionary in user_data['friends']:
        for inner_dictionary in watched_dictionary['watched']:
            friends_watched_movie_list.append(inner_dictionary)
    #this list will store just movies that user has watched, but friends have not
    user_unique_list = []
    for movie in user_data_movie_list:
        if movie not in friends_watched_movie_list:
            user_unique_list.append(movie)
    return user_unique_list
    
def get_friends_unique_watched(user_data): #2ND ITERATION OF THIS FUNCTION WHICH ADDRESES THE DICTS HAVING VARYING DATA STRUCTURE ISSUE
    user_data_movie_list =[]
    total_movie_dicts = []  ### ADDED DICTIONARY TO TRACK FRIENDS MOVIES (THEY HAVE THE MOST DATA)
    for watched_dictionary in user_data['watched']:
        user_data_movie_list.append(watched_dictionary['title'])    ### USER_DATA_MOVIE_LIST NOW TRACKS TITLES ONLY
#this list will store all the movies (as dicts) from the 2 inner dicts from 'friends'
    friends_watched_movie_list =[]
    for watched_dictionary in user_data['friends']:
        for inner_dictionary in watched_dictionary['watched']:
            friends_watched_movie_list.append(inner_dictionary['title'])    ### FRIENDS WATCHED MOVIE LIST NOW TRACKS TITLES ONLY
            if inner_dictionary not in total_movie_dicts:   ### HERE WE ARE ADDING ALL UNIQUE MOVIE DICTIONARIES FROM FRIENDS WATCHED TO TOTAL_MOVIE_DICTS
                total_movie_dicts.append(inner_dictionary)  ###
#this list will store just movies that friends have watched, but user has not
    user_unique_list = []
    for movie in friends_watched_movie_list:
#bc friends_movie_list is compiled from multiple friends, there may be some duplicates in the list
# need to add an additional check to make sure there are no duplicates in final unique_list
        if movie not in user_data_movie_list:    ### MOVED NOT IN USER_UNIQUE_LIST 2 LINES DOWN
            for movie_dict in total_movie_dicts:  ### LOOPING THROUGH ALL MOVIES IN THE LIST TO FIND THE CORRESPONDING DICTIONARY TO THE TITLE
                if movie_dict['title'] == movie:    ### FOUND THE TITLE
                    if movie_dict not in user_unique_list:  ### MAKE SURE THE DICTIONARY IS NOT ALREADY IN OUR UNIQUE LIST
                        user_unique_list.append(movie_dict)     ### NOW WE ADD THE DICTONARY TO THE UNIQUE LIST
    return user_unique_list

# def get_friends_unique_watched(user_data): #1ST VERSION OF FUNCTION
#     user_data_movie_list =[]
#     for watched_dictionary in user_data['watched']:
#         user_data_movie_list.append(watched_dictionary)
# #this list will store all the movies (as dicts) from the 2 inner dicts from 'friends'
#     friends_watched_movie_list =[]
#     for watched_dictionary in user_data['friends']:
#         for inner_dictionary in watched_dictionary['watched']:
#             friends_watched_movie_list.append(inner_dictionary)
# #this list will store just movies that friends have watched, but user has not
#     user_unique_list = []
#     for movie in friends_watched_movie_list:
# #bc friends_movie_list is compiled from multiple friends, there may be some duplicates in the list
# # need to add an additional check to make sure there are no duplicates in final unique_list
#         if movie not in user_data_movie_list and movie not in user_unique_list:
#             user_unique_list.append(movie)
#     return user_unique_list



    

def get_available_recs(user_data):
#call get_friends_unique-watched function to access user_unique_list
# I now have a list of dicts of the movies user wants to watch
    user_wants_to_watch_list = get_friends_unique_watched(user_data)
    print(user_wants_to_watch_list)
#need to see if host value in user_wants_to_watch_list matches and of list of strings in 'subscriptions'
# if there's a match, add dictionary to recommended_movies list
    recommended_movies = [] #recommended_movies is a list of dicts
    if len(user_wants_to_watch_list)== 0:
        return recommended_movies
    else:
        for movie_dict in user_wants_to_watch_list:
            if movie_dict['host'] in user_data['subscriptions']:
                recommended_movies.append(movie_dict)
    
        return recommended_movies

def get_new_rec_by_genre (user_data):
#need to find user's most watched genre
    
    favorite_genre_list = []    
    
    for watched_dict in user_data['watched']:
        favorite_genre_list.append(watched_dict['genre'])
    if len(favorite_genre_list)==0:
        return favorite_genre_list
#now have a list of all genres and need to compare them, use max and count method/ function to find 
#most frequent in the list
    favorite_genre = max(favorite_genre_list, key = favorite_genre_list.count)
    recommended_genre_movies = []
    #call get_friends_unique-watched function to access user_unique_list
# I now have a list of dicts of the movies user wants to watch
    user_wants_to_watch_list = get_friends_unique_watched(user_data)
    
#compare each dict's genre value with the favorite_genre string
# #if it's a match, add to list of dicts, recommended genre movies    
    for dict in user_wants_to_watch_list:
        if favorite_genre == dict['genre']:
            recommended_genre_movies.append(dict)
    return recommended_genre_movies

def get_rec_from_favorites(user_data):
#now have a list of dicts of movies friends _have_ watched    
    friends_have_watched_list = []
    for watched_dictionary in user_data['friends']:
        for inner_dictionary in watched_dictionary['watched']:
            friends_have_watched_list.append(inner_dictionary) 
    
    recommended_favorites = []
    for dict in user_data['favorites']:
        
        
        if dict not in friends_have_watched_list:
            recommended_favorites.append(dict)
    return recommended_favorites

