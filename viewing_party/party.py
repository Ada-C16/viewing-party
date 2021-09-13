def create_movie(movie_title, genre, rating): 
    if movie_title == None or \
    genre == None or \
    rating == None:  
        return None
    
    return {
        "title": movie_title, 
        "genre": genre, 
        "rating": rating
    }


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie): 
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title): 
    watch_list = user_data["watchlist"]
    
    for movie in watch_list: 
        if title == movie.get("title"):
            watch_list.remove(movie)
            updated_data = add_to_watched(user_data, movie)
            return updated_data

    return user_data

def get_watched_avg_rating(user_data):
    watched = user_data["watched"]

    if not user_data["watched"]: 
        return 0

    sum = 0
    for movie in watched: 
        movie_rating = movie.get("rating")
        sum += movie_rating
    
    if sum == 0: 
        return 0
    else: 
        avg_rating = sum/len(user_data["watched"])
        return avg_rating

def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    most_watched_genre_dict = {}
    
    for movie in watched: 
        genre = movie.get("genre")
        if genre in most_watched_genre_dict: 
            most_watched_genre_dict[genre] += 1
        else: 
            most_watched_genre_dict[genre] = 0
    
    if not most_watched_genre_dict: 
        return None

    most_watched_genre = max(most_watched_genre_dict, key = most_watched_genre_dict.get)  
    return most_watched_genre

def get_friends_watched(user_data):
    friends_data = user_data["friends"]
    friends_watched_list = []

    for friend in friends_data:
        for media in friend["watched"]:
            friends_watched_list.append(media)
    
    return friends_watched_list

def get_unique_watched(user_data): 
    watched = user_data["watched"]
    unique_watched_list = []

    for movie in watched:
        if movie not in get_friends_watched(user_data): 
            unique_watched_list.append(movie)

    return unique_watched_list

def get_friends_unique_watched(user_data): 
    watched = user_data["watched"]
    havent_seen_list = []
    
    for movie in get_friends_watched(user_data):
        if movie in havent_seen_list: 
            continue 
        elif movie not in watched: 
            havent_seen_list.append(movie)
    
    return havent_seen_list

def get_available_recs(user_data):
    friends_recs = get_friends_unique_watched(user_data)
    recs = []

    for media in friends_recs:
        if media["host"] in user_data["subscriptions"]:
            recs.append(media)

    return recs

def get_new_rec_by_genre(user_data): 
    friends_recs = get_friends_unique_watched(user_data)
    favorite_genre = get_most_watched_genre(user_data)
    recs_by_genre = []

    for media in friends_recs: 
        if not user_data["watched"]:
            return recs_by_genre
        if media in recs_by_genre: 
            pass
        if media["genre"] in favorite_genre: 
            recs_by_genre.append(media)
    
    return recs_by_genre

def get_rec_from_favorites(user_data):
    unique_recs = get_unique_watched(user_data)
    user_favorites = user_data["favorites"]
    recs_by_favorite_and_unique =[]

    for media in unique_recs: 
        if not user_favorites:
            recs_by_favorite_and_unique
        if media in user_favorites: 
            recs_by_favorite_and_unique.append(media)

    return recs_by_favorite_and_unique
        
