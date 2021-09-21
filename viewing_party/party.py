# FUNCTIONS:


def create_movie(title, genre, rating):
    if title == None:
        return None
    elif genre == None:
        return None
    elif rating == None:
        return None
    else:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
    return movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data,title):
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
        else: 
            continue
    return user_data


def get_watched_avg_rating(user_data):
    rating_list = []
    average = 0
    watched = user_data["watched"]
    for movie in watched:
        rating_list.append(movie["rating"])
    if len(rating_list)==0:
        average = 0.0
        return average 
    else:
        average = sum(rating_list)/len(watched)
    return average


def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    genre_list = []
    popular_genre = "some genre"
    for movie in watched:
        genre_list.append(movie["genre"])
    if len(genre_list)==0:
        popular_genre = None
        return popular_genre
    else:
        popular_genre = max(set(genre_list),key=genre_list.count)
        return popular_genre


def get_unique_watched(user_data):
    watched = user_data["watched"]
    unique_movies_list = []
    for movie in watched:
        if movie not in get_friends_watched(user_data):
            unique_movies_list.append(movie)
    return unique_movies_list


def get_friends_unique_watched(user_data):
    my_movies = []
    for movie in user_data["watched"]:
            my_movies.append(movie)
    my_friends_movies = get_friends_watched(user_data)
    no_dup_friends_movies = [i for n, i in enumerate(my_friends_movies) if i not in my_friends_movies[n + 1:]]
    unique_movies_list = []
    for movie in no_dup_friends_movies:
      if {"title":movie["title"]} not in my_movies:
        unique_movies_list.append(movie)
    return unique_movies_list


def get_available_recs(user_data):
    watched = user_data["watched"]
    recommended_movies = []
    friends_movie_list = get_friends_unique_watched(user_data)
    for movie in friends_movie_list:
        if movie["host"] in user_data["subscriptions"] and movie["title"]not in watched:
            recommended_movies.append(movie)
    return recommended_movies


def get_new_rec_by_genre(user_data):
    watched = user_data["watched"]
    recommended_movies = []
    users_genre = get_most_watched_genre(user_data)
    friends_movie_list = get_friends_unique_watched(user_data)
    if len(watched)==0:
        return recommended_movies
    else:
        for movie in friends_movie_list:
            if movie["genre"] in users_genre and movie["title"]not in watched:
                recommended_movies.append(movie)
    return recommended_movies


def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    recommended_movies = []
    my_friends_movies = get_friends_watched(user_data)
    no_dup_friends_movies = [i for n, i in enumerate(my_friends_movies) if i not in my_friends_movies[n + 1:]]
    print (no_dup_friends_movies)
    for movie in favorites:
            if movie not in no_dup_friends_movies:
                recommended_movies.append(movie)
    return recommended_movies

# HELPER FUNCTION:


def get_friends_watched(user_data):
    friends_data = user_data["friends"]
    friends_watched_list = []
    for friend in friends_data:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)
    return friends_watched_list








            



