import collections

def get_watched_avg_rating(user_data):
    watched = user_data['watched']
    avg_rating = sum(movie['rating'] for movie in watched) / len(watched) if watched else 0
    return avg_rating

def get_most_watched_genre(user_data):
    watched = user_data['watched']
    if watched:
        genre_count = collections.Counter(movie['genre'] for movie in watched)
        most_watched = genre_count.most_common(1)
        return most_watched[0][0]
    return None