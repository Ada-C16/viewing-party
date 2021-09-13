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
    for item in user_data["watchlist"]:
        for key, value in item.items():
            if key == "title" and value == title:
                movie = user_data["watchlist"][user_data["watchlist"].index(item)]
    user_data["watched"].append(movie)
    user_data["watchlist"].remove(movie)
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

def get_unique_watched(user_data):
    unique_movies_dict = {}
    unique_movies = []
    for movie in user_data["watched"]:
        for key, value in movie.items():
            if value not in unique_movies_dict:
        # if movie not in unique_movies_dict:
                unique_movies_dict[movie] = 1
            else:
                unique_movies_dict[movie] += 1
    for movie in unique_movies_dict:
        if unique_movies_dict[movie] == 1:
            unique_movies.append(unique_movies_dict[movie])
    return unique_movies

# def map_character_frequency(words):
#     char_map = {}
#     for word in words:
#         for character in word:
#             if character not in char_map:
#                 char_map[character] = 1
#             else:
#                 char_map[character] += 1
#     return char_map





    # friend_titles = []
    # print(friend_titles)
    # unique_movies = []
    # for friend in user_data["friends"]:
    #     for key, value in friend.items():
    #         friend_titles.append(value)
    # for movie in user_data["watched"]:
    #     for key, value in movie.items():
    #         if value not in friend_titles:
    #             unique_movies.append(movie)
    # return unique_movies
    


# get_unique_watched(user_data)
    
    # user_titles_watched = []
    # # user_watched = set()
    # for item in user_data["watched"]:
    #     user_titles_watched.append(item)
    # user_watched = set(user_titles_watched)
    # friends_watched = set()
    # for item in user_data["friends"]:
    #     friends_movies = user_data["friends"][user_data["friends"].index(item)]
    #     friends_watched.update(friends_movies)
    # unique_movies = user_watched.difference(friends_watched)
    # return unique_movies


    # friends_watched = set()
    # for item in user_data["friends"]:
    #     for key, value in item.items():
    #         friend_movies = user_data["friends"][user_data["friends"]["watched"].index(item)]["title"]
    #         friends_watched.update(friend_movies)
    # unique_movies = user_watched.difference(friends_watched)
    # return unique_movies