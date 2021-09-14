def create_movie(movie_title, genre, rating):
    if not (movie_title and genre and rating):
        return None
    else:
        return {"title": movie_title, "genre": genre, "rating": rating}

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for dict in watchlist:
        if dict["title"] == title:
            user_data["watched"].append(dict.copy())
            watchlist.remove(dict)
    return user_data

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    if watched_list:    
        sum = 0
        for movie in watched_list:
            sum += float(movie["rating"])
        return sum / len(watched_list)
    else:
        return 0

def get_most_watched_genre(user_data):
    genre_frequency = {}
    watched_list = user_data["watched"]
    for movie in watched_list:
        if movie["genre"] in genre_frequency.keys():
            genre_frequency[movie["genre"]] += 1
        else:
            genre_frequency[movie["genre"]] = 1
    max_frequency = 0
    popular_genre = None
    for genre, frequency in genre_frequency.items():
        if frequency > max_frequency:
            max_frequency = frequency
            popular_genre = genre
    return popular_genre

def get_unique_watched(user_data):
    user_watched_set = set()
    user_watched_list = user_data['watched']
    for dict in user_watched_list:
        user_watched_set.add(dict["title"])
    friends_watched_set = set()
    friends_list = user_data["friends"]
    for dict in friends_list:
        watched_list = dict["watched"]
        for item in watched_list:
            friends_watched_set.add(item["title"])
    unique_watched_set = (user_watched_set - friends_watched_set)
    result = []
    for movie in unique_watched_set:
        result.append({"title": movie})
    return result

def get_friends_unique_watched(user_data):
    user_watched_set = set()
    user_watched_list = user_data['watched']
    for dict in user_watched_list:
        user_watched_set.add(dict["title"])
    friends_watched_set = set()
    friends_list = user_data["friends"]
    for dict in friends_list:
        watched_list = dict["watched"]
        for item in watched_list:
            friends_watched_set.add(item["title"])
    unique_watched_set = (friends_watched_set - user_watched_set)
    result = []
    for movie in unique_watched_set:
        result.append({"title": movie})
    return result

def get_available_recs(user_data):
    subscriptions_set = set(user_data["subscriptions"])
    recs_set = set()
    user_watched_set = set()
    user_watched_list = user_data['watched']
    for dict in user_watched_list:
        user_watched_set.add(dict["title"])
    friends_list = user_data["friends"]
    for dict in friends_list:
        watched_list = dict["watched"]
        for item in watched_list:
            if item["title"] not in user_watched_set and item["host"] in subscriptions_set:
                recs_set.add((item["title"], item["host"]))
    result = []
    for movie, host in recs_set:
        result.append({"host": host, "title": movie})
    return result

def get_new_rec_by_genre(user_data):
    recs_set = set()
    user_watched_set = set()
    user_favorite_genre = get_most_watched_genre(user_data)
    user_watched_list = user_data['watched']
    for dict in user_watched_list:
        user_watched_set.add(dict["title"])
    friends_list = user_data["friends"]
    for dict in friends_list:
        watched_list = dict["watched"]
        for item in watched_list:
            if item["title"] not in user_watched_set and item["genre"] == user_favorite_genre:
                recs_set.add((item["title"], item["genre"]))
    result = []
    for movie, genre in recs_set:
        result.append({"genre": genre, "title": movie})
    return result

def get_rec_from_favorites(user_data):
    favorites_set = set()
    recs_set = set()
    for dict in user_data["favorites"]:
        favorites_set.add(dict["title"])
    friends_watched_set = set()
    friends_list = user_data["friends"]
    for dict in friends_list:
        watched_list = dict["watched"]
        for item in watched_list:
            friends_watched_set.add(item["title"])
    recs_set = favorites_set - friends_watched_set
    result = []
    for movie in recs_set:
        result.append({"title": movie})
    return result
