def create_movie(movie_title, genre, rating):
    new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }

    for key in new_movie:
        if new_movie[key] == None:
            return None
    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie_title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    
    return user_data


def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    total_rating = 0.0
    
    for movie in user_data["watched"]:
        total_rating += movie["rating"] 
    
    if len(user_data["watched"]) > 0:
        avg_rating = total_rating/len(user_data["watched"])
    return avg_rating


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_dict = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1

    most_freq = genre
    for genre, freq in genre_dict.items():
        if freq > genre_dict[most_freq]:
            most_freq = genre

    return most_freq


def get_unique_watched(user_data):

    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie)
    
    friends_watched = []
    for watched_dict in user_data["friends"]:
        for title in watched_dict["watched"]:
            friends_watched.append(title)

    user_unique_watched = []
    for movie in user_watched:
        if movie not in friends_watched:
            user_unique_watched.append(movie)

    return user_unique_watched


def get_friends_unique_watched(user_data):
    
    friends_watched = []
    for watched_dict in user_data["friends"]:
        for title in watched_dict["watched"]:
            friends_watched.append(title)
    
    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie)
    

    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in friends_unique_watched:
            movie_in_user_watched = False
            for title in user_watched: 
                if movie["title"] == title["title"]:
                    movie_in_user_watched = True

            if not movie_in_user_watched:
                friends_unique_watched.append(movie)

    return friends_unique_watched


def get_available_recs(user_data):
    watchlist = get_friends_unique_watched(user_data)

    movie_recs = []
    for movie in watchlist:
        if movie["host"] in user_data["subscriptions"]:
            movie_recs.append(movie)
    
    return movie_recs


def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    available_recs = get_friends_unique_watched(user_data)

    movie_recs = []
    for movie in available_recs:
        if fav_genre == movie["genre"]:
            movie_recs.append(movie)
    return movie_recs


def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    fav_recs = []

    for movie in user_data["favorites"]:
        if movie in unique_watched:
            fav_recs.append(movie)

    return fav_recs
