from collections import Counter #for most watched genre

sonyas_data = {
    "watched": [
        {
            "title": "Title A"
        },
        {
            "title": "Title B"
        },
        {
            "title": "Title C"
        }
    ],
    "favorites": [
        {
            "title": "Title A"
        },
        {
            "title": "Title B"
        }
    ],
    "friends": [
        {
            "watched": [
                {
                    "title": "Title B"
                }
            ]
        },
        {
            "watched": [
                {
                    "title": "Title C"
                },
                {
                    "title": "Title D"
                }
            ]
        }
    ]
}
############################################
def get_rec_from_favorites(user_data):
    recommended_movies = []
    users_favorite_movies = user_data["favorites"]
    only_user_watched_movies = get_unique_watched(user_data)
    
    for movie in users_favorite_movies:
        if movie in only_user_watched_movies:
            recommended_movies.append(movie)

    return recommended_movies


#############################################

def get_unique_watched(user_data):
    #first let's get the list of movies the user has watched
    users_movies = []
    for index in range(len(user_data["watched"])):    
        users_movies.append(user_data["watched"][index]["title"])
    
    #print(users_movies)
    

    #print(user_data["friends"][0]["watched"][0]["title"])

    friends_movies = set() #looping to fill this into a set

    friends = user_data["friends"]
    for friend in range(len(friends)):
        watched_list = friends[friend]["watched"]
        for movies in watched_list:
            for individual_title in movies:
                #print(movies[individual_title])
                friends_movies.add(movies[individual_title])
                
    #print(friends_movies)

    users_movies = set(users_movies)
    
    movies_only_user_watched = users_movies - friends_movies
    #print(movies_only_user_watched)
    
    final_movie_list_of_dictionaries = []
    for movie in movies_only_user_watched:
        final_movie_list_of_dictionaries.append({"title": movie}) 
    
    return final_movie_list_of_dictionaries


def get_new_rec_by_genre(user_data):
    #we want to get the user's most frequently watched genre (we have a function for this)

    recommended_movies = []
    friends_watched_movies = []
    users_watched_movies = user_data["watched"]

    #get user's most watched genre:
    most_watched = get_most_watched_genre(user_data)

    #get movies only the friends have watched:
    friends = user_data["friends"]
    for friend in range(len(friends)):
        watched_list = friends[friend]["watched"]
        for movies in watched_list:
            #print(movies)
            friends_watched_movies.append(movies)


    #loop through and see if the genre matches, 
    # is it a movie that is already in the recommended list? 
    # is it a movie in the users watched list?

    for movie in friends_watched_movies:
        if movie["genre"] == most_watched:
            if movie not in recommended_movies and movie not in users_watched_movies:
                recommended_movies.append(movie)

    return recommended_movies

    
        




###########################################



print(get_rec_from_favorites(sonyas_data))
