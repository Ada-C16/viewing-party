# wave 1
from typing import ItemsView


def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        new_movie = {"title": title, "genre": genre, "rating": rating,}
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            del user_data["watchlist"][i]
    return user_data

# wave 2
def get_watched_avg_rating(user_data):
    average_rating = 0.0
    movies_watched = len(user_data["watched"])
    rating_numerator = 0
    for i in range(len(user_data["watched"])):
        rating_numerator += user_data["watched"][i]["rating"]
    if len(user_data["watched"]) == 0:
        return average_rating
    else:
        average_rating = (rating_numerator / movies_watched)
        return average_rating

def get_most_watched_genre(user_data):
    genre_list = []
    genre_dict = {}
    most_frequent = ""
    frequency = 0
    if len(user_data["watched"]) == 0:
        return None
    for i in range(len(user_data["watched"])):
        genre_list.append(user_data["watched"][i]["genre"])
    for genre in genre_list:
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1
    else:
        # reversed_genre_dict = {value: key for (key, value) in genre_dict.items()}
        for key, value in genre_dict.items():
            if value > frequency:
                most_frequent = key
        return most_frequent

# wave 3
def get_unique_watched(user_data):
    #use sets
    friend_movie_list = []
    user_movie_list = []
    unique_list = []
    for friend in range(len(user_data["friends"])):
        for movie in range(len(user_data["friends"][friend]["watched"])):
            friend_movie_list.append(user_data["friends"][friend]["watched"][movie]["title"])
    for i in range(len(user_data["watched"])):
        user_movie_list.append(user_data["watched"][i]["title"])
    unique_watched = set(user_movie_list) - set(friend_movie_list)
    for movie in unique_watched:
        unique_list.append({"title": movie})
    return unique_list

def get_friends_unique_watched(user_data):
    friend_movie_list = []
    user_movie_list = []
    unique_list = []
    for friend in range(len(user_data["friends"])):
        for movie in range(len(user_data["friends"][friend]["watched"])):
            friend_movie_list.append(user_data["friends"][friend]["watched"][movie]["title"])
    for i in range(len(user_data["watched"])):
        user_movie_list.append(user_data["watched"][i]["title"])
    unique_watched = set(friend_movie_list) - set(user_movie_list)
    for movie in unique_watched:
        unique_list.append({"title": movie})
    return unique_list

# wave 4
def get_available_recs(user_data):
    possible_recommendations = []
    host_list = []
    user_movie_list = []
    final_list = []
    movie_host_list = []
    recommendation_dict = {}
    for i in range(len(user_data["watched"])):
        user_movie_list.append(user_data["watched"][i]["title"])
    for i in range(len(user_data["subscriptions"])):
        host_list.append(user_data["subscriptions"][i])
    for friend in range(len(user_data["friends"])):
        for movie in range(len(user_data["friends"][friend]["watched"])):
            if user_data["friends"][friend]["watched"][movie]["host"] in host_list:
                possible_recommendations.append(user_data["friends"][friend]["watched"][movie]["title"])
                movie_host_list.append(user_data["friends"][friend]["watched"][movie]["host"])
        
    recommendations = set(possible_recommendations) - set(user_movie_list)
    if recommendations == False:
        return None
    for item in recommendations:
        i = possible_recommendations.index(item)
        final_list.append({"title": possible_recommendations[i], "host": movie_host_list[i]})
    return final_list

# wave 5
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)

    possible_recommendations = []
    user_movie_list = []
    final_list = []
    movie_genre_list = []
    recommendation_dict = {}
    for i in range(len(user_data["watched"])):
        user_movie_list.append(user_data["watched"][i]["title"])
    for friend in range(len(user_data["friends"])):
        for movie in range(len(user_data["friends"][friend]["watched"])):
            if user_data["friends"][friend]["watched"][movie]["genre"] == most_watched_genre:
                possible_recommendations.append(user_data["friends"][friend]["watched"][movie]["title"])
                movie_genre_list.append(user_data["friends"][friend]["watched"][movie]["genre"])
        
    recommendations = set(possible_recommendations) - set(user_movie_list)
    if recommendations == False:
        return None
    for item in recommendations:
        i = possible_recommendations.index(item)
        final_list.append({"title": possible_recommendations[i], "genre": movie_genre_list[i]})
    return final_list
    
# def get_rec_from_favorites(user_data):
#     possible_recommendations = []
#     user_movie_list = []
#     final_list = []
#     movie_genre_list = []
#     recommendation_dict = {}
#     for i in range(len(user_data["favorites"])):
#         user_movie_list.append(user_data["favorites"][i]["title"])
#     for friend in range(len(user_data["friends"])):
#         for movie in range(len(user_data["friends"][friend]["watched"])):
#             possible_recommendations.append(user_data["friends"][friend]["watched"][movie]["title"])
                 
#     recommendations = set(possible_recommendations) - set(user_movie_list)
#     if recommendations == False:
#         return None
#     for item in recommendations:
#         final_list.append({"title": item})
#     return final_list