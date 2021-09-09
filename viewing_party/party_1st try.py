
def create_movie(title,genre,rating):
    if title and genre and rating:
        movie_dictionary = {}
        movie_dictionary["title"] = title
        movie_dictionary["genre"] = genre
        movie_dictionary["rating"] = rating
        return movie_dictionary
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
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

def get_watched_avg_rating(user_data):
    number_of_movies_watched = 0.0
    total_ratings = 0.0
    
    if user_data["watched"]:
        for movie in user_data["watched"]:
            number_of_movies_watched += 1
            total_ratings += movie["rating"]
        average_rating = total_ratings / number_of_movies_watched
        return average_rating
    return 0.0

def get_most_watched_genre(user_data):
    set_of_genres = set()

    if user_data["watched"]:
        for movie in user_data["watched"]:
            if not movie["genre"] in set_of_genres:
                set_of_genres.add(movie["genre"])

        genre_watch_counts = {}

        for genre in set_of_genres:
            genre_watch_counts[genre] = 0
            for movie in user_data["watched"]:
                if movie["genre"] == genre:
                    genre_watch_counts[genre] += 1

        all_counts = genre_watch_counts.values()
        highest_watch_count = max(all_counts)
        
        for genre in genre_watch_counts:
            if genre_watch_counts[genre] == highest_watch_count:
                return genre

def get_unique_watched(user_data):

    set_of_watched_movies = set()
    set_of_friends_watched_movies = set()

    for movie in user_data["watched"]:
        set_of_watched_movies.add(movie["title"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            set_of_friends_watched_movies.add(movie["title"])

    unwatched_movies = set_of_watched_movies.difference(set_of_friends_watched_movies)
    list_unwatched_movies = []

    for movie in unwatched_movies:
        list_unwatched_movies.append({"title": movie})
    return list_unwatched_movies

def get_friends_unique_watched(user_data):
    set_of_watched_movies = set()
    set_of_friends_watched_movies = set()

    for movie in user_data["watched"]:
        set_of_watched_movies.add(movie["title"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            set_of_friends_watched_movies.add(movie["title"])

    unwatched_movies = set_of_friends_watched_movies.difference(set_of_watched_movies)
    list_unwatched_movies = []

    for movie in unwatched_movies:
        list_unwatched_movies.append({"title": movie})
    return list_unwatched_movies

def get_available_recs(user_data):
    list_unwatched_movies = get_friends_unique_watched(user_data)
    set_with_host_of_recommended_movie = set()

    for movie_listed in list_unwatched_movies:
        movie = movie_listed["title"]
        for friend in user_data["friends"]:
            for watched_movie in friend["watched"]:
                if movie == watched_movie["title"]:
                    set_with_host_of_recommended_movie.add((movie, watched_movie["host"]))
    
    list_recommended_movies = []

    for movie in set_with_host_of_recommended_movie:
        host = movie[1]
        if host in user_data["subscriptions"]:
            list_recommended_movies.append({"title": movie[0], "host": host})

    return list_recommended_movies

def get_new_rec_by_genre(user_data):
    list_unwatched_movies = get_friends_unique_watched(user_data)
    set_with_genre_of_recommended_movie = set()

    for movie_listed in list_unwatched_movies:
        movie = movie_listed["title"]
        for friend in user_data["friends"]:
            for watched_movie in friend["watched"]:
                if movie == watched_movie["title"]:
                    set_with_genre_of_recommended_movie.add((movie, watched_movie["genre"]))


    favorite_genre = get_most_watched_genre(user_data)
    list_recommended_movies = []

    for movie in set_with_genre_of_recommended_movie:
        genre = movie[1]
        if genre == favorite_genre:
            list_recommended_movies.append({"title": movie[0], "genre": genre})

    return list_recommended_movies

def get_rec_from_favorites(user_data):
    unwatched_movies = get_unique_watched(user_data)
    list_recommended_movies = []

    for movie_listed in unwatched_movies:
        movie = movie_listed["title"]
        for favorite in user_data["favorites"]:
            if movie == favorite["title"]:
                list_recommended_movies.append({"title": movie})
    return list_recommended_movies
