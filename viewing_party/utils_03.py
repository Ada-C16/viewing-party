def get_unique_watched(user_data):
    watched = set([movie['title'] for movie in user_data['watched']])

    friends_watched = set([movie['title']
        for friend in user_data['friends']
            for movie in friend['watched']
    ])
    
    user_unique_watched_set = watched - friends_watched
    result = [{'title': title} for title in user_unique_watched_set]
    return result
    
def get_friends_unique_watched(user_data):
    watched = set([movie['title'] for movie in user_data['watched']])

    friends_watched = set([movie['title']
        for friend in user_data['friends']
            for movie in friend['watched']
    ])
    
    friends_unique_watched_set = friends_watched - watched
    result = [{'title': title} for title in friends_unique_watched_set]
    return result
    