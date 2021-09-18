
#Thank you for the patience and understanding!

movies = []
watchlist =[]
watched = []



def create_movie(movie_title, genre, rating):
    #create_movie_no_title_returns_none
    #create_movie_no_genre_returns_none
    #create_movie_no_genre_returns_none

    if (movie_title == None) or (genre == None) or (rating == None):
        return None 

    else:
        new_movie = {}
        new_movie["title"] = movie_title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie

def add_to_watched(user_data, movie):
    #adds_movie_to_watched

    user_data["watched"].append(movie)
    watched.append(user_data)
    return user_data
   

def add_to_watchlist(user_data, movie):
    #adds_movie_to_user_watchlist

    user_data['watchlist'].append(movie)
    watchlist.append(user_data)
    return user_data


def watch_movie(user_data, title):    
    #adds_movie_to_user_watched
    #moves_movie_from_watchlist_to_empty_watched
    #moves_movie_from_watchlist_to_watched
    #does_nothing_if_movie_not_in_watchlist

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)


    if user_data["watched"] == []:
        user_data["watched"].append(movie)

    return user_data


#WAVE 2

def get_watched_avg_rating(user_data):
    #calculates_watched_average_rating
    #returns_zero_for_empty_list

    if len(user_data["watched"]) == 0:
        return 0

    else:
        ratings = []
        for movie in user_data["watched"]:
            ratings.append(movie["rating"])
        average = sum(ratings)/len(ratings)
        return average


def get_most_watched_genre(user_data):    
    #eturns_most_frequent_genre_from_list   
    #returns_most_frequent_genre_from_list_even_when_alphabetically_smaller
    #returns_None_if_empty_watched


    genres_watched = []

    if len(user_data["watched"]) == 0:
        return None

    for movie in user_data["watched"]:
        genres_watched.append(movie["genre"])

    freq = {}

    for genre in genres_watched:
        if not genre in freq:
            freq.update({genre:1})
        else:
            freq[genre] += 1

    popular_genre =  max(freq, key=freq.get)
 
    return popular_genre

#WAVE 3

def get_unique_watched(user_data):

    #returns_list_of_movies_in_amandas_data_absent_from_their_friends_data
    #returns_empty_list_when_amandas_movies_are_all_in_her_friends_movies

    amandas_unique_movies = []
    all_friends_movies = []

    for movie in user_data["watched"]:
        amandas_unique_movies.append(movie)

    for movie_list in user_data["friends"]:
        for movie in movie_list["watched"]:
            all_friends_movies.append(movie)

    for movie in all_friends_movies:
        if movie in amandas_unique_movies:
            amandas_unique_movies.remove(movie)

    return amandas_unique_movies


def get_friends_unique_watched(user_data):
    #returns_list_of_movies_amanda_has_not_watched_and_friends_have_but_does_not_include_two_of_the_same_movie
    #returns_list_of_movies_amanda_has_not_watched_and_friends_have_with_only_one_friend
    #returns_empty_list_when_amanda_has_seen_all_movies_their_friend_has_seenpyt

    amandas_unique_movies = []
    friends_unique_movies = []

    for movie in user_data["watched"]:
        amandas_unique_movies.append(movie)

    for movie_list in user_data["friends"]:
        for movie in movie_list["watched"]:
            if movie not in friends_unique_movies:
                friends_unique_movies.append(movie)

    for movie in amandas_unique_movies:
        if movie in friends_unique_movies:
            friends_unique_movies.remove(movie)

    return friends_unique_movies

#WAVE 4

def get_available_recs(user_data):

    #returns_appropriate_recommendations_for_valid_input():
    #doesnt_recommend_watched_movie
    #returns_nothing_if_all_watched
    #returns_empty_list_for_valid_input_with_no_intersection_in_subscriptions

    recommendations = []

    amandas_subs = []
    amandas_watched = []

    friends_watched = []
    friends_watched_on_amandas_subs = []


    for subscription in user_data["subscriptions"]:
        amandas_subs.append(subscription)

    for movie in user_data["watched"]:
        amandas_watched.append(movie["title"])
    
    for friend in user_data["friends"]:

        for movie in friend["watched"]:
            friends_watched.append(movie)

            if movie not in recommendations:

                if movie["host"] in user_data["subscriptions"]:
                    friends_watched_on_amandas_subs.append(movie)

                    if movie["title"] not in amandas_watched:

                        if movie["title"] not in recommendations:
                            recommendations.append(movie)

    return recommendations
    
    
#WAVE 5

def get_new_rec_by_genre(user_data):

    #returns_appropriate_recommendations_for_large_amount_of_valid_input
    #doesnt_return_duplicate_recommendations_if_watched_by_multiple_friends
    #returns_empty_list_when_sonyas_watched_list_is_empty
    #returns_empty_list_when_friends_watched_lists_are_empty

    recommendations = []
    amandas_genre_watched = []
    friends_genre_watched = []

    genre = get_most_watched_genre(user_data)
    
    for movie in user_data["watched"]:
        if movie["genre"] == genre:
            amandas_genre_watched.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == genre:
                friends_genre_watched.append(movie)
    
    for movie in friends_genre_watched:
        if movie not in amandas_genre_watched:
            if movie not in recommendations:
                recommendations.append(movie)

    print(recommendations)
    return recommendations
   
def get_rec_from_favorites(user_data):
    #returns_empty_list_when_sonya_has_no_favorites
    #returns_expected_list_from_valid_input

    recommendations = []

    if user_data["favorites"] == []:
        return []

    for movie in user_data["watched"]:
        recommendations.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in recommendations:
                recommendations.remove(movie)
    
    print(recommendations)
    return recommendations