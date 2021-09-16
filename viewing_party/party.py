## TEST WAVE 1 ##

def create_movie(movie_title, genre, rating):
    movie = {}
    if movie_title and genre and rating:
        movie["title"] = movie_title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    movie_transfer = {}
    for list_index in user_data["watchlist"]:
        if movie_title in list_index.values():
            movie_transfer.update(list_index)
            user_data["watchlist"].pop()
            user_data["watched"].append(movie_transfer)
    return user_data


def get_watched_avg_rating(user_data):
    rating_list = []
    if len(user_data["watched"]) > 0:
        for watched_key in user_data["watched"]:
            rating_list.append(watched_key["rating"])
        average = (sum(rating_list)) / len(rating_list)
        return average
    else:
        return 0.0


## TEST WAVE 2 ##

def get_most_watched_genre(user_data):
    genre_freq_dict = {}
    if len(user_data["watched"]) > 0:
        for genre in user_data["watched"]:
            for genre_key, genre_name in genre.items():
                if genre_key == "genre":
                    if genre_name not in genre_freq_dict:
                        genre_freq_dict[genre_name] = 1
                    else:
                        genre_freq_dict[genre_name] += 1
    else:
        return None

    max_genre = 0
    max_genre_key = ""

    for genre_name, genre_freq in genre_freq_dict.items():
        if genre_freq > max_genre:
            max_genre_key = genre_name
            max_genre = genre_freq
    return max_genre_key


## TEST WAVE 3 ##

def get_unique_watched(user_data):
    user_list = []
    user_friend_list = []
    unique_list = []
    for movie in user_data["watched"]:
        user_list.append(movie)
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            user_friend_list.append(friend_movie)

    for user_movie in user_list:
        if user_movie not in user_friend_list:
            unique_list.append(user_movie)
    return unique_list


def get_friends_unique_watched(user_data):
    user_list = []
    user_friend_list = []
    unique_list = []
    for movie in user_data["watched"]:
        user_list.append(movie)
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_friend_list:
                user_friend_list.append(friend_movie)

    for friend_movie in user_friend_list:
        if friend_movie not in user_list:
            unique_list.append(friend_movie)
    return unique_list


## TEST WAVE 4 ##

def get_available_recs(user_data):
    recommended_movie_list = []
    for friend in user_data["friends"]:
        for movie_list in friend["watched"]:
            if movie_list["host"] in user_data["subscriptions"]:
                if {"title": movie_list["title"]} not in user_data["watched"] and movie_list not in recommended_movie_list:
                    recommended_movie_list.append(movie_list)
    return recommended_movie_list

## TEST WAVE 5 ##


def get_new_rec_by_genre(user_data):
    recommended_movie_list = []
    user_most_freq_genre = get_most_watched_genre(user_data)
    friends_movies_watched_list = get_friends_unique_watched(
        user_data)
    for movie_dict in friends_movies_watched_list:
        if movie_dict["genre"] == user_most_freq_genre:
            recommended_movie_list.append(movie_dict)
    return recommended_movie_list


def get_rec_from_favorites(user_data):
    recommended_movie_list = []
    user_fav_movie = []
    user_unique_movie = get_unique_watched(
        user_data)  # list of dictionaries key "title"
    print(user_unique_movie)
    for movie_list in user_data["favorites"]:
        user_fav_movie.append(movie_list)
    for movie in user_fav_movie:
        if movie in user_unique_movie:
            recommended_movie_list.append(movie)
    print(recommended_movie_list)
    return recommended_movie_list
