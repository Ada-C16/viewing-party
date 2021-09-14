def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None
    new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
        }
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    movies_to_remove = []
    for item in user_data["watchlist"]:
        for key, value in item.items():
            if key == "title" and value == title:
                movie = user_data["watchlist"][user_data["watchlist"].index(item)]
                movies_to_remove.append(movie)
    if len(movies_to_remove) == 0:
        return user_data
    else:
        for movie in movies_to_remove:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data
                
def get_watched_avg_rating(user_data):
    ratings = []
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        for movie in user_data["watched"]:
            ratings.append(user_data["watched"][user_data["watched"].index(movie)]["rating"])
        num_of_movies = len(ratings)
        ratings_total = sum(ratings)
        avg_rating = ratings_total / num_of_movies
        return avg_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    popular_genres = {}
    for movie in user_data["watched"]:
        for key, value in movie.items():
            if key == "genre":
                if value not in popular_genres:
                    popular_genres[value] = 1
                else:
                    popular_genres[value] += 1
    popularity = 0
    for key, value in popular_genres.items():
        if value > popularity:
            popularity = value
            most_popular_genre = key
    return most_popular_genre


amandas_data = {
        "watched": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            },
            {
                "title": "Title C"
            },
            {
                "title": "Title D"
            },
            {
                "title": "Title E"
            },
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title D"
                    },
                    {
                        "title": "Title F"
                    }
                ]
            }
        ]
    }


def get_unique_watched(user_data):
    friends_watched = []
    unique_movies = []
    for friend in user_data["friends"]:
        for item in friend["watched"]:
            friends_watched.append(item)
    for movie in user_data["watched"]:
        if movie not in friends_watched:
            unique_movies.append(movie)
    return unique_movies


get_unique_watched(amandas_data)