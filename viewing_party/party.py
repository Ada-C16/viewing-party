from collections import Counter #for most watched genre

def create_movie(title, genre, rating):
    #if these three attributes are truthy, return a dictionary
    #dict should have 3 key value pairs
    #keys: title, genre, rating
    #values of these should be appropriate
    #if any of the three attributes are falsy, return none

    if bool(title) == False or bool(genre) == False or bool(rating) == False :
        return None 
    else:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie

def add_to_watched(user_data, movie):
    #the value of user_data will be a dictionary with a key "watched", and a value which is 
    # a list of dictionaries representing the movies the user has watched

    #we want to add an element to the list stored in the dictionary for user_data
    #that element is movie

    #how do we refer to the list? user_data["watched"] 
    #to add something to this list we can use append()

    user_data["watched"].append(movie) 
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    #value of user_data is a dictionary with 2 keys: "watched" and "watchlist"
    #If the title is in a movie in the user's watchlist:
        #remove that movie from the watchlist
        #add that movie to watched
        #return the user_data

    #This is what I originally had: if title in user_data["watchlist"]:
        #user_data["watchlist"].remove(title)
        #user_data["watched"].append(title)
        
    for movie in user_data["watchlist"]:
        #print(movie)
        if title in movie.values():
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    
    #If the title is not a movie in the user's watchlist:
    return user_data

def get_watched_avg_rating(user_data):
    #we want to take in user data which will be a dictionary with nest list with nested dictionaries
    #outer dictionary will be the user's name and the values will be dictionaries with movie info
    #we essentialy want to add up the ratings, increment some counter variable and then divide 

    #let's get the list first
    movies = user_data["watched"]
    
    if len(movies) == 0:
        return 0
    else:
        #let's loop through the elements in the list where movie is one nested dictionary at a time
        count_movies = 0
        sum_of_ratings = 0
        for movie in movies:
            sum_of_ratings += movie["rating"]
            count_movies += 1
        
        avg_rating = sum_of_ratings/count_movies
        return avg_rating

def get_most_watched_genre(user_data):
    #starting with the list of movies
    movies = user_data["watched"]

    if len(movies) == 0:
        return None
    else:
        list_genres = []
        most_watched = ""
        
        for movie in movies:
            list_genres.append(movie["genre"])

        most_watched = Counter(list_genres).most_common(1)[0][0]

    
    return most_watched

### WAVE 3 ###
def get_unique_watched(user_data):
    #first let's get the list of movies the user has watched
    users_movies = []
    for index in range(len(user_data["watched"])):    
        users_movies.append(user_data["watched"][index]["title"])
    
    #print(users_movies)
    

    #print(user_data["friends"][0]["watched"][0]["title"])

    friends_movies = set() #looping to fill this into a set

    friends = user_data["friends"]
    for friend in range(len(friends)):
        watched_list = friends[friend]["watched"]
        for movies in watched_list:
            for individual_title in movies:
                #print(movies[individual_title])
                friends_movies.add(movies[individual_title])
                
    #print(friends_movies)

    users_movies = set(users_movies)
    
    movies_only_user_watched = users_movies - friends_movies
    #print(movies_only_user_watched)
    
    final_movie_list_of_dictionaries = []
    for movie in movies_only_user_watched:
        final_movie_list_of_dictionaries.append({"title": movie}) 
    
    return final_movie_list_of_dictionaries

def get_friends_unique_watched(user_data):
    #first, let's get the list of movies the user has watched
    users_movies = []
    for index in range(len(user_data["watched"])):    
        users_movies.append(user_data["watched"][index]["title"])

    #next, let's get the set of movies the friends have watched
    friends_movies = set()

    friends = user_data["friends"]
    for friend in range(len(friends)):
        watched_list = friends[friend]["watched"]
        for movies in watched_list:
            for individual_title in movies:
                #print(movies[individual_title])
                friends_movies.add(movies[individual_title])
                
    #convert the users_movies to a set for comparison
    users_movies = set(users_movies)
    
    #find the difference
    movies_at_least_one_friend_watched = friends_movies - users_movies

    #convert to a list of dictionaries to return
    final_movie_list_of_dictionaries = []
    for movie in movies_at_least_one_friend_watched:
        final_movie_list_of_dictionaries.append({"title": movie}) 
    
    return final_movie_list_of_dictionaries

def get_available_recs(user_data):

    #Determine a list of recommended movies. 
    # A movie should be added to this list if and only if
    #The user has not watched it
    #At least one of the user's friends has watched
    #The "host" of the movie is a service that is in the user's "subscriptions"

    user_watched_list = user_data["watched"]
    user_subscriptions = user_data["subscriptions"]
    
    recommended_movies = []

    friends = user_data["friends"]
    for friend in range(len(friends)):
        watched_list = friends[friend]["watched"]
        for movie in watched_list:
            if movie["host"] in user_subscriptions and movie not in recommended_movies:
                if len(user_data['watched']) > 0:
                    count = 0
                    for title in user_data["watched"]:
                        if movie['title'] is not title['title']:
                            recommended_movies.append(movie)
                        else:
                            count += 1

                        if count == len(recommended_movies):
                            recommended_movies = []      
                
                else:
                    recommended_movies.append(movie)
    
    
    return recommended_movies

def get_new_rec_by_genre(user_data):
    #we want to get the user's most frequently watched genre (we have a function for this)

    recommended_movies = []
    friends_watched_movies = []
    users_watched_movies = user_data["watched"]

    #get user's most watched genre:
    most_watched = get_most_watched_genre(user_data)

    #get movies only the friends have watched:
    friends = user_data["friends"]
    for friend in range(len(friends)):
        watched_list = friends[friend]["watched"]
        for movies in watched_list:
            #print(movies)
            friends_watched_movies.append(movies)


    #loop through and see if the genre matches, 
    # is it a movie that is already in the recommended list? 
    # is it a movie in the users watched list?

    for movie in friends_watched_movies:
        if movie["genre"] == most_watched:
            if movie not in recommended_movies and movie not in users_watched_movies:
                recommended_movies.append(movie)

    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []
    users_favorite_movies = user_data["favorites"]
    only_user_watched_movies = get_unique_watched(user_data)
    
    for movie in users_favorite_movies:
        if movie in only_user_watched_movies:
            recommended_movies.append(movie)

    return recommended_movies