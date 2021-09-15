
######################################################
                # Wave 1 #
######################################################

#makes movie dictionary and returns it
def create_movie(movie_title, genre, rating):
    #initialize variables
    movie_dict = {}

    #check if movie title, genre and rating are string/float variables
    #returns movie_dict or None
    if type(movie_title) == str and type(genre) == str and type(rating) == float:
        movie_dict['title'] = movie_title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
    else:
        return None
    return movie_dict

#add movie already seen to user_data dictionary and returns user_data
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

#add movies to user_data watchlist and returns user_data
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

#modifies watched and watchlist lists if movie is watched
#and returns user_data list
def watch_movie(user_data, title):
    #loop through each movie in watchlist
    #if movie title is same as given title, add movie to watched
    #remove movie from watchlist
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
    return user_data

######################################################
                # Wave 2 #
######################################################

#calculates average for all movie ratings and returns average rating
def get_watched_avg_rating(user_data):
    #initliaze list
    rating_list = []
    
    #check if watched list has at least one movie
    #loop through each movie in watched list and get rating
    #calculates avg rating or return 0 if no movies are in list
    if len(user_data['watched']) >= 1:
        for movies in user_data['watched']:
            rating_list.append(movies['rating'])
        avg_rating = sum(rating_list)/len(rating_list)
    else:
        avg_rating = 0
    
    return avg_rating


#returns the most watched genre
def get_most_watched_genre(user_data):
    #call make_genre_frequency_dict and store frequency dict in genre_frequency
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

    #loop through movies in watched list and checks if movie genre is key
    #add 1 to value in dict if genre is key
    #add genre to freq_dict if not in freq_dict
    for movies in user_data['watched']:
        if movies['genre'] in genre_frequency.keys():
            genre_frequency[movies['genre']] += 1
        else:
            genre_frequency[movies['genre']] = 1
    
    return genre_frequency

######################################################
                # Wave 3 #
######################################################

#returns list of dictionary that user has seen that none of their friends have seen
def get_unique_watched(user_data):
    #initalize variables
    user_unqiue_movie_watched = []

    #call set-making functions and capture return in assigned var
    my_movie_set = make_my_movie_set(user_data) 
    friend_movie_set = make_friend_movie_set(user_data)
    #convert difference set to tuple to iterate and make new dictionary
    movie_titles_unqiue = tuple(my_movie_set - friend_movie_set)

    #loop through each title in movies_title_unquie tuple and add title
    #dictionary to unser_unique_movie_watched list
    for title in movie_titles_unqiue:
        user_unqiue_movie_watched.append({'title': title})

    return user_unqiue_movie_watched

#take movies from user and return set of movie titles from user list
def make_my_movie_set(user_data):
    #intialize variable
    user_movie_set = set()

    #for each movie in watched list, add only movie title to user_set set
    for my_movies in user_data['watched']:
        user_movie_set.add(my_movies['title'])
    
    return user_movie_set

#takes nested friend dictionary list and returns set of movie titles from friend list
def make_friend_movie_set(user_data):
    #intialize variables
    friend_movie_set = set()
    friend_list = user_data['friends']

    #iterating thru each friend's movie dictionary list
    #set friend_movie_list to hold the dictionary of of movies watched from friends
    for friend_num in range(len(friend_list)):
        friend_movie_list = friend_list[friend_num]['watched']
        #for each movie in friend_movie_list, add movie title to friend_movie_set
        for movie in friend_movie_list:
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
    
    #add title to unique_movie_watched list
    for title in movie_titles_unqiue:
        friend_unqiue_movie_watched.append({'title': title})

    return friend_unqiue_movie_watched

######################################################
                # Wave 4 #
######################################################

#takes user_data and returns a list of reccomended movies referencing
#friend's movie watched list and user subscription
def get_available_recs(user_data):
    #intialize variables
    rec_list = []
    movie_title_user = []

    #add movie title to movie_title_user list
    for movie_user in user_data['watched']:
        movie_title_user.append(movie_user['title'])

    #access friend key in dict for friend list
    for friend in user_data['friends']:
        friend_movies_watched_list = friend['watched']

        #make boolean list from friend watched list
        for movie_item in friend_movies_watched_list:
            user_has_seen_movie = movie_item['title'] in movie_title_user
            user_has_subscription = movie_item['host'] in user_data['subscriptions']

            if not user_has_seen_movie and user_has_subscription and movie_item not in rec_list:
                rec_list.append(movie_item)

    return rec_list


######################################################
                # Wave 5 #
######################################################

#make recommendation list of movies dictionaries by genre and
#friend's watched list
def get_new_rec_by_genre(user_data):
    #intialize variables
    rec_list = []

    #call get_most_watched_grenre function and return 
    user_most_watched_genre = get_most_watched_genre(user_data)

    #call get_friends_unique_watched and returns dictionary of movie titles that
    #friends have seen but user has not seen
    movies_friend_watched = get_friends_unique_watched(user_data)
    
    #add genre to movies_friend_watched list and..
    for movies in movies_friend_watched:
        for friend in user_data['friends']:
            friend_movies_watched_list = friend['watched']
    
            for movie_item in friend_movies_watched_list:
                if movies['title'] == movie_item['title']:
                    movies['genre'] = movie_item['genre']
                
                #checks if genre is user's most watched genre and adds to rec_list
                if user_most_watched_genre == movie_item['genre'] and movie_item not in rec_list:
                    rec_list.append(movie_item)

    return rec_list

#helper function turns tuple into set with a dict
def make_tuple_return_set(given_dict):
    movie_tuple = tuple()
    for movie_item in given_dict:
        movie_tuple += tuple(movie_item.items())
    return set(movie_tuple)

#make reccomendation list from favorites list and friend's watched list
def get_rec_from_favorites(user_data):
    #initialize variables
    rec_list = []

    fav_movies_set = make_tuple_return_set(user_data['favorites'])
    
    movies_friend_not_watched = get_unique_watched(user_data)
    movies_friend_not_watched_set = make_tuple_return_set(movies_friend_not_watched)

    #get movies in both fav_movies_set and movies_friend_not_watched_set
    movies_rec_tuple = tuple(fav_movies_set & movies_friend_not_watched_set)
    
    #check if any movies were returned and append to rec list
    if len(movies_rec_tuple) > 0:
        rec_list.append(dict(movies_rec_tuple))

    return rec_list