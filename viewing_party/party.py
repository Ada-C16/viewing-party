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

    unique_movies = []
    for movie in movies_watched:
        unique_movies.append({"title": movie})

    # movies_watched_dict = {}
    # movies_watched_dict[key] = {"title"}

    
    # movies_watched = [ "Harry Potter"]
    # expected output is [ {"title": "Harry Potter" } ]

    # converted_movies_watched = set(movies_watched)
    # converted_friends_watched = set(friends_watched)

    # result_converted = converted_movies_watched - converted_friends_watched
    
    return unique_movies

