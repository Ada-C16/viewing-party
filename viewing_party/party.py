# The goal of this project is to write code in `party.py` so that as many of the tests pass as possible.

def create_movie(title, genre, rating):
    """
    takes three parameters -title, genre and ratings. title and parameters
    expected to be strings, rating expected to be real number
    returns a dictionary movie with values as arguments passed in params
    if any param is missing function returns none

    function tests first 4 tests
    """
    movie = None
    if title and genre and rating:
        movie = {}
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    """
    takes two parameters user_data expected to be a dictionary with watched
    as key and list value, dictionary populates list values and adds 
    movie to list, funct. returns dict of userdata with updated 
    watched movies.
    """
    #watched = user_data
    #new_user_data = {}

    for data in user_data:
        user_data[data].append(movie)

    return user_data

    # for data in user_data:
    #     new_user_data["watched"] = user_data[data] 

    # new_user_data["watched"].append(movie)

    # return new_user_data


def add_to_watchlist(user_data, movie):
    """
    takes two params userdata and movie, user_data a dict and movie expected
    returns dictionary with list of watchlist as values
    """
    # updating list while looping through, fix that
    #watchlist = user_data
    #new_dict = {"watchlist":[]}

    # for data in user_data:
    #     user_data[data].append(movie)

    # return user_data

    # for data in user_data:
    #     new_dict[data] = new_dict[data].append(movie)

    # return new_dict
    # new_dict = {"watchlist":[]}

    for data in user_data:
        user_data[data].append(movie)

    return user_data

    # for data in user_data:
    #     new_dict["watchlist"] = user_data[data]

    # return new_dict
    # new_dict = {}

    # for data in user_data:
    #     new_dict["watchlist"] = user_data[data]
        
    # new_dict["watchlist"].append(movie)

    # return new_dict

def watch_movie(movie_catalogue, movie):
    """
    takes two parameters movie_catalogue dictionary with keys watched and watched
    list, updates watchedlist with movie, can be string or dict, if movie
    in watched list, movies to watched, if movie not, does nothing 
    returns updated library.
    """
    new_movie_catalogue = {}

    new_movie_catalogue["watchlist"] = movie_catalogue["watchlist"]
    new_movie_catalogue["watched"] = movie_catalogue["watched"]


    # for the_movies in range(len(movie_catalogue[""])):
    #     new_movie_catalogue["watchlist"] = the_movies
    #     #new_movie_catalogue["watched"] = movie_catalogue["watched"]
    #     movie_in_the_library = new_movie_catalogue["watchlist"][the_movies]["title"]
    #     if movie_in_the_library == movie:
    #         watched_movie = new_movie_catalogue["watchlist"].pop(the_movies)
    #         new_movie_catalogue["watched"].append(watched_movie)

    # new_movie_catalogue["watched"] += movie_catalogue["watched"]

    # return new_movie_catalogue
  

    for the_movies in range(len(new_movie_catalogue["watchlist"])):
        movie_in_the_library = new_movie_catalogue["watchlist"][the_movies]["title"]
        if movie_in_the_library == movie:
            watched_movie = new_movie_catalogue["watchlist"].pop(the_movies)
            new_movie_catalogue["watched"].append(watched_movie)

    return new_movie_catalogue


# ********* wave 2 begins ***********

def get_watched_avg_rating(user_data):
    """
    takes a dictionary of watched, values are a list of movies
    returns average rating of movies in list, if list empty returns 
    0.0
    """
    #userdata = user_data

    average_rating = 0.0
    total_rating = 0.0

    if user_data["watched"]:
        for movie in range(len(user_data["watched"])):
            total_rating += user_data["watched"][movie]["rating"]
        
        average_rating = total_rating / len(user_data["watched"]) 
    
    return average_rating

def get_most_watched_genre(watchedlist):
    """
    takes dictionary of watched list, returns
    most watched genre, in dictionary
    """
    genre_tally = {}
    highest_value = 0 
    highest_genre = None

    for i in range(len(watchedlist["watched"])):
        if watchedlist["watched"]:
            if watchedlist["watched"][i]["genre"] not in genre_tally:
                genre_tally[watchedlist["watched"][i]["genre"]] = 1
            else:
                genre_tally[watchedlist["watched"][i]["genre"]] += 1
                if genre_tally[watchedlist["watched"][i]["genre"]] > highest_value:
                    highest_value = genre_tally[watchedlist["watched"][i]["genre"]]
                    highest_genre = watchedlist["watched"][i]["genre"]

    return highest_genre

# ********* wave 3 begins ***********

def get_unique_watched(data):
    """
    takes dictionary or of two keys watched and friends
    returns list of movies in watched not in friends list
    """
    friends_watched_movie_list = []
    for i in range(len(data["friends"])):
        friends_watched_movie_list += data["friends"][i]["watched"]
    
    unique_list = []
    for i in data["watched"]:
        if i not in friends_watched_movie_list:
            unique_list.append(i)

    return unique_list

def get_friends_unique_watched(user_data):
    """
    takes dictionary or of two keys watched and friends
    returns list of movies in friends watched but not in "watched"
    does not return duplicates
    """
    friends_watched = []
    for i in range(len(user_data["friends"])):
        friends_watched  += user_data["friends"][i]["watched"]

    friends_unique_watched = []
    for i in friends_watched:
        if i not in user_data["watched"]:
            if i in friends_unique_watched:
                continue
            friends_unique_watched.append(i)
    
    return friends_unique_watched


# ********* wave 4 begins ***********
def get_available_recs(user_data):
    friends_watched = []
    for i in user_data["friends"]:
        for w in i["watched"]:
            if w not in friends_watched:
                friends_watched.append(w)


    friends_watched_titles = []
    for i in friends_watched:
        friends_watched_titles.append(i["title"])

    users_watched_titles = []
    for i in user_data["watched"]:
        users_watched_titles.append(i["title"])

    unwatched_movies = set(friends_watched_titles).difference(set(users_watched_titles))

    recs = []
    for i in friends_watched:
        if i["title"] in unwatched_movies and i["host"] in user_data["subscriptions"]:
            recs.append(i)

    return recs


# ********* wave 5 begins ***********