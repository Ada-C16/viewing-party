from pprint import pprint

#  Wave 1 **********************************************

# 1

def create_movie(title, genre, rating):
    
    movie = {}

    if title is None or genre is None or rating is None:
        return None

    if title:
        movie["title"] = title

    if genre:
        movie["genre"] = genre

    if rating:
        movie["rating"] = rating

    return movie


# 2

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data


# 3

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data


# 4

def watch_movie(user_data, title):
    watched = user_data["watched"]
    watch_list = user_data["watchlist"]

    for index, movie_info in enumerate(watch_list):
        if title == movie_info["title"]:
            watched.append(movie_info)
            user_data["watched"] = watched
            del watch_list[index]
    return user_data


# Wave 2 **********************************************

# 1

def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    ratings = []
    for movie_info in (watched):
        ratings.append(movie_info["rating"])

    if len(watched) == 0:
        return 0.0
    else:
        avg_rating = sum(ratings)/len(ratings)
        return avg_rating


# 2

def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    genres = []
    for movie_info in watched:
        genres.append(movie_info["genre"])

    fav_genres = {}
    if len(watched) == 0:
        return None 
    else:
        for genre in genres:
            if genre not in fav_genres:
                fav_genres[genre] = 1
            else:
                fav_genres[genre] += 1
    
    favorite_genre = max(fav_genres, key=fav_genres.get)
    
    return favorite_genre


# Wave 3 **********************************************

# 1

def get_unique_watched(user_data):
    unique_watched_list = []
    for dicts in user_data["watched"]:
        unique_watched_list.append(dicts)
    
    friends_watched_list = []
    for friends_watched in user_data["friends"]:
        for friends_dicts in friends_watched["watched"]:
            friends_watched_list.append(friends_dicts)

    unique_watched_set = set()
    friends_watched_set = set()

    if len(user_data["watched"]) == 0:
        return []
    else:
        for movie_dict in unique_watched_list:
            for movie in movie_dict.values():
                unique_watched_set.add(movie)
        for friends_movie_dicts in friends_watched_list:
            for title in friends_movie_dicts.values():
                friends_watched_set.add(title)

    set_difference = unique_watched_set - friends_watched_set
    unique_watched_list = list(set_difference)

    users_unique_watched_list = []
    for unique_movies in unique_watched_list:
        list_of_dicts = {"title": unique_movies}
        users_unique_watched_list.append(list_of_dicts)

    return users_unique_watched_list


# 2

def get_friends_unique_watched(user_data):
    user_watched_list = []
    for user_dicts in user_data["watched"]:
        user_watched_list.append(user_dicts)

    friends_watched_list = []
    for friend_list in user_data["friends"]:
        for friend_dicts in friend_list["watched"]:
            friends_watched_list.append(friend_dicts)

    user_watched_set = set()
    friends_watched_set = set()
    for list_of_dicts in user_data["friends"]:
        for watched_list in list_of_dicts["watched"]:
            if len(watched_list) == 0:
                return []
        else: 
            for movie_dict in user_watched_list:
                for movie in movie_dict.values():
                    user_watched_set.add(movie)
            for friends_movie_dicts in friends_watched_list:
                for title in friends_movie_dicts.values():
                    friends_watched_set.add(title)

    set_difference = friends_watched_set - user_watched_set
    unique_watched_list = list(set_difference)

    friends_unique_watched_list = []
    for unique_movies in unique_watched_list:
        list_of_dicts = {"title": unique_movies}
        friends_unique_watched_list.append(list_of_dicts)

    return friends_unique_watched_list


# Wave 4 **********************************************

# 1

def get_available_recs(user_data):
    user_movies = []
    for movie in user_data["watched"]:
        user_movies.append(movie["title"])

    recommended_movies = []
    for friends_watched in user_data["friends"]:
        for friend_dicts in friends_watched["watched"]:
            if (
                friend_dicts["title"] not in user_movies
                and friend_dicts["host"] in user_data["subscriptions"]
                and friend_dicts not in recommended_movies
            ):
                recommended_movies.append(friend_dicts)
    
    return recommended_movies


# Wave 5 **********************************************

# 1

def get_new_rec_by_genre(user_data):
    import statistics
    from statistics import mode

    favorite_genres = []
    for watched in user_data["watched"]:
        favorite_genres.append(watched["genre"])
    
    if len(favorite_genres) == 0:
        return []
    else:
        favorite_genre = mode(favorite_genres)

    user_movies = []
    for movie in user_data["watched"]:
        user_movies.append(movie["title"])

    recommended_movies = []
    for friends_watched in user_data["friends"]:
        for friend_dicts in friends_watched["watched"]:
            if (
                friend_dicts["title"] not in user_movies
                and friend_dicts["genre"] == favorite_genre
                and friend_dicts not in recommended_movies
            ):
                recommended_movies.append(friend_dicts)

    return recommended_movies


# 2


def get_rec_from_favorites(user_data):

    favorites = []
    for faves in user_data["favorites"]:
        favorites.append(faves["title"])
    
    if len(favorites) == 0:
        return []

    favorites_set = set(favorites)
    friends_watched_set= set()
    for friends_watched in user_data["friends"]:
        for friend_list in friends_watched["watched"]:
            friends_watched_set.add(friend_list["title"])
    
    recommendation = favorites_set - friends_watched_set
    rec_list = list(recommendation)

    for rec in rec_list:
        recommended_dict = {"title": rec}
        recommended_movies = [recommended_dict]

    return recommended_movies

