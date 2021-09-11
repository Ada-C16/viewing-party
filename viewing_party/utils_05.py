from .utils_03 import *

def get_new_rec_by_genre(user_data):
    genres = set([movie['genre']
        for movie in user_data['watched']
    ])

    movies_user_not_watched = [movie['title'] for movie in get_friends_unique_watched(user_data)]
    result = []
    [result.append(movie) 
        for friend in user_data['friends']
            for movie in friend['watched']
                if movie['title'] in movies_user_not_watched and movie['genre'] in genres and movie not in result
    ]
    return result

def get_rec_from_favorites(user_data):
    movies_friends_not_watched = [movie['title'] for movie in get_unique_watched(user_data)]
    result = [movie 
        for movie in user_data['favorites']
            if movie['title'] in movies_friends_not_watched
    ]
    return result