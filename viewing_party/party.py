
#makes movie dictionary and returns it
def create_movie(movie_title, genre, rating):
    #initialize variables
    movie_dict = {}

    #check if movie title, genre and rating are correct
    #var types and returns movie_dict or None
    if type(movie_title) == str and type(genre) == str and type(rating) == float:
        movie_dict['title'] = movie_title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
    else:
        return None
    return movie_dict

#add movie already seen to user_data dictionary and returns user_data
def add_to_watched(user_data, movie):
    #add user data to watched dictionary
    user_data["watched"].append(movie)
    
    return user_data

#add movies to user_data watchlist and returns user_data
def add_to_watchlist(user_data, movie):
    #add user data to watched dictionary
    user_data["watchlist"].append(movie)
    
    return user_data

#modifies watched and watchlist lists if movie is watched
#and returns user_data list
def watch_movie(user_data, title):
    #iterating through movies in user watch list
    for movie in user_data['watchlist']:
        #if movie title is the same as given title
        if movie['title'] == title:
            #add movie to watched
            user_data['watched'].append(movie)
            #remove movie from watchlist
            user_data['watchlist'].remove(movie)
    return user_data

#calculates average for all movie ratings and returns average rating
def get_watched_avg_rating(user_data):
    #initliaze list
    rating_list = []
    #check if watched list has at least one movie..
    if len(user_data['watched']) >= 1:
        #for each movie in watched list...
        for movies in user_data['watched']:
            #get rating value and store in list
            rating_list.append(movies['rating'])
        #caluculate average
        avg_rating = sum(rating_list)/len(rating_list)
    #if no movies are in list, return 0 as average rating
    else:
        avg_rating = 0
    
    return avg_rating


#returns the most watched genre
def get_most_watched_genre(user_data):
    #call make_genre_frequency_dict and store return variable in genre_frequency
    genre_frequency = make_genre_frequency_dict(user_data)
    if len(genre_frequency) > 0:
        popular_genre = max(genre_frequency, key = genre_frequency.get)
        return popular_genre
    else:
        return None

#takes user data to create genre frequency and returns it
def make_genre_frequency_dict(user_data):
    #intialize variables
    genre_frequency = {}

    #for each movie in watched list...
    for movies in user_data['watched']:
        #check if movie genre is a key in genre_frequency dict
        if movies['genre'] in genre_frequency.keys():
            #add one to value if key is in genre_frequency
            genre_frequency[movies['genre']] += 1
        #add genre if not in frequency dict
        else:
            genre_frequency[movies['genre']] = 1
    
    return genre_frequency


#returns list of dictionary that user has seen that none of their friends have seen
def get_unique_watched(user_data):
    #initalize variables
    user_unqiue_movie_watched = []

    #call set-making functions and capture return in assigned var
    my_movie_set = make_my_movie_set(user_data) 
    friend_movie_set = make_friend_movie_set(user_data)
    #convert difference set to tuple to iterate and make new dictionary
    movie_titles_unqiue = tuple(my_movie_set - friend_movie_set)
    
    #iterating thru tuple list..
    for title in movie_titles_unqiue:
        #add title dictionary to unique_movie_watched list
        user_unqiue_movie_watched.append({'title': title})

    return user_unqiue_movie_watched

#take movies from user and return set of movie titles from user list
def make_my_movie_set(user_data):
    #intialize variable
    user_movie_set = set()
    #for each movie in watched list..
    for my_movies in user_data['watched']:
        #add only movie title to user_set set
        user_movie_set.add(my_movies['title'])
    
    return user_movie_set

#takes nested friend dictionary list and returns set of movie titles from friend list
def make_friend_movie_set(user_data):
    #intialize friend_set
    friend_movie_set = set()
    #set friend_list to list of friend's movie dictionary list
    friend_list = user_data['friends']
    #iterating thru each friend's movie dictionary list, 
    for friend_num in range(len(friend_list)):
        #set friend_movie_list to hold the dictionary of of movies watched from friends
        friend_movie_list = friend_list[friend_num]['watched']
        #for each movie in friend_movie_list..
        for movie in friend_movie_list:
            #add movie title to friend_movie_set
            friend_movie_set.add(movie['title'])

    return friend_movie_set

#returns list of dictionary that friends have seen that user has not seen
def get_friends_unique_watched(user_data):
    #initalize variables
    friend_unqiue_movie_watched = []

    #call set-making functions and capture return in assigned var
    my_movie_set = make_my_movie_set(user_data) 
    friend_movie_set = make_friend_movie_set(user_data)
    #convert difference set to tuple to iterate and make new dictionary
    movie_titles_unqiue = tuple(friend_movie_set - my_movie_set)
    
    #iterating thru tuple list..
    for title in movie_titles_unqiue:
        #add title dictionary to unique_movie_watched list
        friend_unqiue_movie_watched.append({'title': title})

    return friend_unqiue_movie_watched


amandas_data = {
    "subscriptions": ["Service A", "Service B"],
    "watched": [{ "title": "Title A" }],
    "friends": [
        {
            "watched": [
                {
                    "title": "Title A",
                    "host": "Service A"
                },
                {
                    "title": "Title C",
                    "host": "Service C"
                }
            ]
        },
        {
            "watched": [
                {
                    "title": "Title A",
                    "host": "Service A"
                },
                {
                    "title": "Title B",
                    "host": "Service B"
                },
                {
                    "title": "Title D",
                    "host": "Service D"
                }
            ]
        }
    ]
}

#takes user_data and returns a list of reccomended movies
def get_available_recs(user_data):
    #intialize variables
    recommended_movies_list = []
    friend_movie_list = user_data['friends']
    user_watched = user_data['watched']

    print(user_watched)

    # for friend_num in range(len(friend_movie_list)):
    #     movie_list = friend_movie_list[friend_num]['watched']
    #     for movie_num in range(len(movie_list)):
    #         if movie_list[movie_num]['title'] != 

        
print(get_available_recs(amandas_data))