# The goal of this project is to write code in `party.py` so that as many of the tests pass as possible.

# To complete this project, use the above workflow and follow these steps:

# 1. Start with making the tests in `test_wave_01.py` pass.
# 1. Review your code in `party.py` and see if there are ways you can make the code more readable.
# 1. Then, work on making the tests in `test_wave_02.py` pass.
# 1. Review your code in `party.py`
# 1. Repeat on all test files until submission time.

# At submission time, no matter where you are, submit the project via Learn.

# 1. The first four tests are about a `create_movie()` function.

# In `party.py`, there should be a function named `create_movie`. This function should...

# - take three parameters: `title`, `genre`, `rating`
# - If those three attributes are truthy, then return a dictionary. This dictionary should...
#   - Have three key-value pairs, with specific keys
#   - The three keys should be `"title"`, `"genre"`, and `"rating"`
#   - The values of these key-value pairs should be appropriate values
# - If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`


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
    watched = user_data

    for data in watched:
        watched[data].append(movie)

    return watched

def add_to_watchlist(user_data, movie):
    """
    takes two params userdata and movie, user_data a dict and movie expected
    returns dictionary with list of watchlist as values
    """

    watchlist = user_data

    for data in watchlist:
        watchlist[data].append(movie)

    return watchlist


def watch_movie(movie_catalogue, movie):
    """
    takes two parameters movie_catalogue dictionary with keys watched and watched
    list, updates watchedlist with movie, can be string or dict, if movie
    in watched list, movies to watched, if movie not, does nothing 
    returns updated library.
    """

    movie_library = movie_catalogue

    # for the_movies in range(len(movie_library["watchlist"])):
    #     if movie_library["watchlist"][the_movies]["title"] == movie:
    #         a = movie_library["watchlist"].pop(the_movies)
    #         movie_library["watched"].append(a)

    # return movie_library

    for the_movies in range(len(movie_library["watchlist"])):
        movie_in_the_library = movie_library["watchlist"][the_movies]["title"]
        if movie_in_the_library == movie:
            watched_movie = movie_library["watchlist"].pop(the_movies)
            movie_library["watched"].append(watched_movie)

    return movie_library

# ********* wave 2 begins ***********
# janes_data = {
#     "watched": [
#         {
#             "title": "Title A",
#             "genre": "Fantasy",
#             "rating": 4.8
#         },
#         {
#             "title": "Title B",
#             "genre": "Action",
#             "rating": 2.0
#         },
#         {
#             "title": "Title C",
#             "genre": "Intrigue",
#             "rating": 3.9
#         }
#     ]
# }
def get_watched_avg_rating(user_data):
    """
    takes a dictionary of watched, values are a list of movies
    returns average rating of movies in list, if list empty returns 
    0.0
    """
    userdata = user_data

    average_rating = 0.0
    total_rating = 0.0

    if userdata["watched"]:
        for movie in range(len(userdata["watched"])):
            total_rating += userdata["watched"][movie]["rating"]
        
        average_rating = total_rating / len(userdata["watched"]) 
    
    return average_rating

def get_most_watched_genre(watchedlist):
    genre_tally = {}
    highest_value = 0 
    highest_genre = None

    for i in range(len(watchedlist["watched"])):
        if watchedlist["watched"]:
            #genre_tally = {}
            if watchedlist["watched"][i]["genre"] not in genre_tally:
                genre_tally[watchedlist["watched"][i]["genre"]] = 1
            else:
                genre_tally[watchedlist["watched"][i]["genre"]] += 1
    #             for i in genre_tally:
    #                 if genre_tally[i] > highest_value:
    #                     highest_value = genre_tally[i]
    #                     highest_genre = i
                if genre_tally[watchedlist["watched"][i]["genre"]] > highest_value:
                    highest_value = genre_tally[watchedlist["watched"][i]["genre"]]
                    #print(genre_tally)
                    highest_genre = watchedlist["watched"][i]["genre"]

    return highest_genre
#print(genre_tally)
# print(highest_value)
# print(highest_genre)