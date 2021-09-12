
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