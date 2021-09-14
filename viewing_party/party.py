# Two general questions:
# 1. Should I remove these wordy docstrings? They were written to help me in 
#    my process, but seem a bit long for "real life" (?).  
# 2. Should I avoid list comprehensions b/c they're too confusing for 
#    someone reading your code who is not you? (See first line of 
#    find_user_and_friend_movies() function as an example.)

def create_movie(title, genre, rating):
    '''returns a dict with 3 key-value pairs (1 per param)'''
    if title and genre and rating:
        return {
            'title': title,
            'genre': genre,
            'rating': rating
        } 
    return None 

def add_to_watched(user_data, movie):
    '''takes in a user_data dict with key 'watched' and a value which is a 
    list of dicts repping movies the user watched and a movie to add to 
    user_data; returns updated user_data'''
    user_data['watched'].append(movie) 
    return user_data

def add_to_watchlist(user_data, movie):
    '''takes in a user_data dict with key 'watchlist' and a value which is a 
    list of dicts repping movies the user wants to watch and a movie to add to 
    user_data; returns updated user_data'''
    user_data['watchlist'].append(movie) 
    return user_data

def watch_movie(user_data, title):
    '''takes in a user_data dict with two keys--watchlist and watched--that 
    each correspond to a list of movies, and a title; if title in watchlist,
    it's removed from watchlist + added to watched; returns user_data'''
    for movie in user_data['watchlist']:
        if title == movie['title']:
            user_data['watchlist'].remove(movie)
            add_to_watched(user_data, movie)
    return user_data

def get_watched_avg_rating(user_data):
    '''takes in a user_data dict with key 'watched' and values of list of 
    watched movies; returns average rating of all movies'''
    rating_sum = 0
    num_of_movies = len(user_data['watched']) 
    for movie in user_data['watched']:
        rating_sum += movie['rating']
    return 0.0 if num_of_movies == 0 else rating_sum/num_of_movies

def get_most_watched_genre(user_data):
    '''takes in a user_data dict with key 'watched' and values of list of 
    watched movies; returns which genre occurs most frequently in list'''
    if user_data['watched'] == []: return None 
    
    genre_dict = {}
    for movie in user_data['watched']:
        genre = movie['genre']
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1

    return max(genre_dict, key=genre_dict.get)  

# extra helper method that's not asked for but was made to DRY up code 
def find_user_and_friend_movies(user_data):
    '''takes in a user_data dict with keys 'watched' (list of watched movies)
    and friends (list of friends and movies they've watched); returns two 
    lists--one that reps movies only user has watched and one that reps 
    movies only friends have watched'''
    movies_user_watched = [movie['title'] for movie in user_data['watched']]

    movies_friends_watched = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            movies_friends_watched.append(movie['title'])
    
    return movies_user_watched, movies_friends_watched

def get_unique_watched(user_data):
    '''takes in a user_data dict with keys 'watched' (list of watched movies)
    and friends (list of friends and movies they've watched); returns list of 
    dicts that rep list of movies that user has watched but friends haven't''' 
    user_movies, friend_movies = find_user_and_friend_movies(user_data)
    user_unique_movies = set(user_movies) - set(friend_movies)
    return [{ 'title' : movie } for movie in user_unique_movies]
    
def get_friends_unique_watched(user_data):
    '''takes in a user_data dict with keys 'watched' (list of watched movies)
    and friends (list of friends and movies they've watched); returns list of 
    dicts that rep list of movies a friend has watched but user hasn't'''
    user_movies, friend_movies = find_user_and_friend_movies(user_data)
    friend_unique_movies = set(friend_movies) - set(user_movies)
    return [{ 'title' : movie } for movie in friend_unique_movies]

def get_available_recs(user_data):
    '''takes in a user_data dict with keys 'subscriptions' (list of streaming
    services), 'watched' (list of movies), and 'friends' (list of 'watched' 
    dicts that contain titles and streaming service hosts); returns list of 
    movies that user hasn't watched that friend has watched + shares a 
    streaming service with the user'''
    recommendations = []

    for friend in user_data['friends']:
        for movie in friend['watched']:
            title, host = movie['title'], movie['host']
            new_rec = {"title": title, "host": host}

            if title not in find_user_and_friend_movies(user_data)[0] and\
                host in user_data['subscriptions'] and\
                new_rec not in recommendations:
                    recommendations.append(new_rec)

    return recommendations

def get_new_rec_by_genre(user_data):
    '''takes in a user_data dict with keys 'watched' (list of watched movies)
    and friends (list of friends and movies they've watched); returns list of 
    recommendations that user should watch based on genre they watch most'''
    top_genre = get_most_watched_genre(user_data)
    recommendations = []

    for friend in user_data['friends']:
        for movie in friend['watched']:
            title, genre = movie['title'], movie['genre']
            new_rec = {"title": title, "genre": genre}

            if title not in find_user_and_friend_movies(user_data)[0] and\
                genre == top_genre and\
                new_rec not in recommendations:
                    recommendations.append(new_rec)
    
    return recommendations

def get_rec_from_favorites(user_data):
    '''takes in a user_data dict with keys 'watched' (list of watched movies),
    'favorites' (list of fav movies), and friends (list of friends and movies 
    they've watched); returns list of recommendations that are in users favs
    that none of user's friends have watched'''
    recommendations = []

    for movie in get_unique_watched(user_data):
        if movie in user_data['favorites']:
            recommendations.append(movie)
    
    return recommendations