
#this is the function that creates a new movie
def create_movie(title, genre, rating):

    # initilialize variables
    
    movie_dict = {}

    #if these values are true, return dictionary
    if title and genre and rating: #insert how to denote truthy and falsy values
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
    else:
        return None
    
    return movie_dict


# function that that adds movie to watched list
def add_to_watched(user_data, movie):
    #add each movie in the 'watched' field of user_data
    user_data['watched'].append(movie)
    # return user-data
    return user_data


#add movie to movies to watch
def add_to_watchlist(user_data, movie):
    # user_data has a key - 'watchlist'
    # value (which is what we are going to make) is a list of dictionaries 
    # repping movies user wants to watch
    
    
    # add movie to 'watchlist' key
    user_data['watchlist'].append(movie)


    #return user_data
    return user_data



# function that adds a movie to watched if given 
def watch_movie(user_data,title):

    # if title is a movie in user's watchlist
    for movie in user_data['watchlist']:
        
        if title == movie['title']:
            
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
    
    return user_data


# wave 2
# function that takes the average rating of movies in watched
def get_watched_avg_rating(user_data):
    
    rating_sum = 0
    rating_list = []
    
    # get th ratings out of user data and put it in a list

    for movie in user_data['watched']:
        rating_sum += movie['rating']
        rating_list.append(movie['rating'])
    if len(rating_list) == 0:
        avg_rating = 0
    else:
        avg_rating =rating_sum/len(rating_list)

    
    
    return avg_rating



# gets the genre from the list of movies that was watched the most
def get_most_watched_genre(user_data):
    genre_list = []
    # user data is a dictionary w a watched list of movie dictionaries. in each element is a key genre and the value is a string
    # see which genre appears the most and return it

    # get to genres and add them to a list

    for movie in user_data['watched']:
        genre_list.append(movie['genre'])
    
    if len(user_data['watched']) == 0:
        most_watched_genre = None
    else:
        most_watched_genre = max(set(genre_list), key = genre_list.count)

    return most_watched_genre

# wave 3
# return a list of movies that the user has watched, but none of their friends have watched
def get_unique_watched(user_data):
    unique_user_watch_list = []
    user_watched_list = []
    friend_watched_list = []
    for user_movie in user_data['watched']:
        user_watched_list.append(user_movie)
    for friend in user_data['friends']:
        for friend_movie in friend['watched']:
            friend_watched_list.append(friend_movie)
    for user_movie in user_watched_list:
        if user_movie not in friend_watched_list:
            unique_user_watch_list.append(user_movie)
            
    return unique_user_watch_list


# returns a list of movies that the friends have watched, but the user hasn't
def get_friends_unique_watched(user_data):
    # compare the user's 'watched' list and the users 'watched' list
    unique_friends_watch_list= []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in user_data['watched']:
                if movie not in unique_friends_watch_list:
                    unique_friends_watch_list.append(movie)
    return unique_friends_watch_list
    
# wave 4

def get_available_recs(user_data):
    rec_list = []
    friend_watched = []
    user_watched_titles = []
    # get to iteration over  subs list and friends hosts
    for friend in user_data['friends']:
        for movie in friend['watched']: 
            friend_watched.append(movie)
    for movie in user_data['watched']:
        user_watched_titles.append(movie['title'])
    for friend_movie in friend_watched:
        friend_host = friend_movie['host']
        # if statements that have requirements of the movies to be added to a list    
        if friend_host in user_data['subscriptions']:
            if friend_movie['title'] not in user_watched_titles:
                if friend_movie not in rec_list:
                    rec_list.append(friend_movie)
    return rec_list


    #WAVE 5
# get recommendations by genre
def get_new_rec_by_genre(user_data):
    #compare most watcehd to friends 
    most_watched_genre = get_most_watched_genre(user_data)
    genre_rec_list = []
    friend_watched = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in friend_watched:
                friend_watched.append(movie)
    # add a movie to a list to give recs
    for friend_movie in friend_watched:
        friend_genre = friend_movie['genre']
        if friend_movie not in user_data['watched']:
            if friend_genre == most_watched_genre:
                if movie not in genre_rec_list:
                    genre_rec_list.append(friend_movie)
    return genre_rec_list


# get a list of users faves
def get_rec_from_favorites(user_data):
    rec_from_faves_list = []
    friend_watched = []
    for friend in user_data['friends']:
        for friend_movie in friend['watched']:
            if friend_movie not in friend_watched:
                friend_watched.append(friend_movie)

    for fave_movie in user_data['favorites']:
        if fave_movie not in  friend_watched:
            if fave_movie not in rec_from_faves_list:
                rec_from_faves_list.append(fave_movie)
    return rec_from_faves_list







    

    







