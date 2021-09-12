
#make movie dictionary
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

#add movie already seen to user_data dictionary and return user_data
def add_to_watched(user_data, movie):
    #add user data to watched dictionary
    user_data["watched"].append(movie)
    
    return user_data

#add movies to user_data watchlist and return user_data
def add_to_watchlist(user_data, movie):
    #add user data to watched dictionary
    user_data["watchlist"].append(movie)
    
    return user_data

#moves movie into watched list if already seen
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

#calculates average for all movie ratings
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


#gets the most eatched genre
def get_most_watched_genre(user_data):
    #make frequency_dict table
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

