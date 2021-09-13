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
            watched_movie = movie
            break
    else:
        return user_data
    add_to_watched(user_data, watched_movie)
    watchlist.remove(watched_movie)
    return user_data

# Wave 2

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    total_ratings = 0.0
    if not watched_list:
        return total_ratings
    for movie in watched_list:
        total_ratings += movie["rating"]
    avg = total_ratings / len(watched_list)
    return avg

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    if not watched_list:
        return None
    genre_counts = {}
    for movie in watched_list:
        genre = movie["genre"]
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    max_count = max(genre_counts.values())
    for genre, count in genre_counts.items():
        if count == max_count:
            return genre

# Wave 3

def get_unique_watched(user_data):
    unique_movies = []
    for movie in user_data["watched"]:
        for friend in user_data["friends"]:
            if is_movie_in_list(friend["watched"], movie):
                break
        else:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):

    unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not is_movie_in_list(user_data["watched"], movie) and not is_movie_in_list(unique_movies, movie):
                unique_movies.append(movie)
    return unique_movies

# helper function

def is_movie_in_list(list, movie):
    """
    checks if the movie is in the list and returns boolean value
    """
    for item in list:
        if item["title"] == movie["title"]:
            return True
    return False

# Wave 4

def get_available_recs(user_data):
    subscriptions = user_data["subscriptions"]
    recommendations = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie["host"] in subscriptions:
            recommendations.append(movie)
    return recommendations

# Wave 5

def get_new_rec_by_genre(user_data):
    favorite_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    recommendations = []
    for movie in friends_unique_watched:
        if movie["genre"] == favorite_genre and not is_movie_in_list(recommendations, movie):
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    favorites = user_data["favorites"]
    return [movie for movie in unique_watched if movie in favorites]