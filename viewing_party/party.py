# Wave 1

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    return {
        "title": title,
        "genre": genre,
        "rating": rating,
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if movie["title"] == title:
            watched_from_watchlist = movie
            break
        watched_from_watchlist = None
    if watched_from_watchlist:
        watchlist.remove(watched_from_watchlist)
        user_data["watched"].append(watched_from_watchlist)
    return user_data

# Wave 2

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    if not watched_list:
        return 0.0

    total_ratings = 0
    for movie in watched_list:
        total_ratings += movie["rating"]
    avg = total_ratings / len(watched_list)
    return avg

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    if len(watched_list) == 0:
        return None
    genre_counts = {}
    for movie in watched_list:
        genre = movie["genre"]
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    
    max_count = max(genre_counts.values())
    for genre, count in genre_counts.items():
        if count == max_count:
            return genre
    # What if more than one generes at the same max counts?


# Wave 3

def get_unique_watched(user_data):
    movies_watched = user_data["watched"]
    friends = user_data["friends"]

    unique_movies = []
    for movie in movies_watched:
        is_unique = True
        for friend in friends:
            if movie in friend["watched"]:
                is_unique = False
                break
        if is_unique:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    movie_watched = user_data["watched"]
    friends = user_data["friends"]

    unique_movies = []
    for friend in friends:
        for movie in friend["watched"]:
            if movie not in movie_watched and movie not in unique_movies:
                unique_movies.append(movie)
    return unique_movies
