import statistics
from statistics import mode
def create_movie(title, genre, rating):
#this function creates a movie dict with keys and values and returns it
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
#iterate through dictionary (the iterator) in list of dicts which is the value of 
#user_data ['watched']
    for dictionary in user_data['watched']:
#access the genre key in each dict and append the value to genre_list
        genre_list.append(dictionary['genre'])
    if len(genre_list)==0:
        return None
#use mode function from stats module to find most common item in list
    else:
        return mode(genre_list)

def get_unique_watched(user_data):
    # this block of code represents one of my attempts to solve this by deleting dicts from the list
    # that didn't meet criteria, theoretically leaving a list of dicts that do meet criteria
    # it didn't work
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

def get_friends_unique_watched(user_data): #2ND ITERATION OF THIS FUNCTION WHICH ADDRESES 
#THE DICTS HAVING VARYING DATA STRUCTURE ISSUE-- some dicts have less data making an equal comparison 
#of dict to dict not possible
    user_data_movie_list =[] #a list of titles only
    total_movie_dicts = []  #this dict will have all movies from all friends, they have the most data
    for watched_dictionary in user_data['watched']:
        user_data_movie_list.append(watched_dictionary['title'])    #user_data_movie_list tracks titles only. BC of dicts having different 
# data structures, dicts cannot be compared to each other, so will need to compare titles to titles
#this list will store all the movies (as 'title' strings only) from the 2 inner dicts from 'friends'
    friends_watched_movie_list =[]
    for watched_dictionary in user_data['friends']:
        for inner_dictionary in watched_dictionary['watched']:
#friends_watched_movie_list tracks titles only
            friends_watched_movie_list.append(inner_dictionary['title'])    
#populating total_movie_dict list with friends dicts
            if inner_dictionary not in total_movie_dicts:   
                total_movie_dicts.append(inner_dictionary)  
#this list will store just movies that friends have watched, but user has not
    user_unique_list = []
    for movie in friends_watched_movie_list:
#bc friends_movie_list is compiled from multiple friends, there may be some duplicates in the list
# need to add an additional check to make sure there are no duplicates in final unique_list
        if movie not in user_data_movie_list:   #checking the list of title strings
            for movie_dict in total_movie_dicts:  #checking all movies to find the corresponding dict to the title
                if movie_dict['title'] == movie:    #comparing value of dict 'title' key (which is a string) to the title string from 
#friends_watched_movie_list, which is a list of strings only.  Find a match which is how to access the whole dict, and not just the title string
                    if movie_dict not in user_unique_list:  #make sure dict is not already in unique list
                        user_unique_list.append(movie_dict)     #add dict to user_unique list
    return user_unique_list #repair exploded brain and weep for the 12 hours it took to solve this

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
#now have a list of dicts of the movies user wants to watch
    user_wants_to_watch_list = get_friends_unique_watched(user_data)

    recommended_movies = [] #recommended_movies is a list of dicts
#this is a check to return an empty list if given an empty list
    if len(user_wants_to_watch_list)== 0:
        return recommended_movies
#need to see if host value in user_wants_to_watch_list matches any of list of strings in 'subscriptions'
#if there's a match, add dictionary to recommended_movies list
    else:
        for movie_dict in user_wants_to_watch_list:
            if movie_dict['host'] in user_data['subscriptions']:
                recommended_movies.append(movie_dict)
    
        return recommended_movies

def get_new_rec_by_genre (user_data):
#need to find user's most watched genre
    
    favorite_genre_list = [] #will be a list of strings, representing genres   
    
    for watched_dict in user_data['watched']:
        favorite_genre_list.append(watched_dict['genre'])
#this is a check to return an empty list if given an empty list
    if len(favorite_genre_list)==0:
        return favorite_genre_list
#now have a list of all genres and need to compare them, use max and count method/ function to find 
#most frequent in the list, could also use mode here but I wanted to try a different method
    favorite_genre = max(favorite_genre_list, key = favorite_genre_list.count) #this is now a single string, representing favorite_genre
    recommended_genre_movies = []
#call get_friends_unique-watched function to access user_unique_list
#now have a list of dicts of the movies user wants to watch
    user_wants_to_watch_list = get_friends_unique_watched(user_data)
    
#compare each dict's genre value with the favorite_genre string
#if it's a match, add to list of dicts, recommended genre movies    
    for dict in user_wants_to_watch_list:
        if favorite_genre == dict['genre']:
            recommended_genre_movies.append(dict)
    return recommended_genre_movies

def get_rec_from_favorites(user_data):
#now have a list of dicts of movies friends _have_ watched    
    friends_have_watched_list = [] #this will be a list of dicts
#adding all dicts from friends to list
    for watched_dictionary in user_data['friends']:
        for inner_dictionary in watched_dictionary['watched']:
            friends_have_watched_list.append(inner_dictionary) 
    recommended_favorites = []
    for dict in user_data['favorites']: #accessing the dicts in 'favorites"
#comparing those dicts to friends_watched_list, by loooking for if it IS NOT already in the list
# if not in the list, then friend hasn't watched user's favorite movie
# add to recommended_favorites, which will be a list of dicts        
        if dict not in friends_have_watched_list:
            recommended_favorites.append(dict)
    return recommended_favorites #set off some fireworks and pop some champagne cuz we DONE!!!

