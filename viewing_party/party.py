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
    if not user_data["watched"]:
        return 0.0
    else:
        sum_ratings = 0
        ratings_count = 0
        for movie in user_data["watched"]:
            sum_ratings += movie["rating"]
            ratings_count += 1
        avg_rating = sum_ratings/ratings_count
        return avg_rating

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
    unique_watched = []
    friend_watched = get_friends_watched(user_data)
    for movie in user_data["watched"]:
        if movie not in friend_watched:
            unique_watched.append(movie)
    return unique_watched

def get_friends_watched(user_data):
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)
    return friends_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
    return friends_unique_watched

# Wave 04

def get_available_recs(user_data):
    recommendations = []
    friends_watched = get_friends_watched(user_data)
    user_watched_titles = get_user_watched_titles(user_data)
    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"] and movie["title"] \
        not in user_watched_titles:
            recommendations.append(movie)
    return recommendations

def get_user_watched_titles(user_data):
    user_watched_titles = []
    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])
    return user_watched_titles

# Wave 05

def get_new_rec_by_genre(user_data):
    recs_by_genre = []
    most_watched_genre = get_most_watched_genre(user_data)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in recs_by_genre and movie["genre"] == most_watched_genre\
                and movie["title"] not in user_data["watched"]:
                recs_by_genre.append(movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    recs_from_favorites = []
    friends_watched = get_friends_watched(user_data)
    for movie in user_data["favorites"]:
        if movie not in friends_watched:
            recs_from_favorites.append(movie)
    return recs_from_favorites
