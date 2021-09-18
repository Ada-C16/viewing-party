from .utils_03 import get_friends_unique_watched

def get_available_recs(user_data):
    subscriptions = set(user_data['subscriptions'])
    friends_subscriptions = set([movie['host']
        for friend in user_data['friends']
            for movie in friend['watched']
    ])
    
    movies_user_not_watched = [movie['title'] for movie in get_friends_unique_watched(user_data)]
    result = []
    [result.append(movie) 
        for friend in user_data['friends']
            for movie in friend['watched']
                if movie['title'] in movies_user_not_watched and movie['host'] in subscriptions and movie not in result
    ]
    return result

                


    
    