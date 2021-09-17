def create_movie(movie_title, genre, rating):
    movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
  
    }

    if movie_title is None:
        return None
    if genre is None:
        return None
    if rating is None:
        return None
    return movie


def add_to_watched(user_data, movie):
        user_data["watched"].append(movie)

        return user_data
    
def add_to_watchlist(user_data, movie):
        user_data["watchlist"].append(movie)

        return user_data

def watch_movie(user_data, title):
        for movie in user_data["watchlist"]:
            if movie["title"] == title:
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)
                new_watchlist = user_data["watchlist"]
        
        # converted_watchlist = set(user_data["watchlist"])
        # converted_watched = set(user_data["watched"])

        # result_converted = converted_watchlist - converted_watched
        # user_data["watchlist"] = list(result_converted)

        return user_data

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0
    average = 0
    for movie in user_data["watched"]:
        average += movie["rating"]

    return average / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_count = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
        else:
            genre_count[movie["genre"]] = 1
    
    max_value = 0
    max_genre = None

    for genre in genre_count:
        if genre_count[genre] > max_value:
            max_value = genre_count[genre]
            max_genre = genre

    return max_genre

def get_unique_watched(user_data):
    movies_watched = []
    friends_watched = []

    for movie in user_data["watched"]:
        movies_watched.append(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie["title"])

    #compare movies_watched with friends_watched
    #.remove method on movies_watched

    for movie in friends_watched:
        if movie in movies_watched:
            movies_watched.remove(movie)

    # unique_movies = []
    # for movie in movies_watched:
    #     unique_movies.append({"title": movie})

    converted_movies_watched = set(movies_watched)
    converted_friends_watched = set(friends_watched)

    result_converted = converted_movies_watched - converted_friends_watched

    unique_movies = []
    for movie in result_converted:
        unique_movies.append({"title": movie})
    
    return unique_movies

def get_friends_unique_watched(user_data):
    movies_watched = []
    friends_watched = []

    for movie in user_data["watched"]:
        movies_watched.append(movie["title"])
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie["title"])
    
    for movie in friends_watched:
        if movie in movies_watched:
            friends_watched.remove(movie)

    converted_movies_watched = set(movies_watched)
    converted_friends_watched = set(friends_watched)

    result_converted = converted_friends_watched - converted_movies_watched

    unique_movies_friends = []
    for movie in result_converted:
        unique_movies_friends.append({"title": movie})
    
    return unique_movies_friends

def get_available_recs(user_data):
    movies_watched = []
    friends_watched = []
    movies_recommended = []

    for movie in user_data["watched"]:
        movies_watched.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for user_movie in movies_watched:
        found = []
        for friend_movie in friends_watched:
            if friend_movie["title"] == user_movie["title"]:
                found.append(friend_movie)
        
        for found_movie in found:
            friends_watched.remove(found_movie)
        # if movie in movies_watched:
        #     friends_watched.remove(movie)
    
    for friend_movie in friends_watched:
        if friend_movie["host"] in user_data["subscriptions"] and friend_movie not in movies_recommended:
            movies_recommended.append(friend_movie)
    
    return movies_recommended

    
    


    #iterate through what friends have watched
    # create a list that describes the movies for recommend
    # if movie title is in watched and host is in subscriptions, then add it to movies_recommended
    # return a list of dictionaries 

def get_new_rec_by_genre(user_data):
    movies_watched = []
    friends_watched = []
    movies_recommended = []

    for movie in user_data["watched"]:
        movies_watched.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for user_movie in movies_watched:
        found = []
        for friend_movie in friends_watched:
            if friend_movie["title"] == user_movie["title"]:
                found.append(friend_movie)
        
        for found_movie in found:
            friends_watched.remove(found_movie)

    genre_count = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
        else:
            genre_count[movie["genre"]] = 1
    
    max_value = 0
    max_genre = None

    for genre in genre_count:
        if genre_count[genre] > max_value:
            max_value = genre_count[genre]
            max_genre = genre

    for friend_movie in friends_watched:
        if max_genre == friend_movie["genre"] and friend_movie not in movies_recommended:
            movies_recommended.append(friend_movie)

    return movies_recommended

def get_rec_from_favorites(user_data):
    unique_favorites = get_unique_watched(user_data)
    recommended_movies = []

    for movie in user_data["favorites"]:
        for favorite_movie in unique_favorites:
            if favorite_movie == movie:
                recommended_movies.append(movie)

    return recommended_movies


    
    
    
    
    
    
