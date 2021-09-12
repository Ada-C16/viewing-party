def create_movie(title, genre, rating):        
    if title and genre and rating:
        movie_dict ={}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    elif not title or genre or rating:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return(user_data)

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return(user_data)

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

    return user_data

def get_watched_avg_rating(user_data):
    avg_rating = 0.0

    if len(user_data["watched"]) > 0:
        sum_of_ratings = 0.0
        for movie in user_data["watched"]:
            sum_of_ratings += movie["rating"]
        avg_rating = sum_of_ratings / len(user_data["watched"])

    return avg_rating

def get_most_watched_genre(user_data):
    # create a variable to contain the most watched genre
    most_watched_genre = None

    # create a dictionary to hold stats on all the genres the 
    # user has watched
    most_watched_genre_stat_dict = {}
    
    # iterate thru the list of watched movies and add value (num of watched) 
    # key (genre of movie) pair to most_watched_genre_stat_dict
    for movie_dict in user_data["watched"]:  
        if movie_dict["genre"] in  most_watched_genre_stat_dict:
            most_watched_genre_stat_dict[movie_dict["genre"]] += 1
        else:
            most_watched_genre_stat_dict[movie_dict["genre"]] = 1

    # determine the most watched genre and assign it to most_watched_genre
    if len(user_data["watched"]):
        most_watched_genre = max(most_watched_genre_stat_dict, key=most_watched_genre_stat_dict.get)

    # return the most watched genre
    return most_watched_genre

def get_unique_watched(user_data):
    # create list to host dictionaries of movies that only the user has watched
    user_unique_watched = []

    # create list of strings of movie titles that friends have watched
    friends_watched_movie_titles = []

    # iterate through the movie dictionaries that friends have watched
    # and add the titles to a the friends_watched_movie_titles list 
    for i in range(0, len(user_data["friends"])):
        for movie in user_data["friends"][i].get("watched"):
            friends_watched_movie_titles.append(movie["title"])

    # iterate through the movies that the user has watched.
    # if the title of a movie the user has watched is not in 
    # the friends_watched_movie_titles list add the movie dictionary 
    # to the user_unique_watched list
    for user_movie in user_data["watched"]:
        if user_movie.get("title") not in friends_watched_movie_titles:
            user_unique_watched.append(user_movie)

    # return the list of movie dictionaries representing movies only
    # the user has watched
    return user_unique_watched

def get_friends_unique_watched(user_data):
    # create list to host dictionaries of movies that the user's friends 
    # have watched
    friends_unique_watched_list = []
    
    # create list of strings of movie titles that the user has watched
    user_watched_movie_titles = []

    # create list of strings of movie titles that a user's friend has watched
    friend_watched_movie_titles = []

    # iterate through the movie dictionaries that the user has watched
    # and add the titles to a the user_watched_movie_titles list
    for movie_dict in user_data["watched"]:
        user_watched_movie_titles.append(movie_dict.get("title"))

    # check that the user has friends
    if user_data["friends"]:
    # iterate through the movies that the user's friends have watched.
    # if the title of a movie the user's friends have watched is not in 
    # the user_watched_movie_titles list add the movie dictionary 
    # to the friends_unique_watched list
        for i in range(0, len(user_data["friends"])):
            for movie_dict in user_data["friends"][i]["watched"]:
                if movie_dict["title"] not in user_watched_movie_titles and movie_dict["title"] not in friend_watched_movie_titles:
                    friends_unique_watched_list.append(movie_dict)
                    friend_watched_movie_titles.append(movie_dict["title"])

    # return the list of movie dictionaries representing movies only
    # the user has watched
    return friends_unique_watched_list

def get_available_recs(user_data):
    # create a list of movie dictionaries for movies that the user 
    # has not seen but a friend has seen, and that the user has access 
    # to aka the movie's host is in the user's subscriptions list 
    movie_recs = []

    # iterate through movies that only the user's friends have seen
    # check if the user has access to the movie's host
    # check if the movie has already been added to the rec list
    # if passes both checks add the movie to the rec list
    for movie_dict in get_friends_unique_watched(user_data):
        if movie_dict["host"] in user_data["subscriptions"]: 
                movie_recs.append(movie_dict)

    # return list of dictionaries reccomending movies
    return movie_recs

def get_new_rec_by_genre(user_data):
    # create list of movie dictionaries of movies that the user
    # has not seen, but a friend has, that are in the user's top
    # genre
    recs_by_genre_list = []

    # iterate through movies that the user has not seen but 
    # friends have seen
    # check if the movie's genre is the user's top genre
    # if the movie passes the check add it to the recs_by_genre_list
    for movie_dict in get_friends_unique_watched(user_data):
        if movie_dict["genre"] == get_most_watched_genre(user_data):
            recs_by_genre_list.append(movie_dict)
    
    # return list of movie recs
    return recs_by_genre_list

def get_rec_from_favorites(user_data):
    # create a list of movie dictionaries of the user's fav
    # movies. aka movies in the user's "favorites" list that
    # none of their friends have watched
    recs_from_favorites_list = []

    # iterate through the user's favorite movies
    # check to see if any of the user's friends have seen it
    # if a movie passes the check add it to the recs_from_favorites_list
    for movie_dict in user_data["favorites"]:
        if movie_dict in get_unique_watched(user_data):
            recs_from_favorites_list.append(movie_dict)
    
    #return list of movie dictionaries for user's fav movie recs
    return recs_from_favorites_list

# ************************************************************* ~
# pytest tests/test_wave_01.py
# pytest tests/test_wave_02.py
# pytest tests/test_wave_03.py
# pytest tests/test_wave_04.py
# pytest tests/test_wave_05.py

# When you need to save changes and add them to github:
# Add all changed files  git add .
# Commit changes git commit -m "useful message about the change"
# Push changed files to github git push