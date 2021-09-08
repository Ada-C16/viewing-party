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
    '''takes in a user_data dict with two keys--watch list and watched--that 
    each correspond to a list of movies, and a title; returns updated 
    user_data depending on which condition is met'''
    for movie in user_data['watchlist']:
        if title == movie['title']:
            add_to_watched(user_data, movie)
            user_data['watchlist'].remove(movie)
    return user_data

def get_watched_avg_rating(user_data):
    '''takes in a user_data dict with key 'watched' and values of list of 
    watched movies; returns average rating of all movies'''
    rating_sum, num_of_movies = 0, len(user_data['watched']) 
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
# sample data
# user_data = {
#     'watched' : [{
#             'title': 'Bridesmaids',
#             'genre': 'comedy',
#             'rating': 5
#         }, 
#         {
#             'title': 'Us',
#             'genre': 'horror',
#             'rating': 4.5
#         },
#         {
#             'title': 'Candyman',
#             'genre': 'horror',
#             'rating': 4.5
#         }], 
#     'watchlist' : [{
#             'title': 'John Wick III',
#             'genre': 'action',
#             'rating': 3
#         }, 
#         {
#             'title': 'Her',
#             'genre': 'scifi',
#             'rating': 4
#         }]
# }

# user_data2 = {
#     'watched' : []
# }

# get_most_watched_genre(user_data)