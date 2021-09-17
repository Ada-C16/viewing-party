# Wave 01

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
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
            break
    return user_data

# Wave 02

def get_watched_avg_rating(user_data):
    sum_ratings = 0
    ratings_count = 0
    for movie in user_data["watched"]:
        sum_ratings += movie["rating"]
        ratings_count += 1
    if ratings_count > 0:
        avg_rating = sum_ratings/ratings_count
        return avg_rating
    else:
        return 0.0

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    else:
        genre_dict = {}
        for movie in user_data["watched"]:
            if movie["genre"] not in genre_dict:
                genre_dict[movie["genre"]] = 1
            else:
                genre_dict[movie["genre"]] += 1
        most_watched_genre = max(genre_dict, key=genre_dict.get)
        return most_watched_genre


# Wave 03

def get_unique_watched(user_data):
    user_watched_set = make_user_watched_set(user_data)
    friend_watched_set = make_friends_watch_set(user_data)
    unique_watched_set = user_watched_set - friend_watched_set
    unique_watched_list = make_list_of_dict_from_set(unique_watched_set)
    return unique_watched_list

def get_friends_unique_watched(user_data):
    user_watched_set = make_user_watched_set(user_data)
    friend_watched_set = make_friends_watch_set(user_data)
    friends_unique_watched_set = friend_watched_set - user_watched_set
    friends_unique_watched_list = make_list_of_dict_from_set(friends_unique_watched_set)
    return friends_unique_watched_list

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

# Wave 04

def get_available_recs(user_data):
    recommendations = []
    friends_watched_set = make_friends_watch_set(user_data)
    watched_set = make_user_watched_set(user_data)
    friends_unique_watched = friends_watched_set - watched_set
    friends_unique_watched_host = get_friends_unique_watched_host(user_data, friends_unique_watched)
    for movie in friends_unique_watched:
        host = friends_unique_watched_host[movie]   
        if host in user_data["subscriptions"]:
            recommendations.append({"title": movie, "host": host})
    return recommendations

def get_friends_unique_watched_host(user_data, friends_unique_watched):
    friends_watched_with_host = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_with_host[movie["title"]] = movie["host"]
    return friends_watched_with_host

# Wave 05

# ***********************************
def get_new_rec_by_genre(user_data):
    recs_by_genre = []
    user_watched = make_user_watched_set(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in recs_by_genre and movie["genre"] == most_watched_genre\
                and movie["title"] not in user_watched:
                recs_by_genre.append(movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    recs_from_favorites = []
    friends_unique_watched = make_friends_watch_set(user_data)
    for movie in user_data["favorites"]:
        if movie["title"] not in friends_unique_watched:
            recs_from_favorites.append(movie)
    return recs_from_favorites
