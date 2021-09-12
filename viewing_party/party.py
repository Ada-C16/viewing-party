def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data    

def watch_movie(user_data, title):
    new_watchlist = []
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
        else:
            new_watchlist.append(movie)
    user_data["watchlist"] = new_watchlist
    return user_data

def get_watched_avg_rating(user_data):
    ratings = make_avg_rating_list(user_data)
    num_ratings = len(ratings)
    if num_ratings > 0:
        avg_rating = sum(ratings)/num_ratings
        return avg_rating
    else:
        return 0.0

def make_avg_rating_list(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    return ratings

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    else:
        watched_genres = make_watched_genre_list(user_data)
        most_watched_genre = max(watched_genres, key = watched_genres.count)
        return most_watched_genre

def make_watched_genre_list(user_data):
    watched_genres = []
    for movie in user_data["watched"]:
        watched_genres.append(movie["genre"])
    return watched_genres

def get_friends_unique_watched(user_data):
    user_watched_set = make_user_watched_set(user_data)
    friend_watched_set = make_friends_watch_set(user_data)
    friends_unique_watched = friend_watched_set - user_watched_set
    friends_unique_watched_list = make_list_of_dict_from_set(friends_unique_watched)
    return friends_unique_watched_list

def get_unique_watched(user_data):
    user_watched_set = make_user_watched_set(user_data)
    friend_watched_set = make_friends_watch_set(user_data)
    unique_watched = user_watched_set - friend_watched_set
    unique_watched_list = make_list_of_dict_from_set(unique_watched)
    return unique_watched_list

def make_user_watched_set(user_data):
    user_watched_set = set()
    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])
    return user_watched_set

def make_friends_watch_set(user_data):
    friends_watch_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watch_set.add(movie["title"])
    return friends_watch_set

def make_list_of_dict_from_set(unique_set):
    unique_list = []
    for movie in unique_set:
        unique_list.append({"title": movie})
    return unique_list