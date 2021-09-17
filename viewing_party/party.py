# ************   Wave 1   ************
def create_movie(title, genre, rating):
    # return a dictionary if all parameters are Truthy.
    # return None if any parameter is Falsy

    if title == None or genre == None or rating == None:
        return None

    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    return new_movie


def add_to_watched(user_data, movie):
    """
    i.e user_data = {"watched": [{"title": "Title A", "genre": "Horror", "rating": 3.5}]}
    """
    # an empty list that user has no movies to watch
    # add movie to "watched" list inside of user_data
    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    # user_data = {"watchlist": [{title: " "...}]
    #             "watched": [{title: " "...}]}

    for movie in user_data["watchlist"]:
        # {title: " "...}
        if movie["title"] == title:
            #" "
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data

    return user_data


# ************   Wave 2   ************
def get_watched_avg_rating(user_data):
    # user_data = {"watchlist": [{title: " "...}]
    #             "watched": [{title: " "...}, {"title: " ", "rating": ""}]}

    # return rating 0.0 if rating is empty
    if len(user_data["watched"]) == 0:
        return 0.0

    # return avarage rating
    sum = 0
    for movie in user_data["watched"]:

        sum += movie["rating"]

    return sum/len(user_data["watched"])


def get_most_watched_genre(user_data):

    # creating a dictionary with genre type is key and count is value
    genre_counts = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_counts:
            genre_counts[movie["genre"]] = 1
            # print(genre_counts)
        else:
            genre_counts[movie["genre"]] += 1

    # return most_watched_genre
    max_count = 0
    max_genre = None
    for genre, count in genre_counts.items():
        if count > max_count:
            max_count = count
            max_genre = genre

    return max_genre


# ************   Wave 3   ************

# movie is a dictionary of the form:
#  {"title": <str>, ...}
# user_data is a dictionary of the form:
#  {
#    "watched": [<movie>, <movie>, ...]
#    "friends": [<user_data>, <user_data>, ...]
#  }

def get_unique_watched(user_data):
    # collect friends' watched movies
    friends_movie_titles = set()
    for friends_data in user_data["friends"]:
        for movie in friends_data["watched"]:
            friends_movie_titles.add(movie["title"])

    # go through my movies and find the movies that my friends haven't watched.
    unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movie_titles:
            unique_movies.append(movie)

    return unique_movies


def get_friends_unique_watched(user_data):

    # collect the title of movies I have watched
    my_watched_movie_titles = set()
    for movie in user_data["watched"]:
        my_watched_movie_titles.add(movie["title"])

    # go through my friends movies in an output list that are not movies in my watched list
    friends_unique_movies = {}
    for friends_data in user_data["friends"]:
        for movie in friends_data["watched"]:
            if movie["title"] not in my_watched_movie_titles:
                friends_unique_movies[movie["title"]] = movie

    return friends_unique_movies.values()


# ************   Wave 4   ************

# user_data = {
#    "supscriptions": [<"Service A">] - streaming services that user has access
#    "watched": [],
#    "friends": [
#            {watched: [{"title": <"Title A">, "host": <"Service A"},
#            {watched: [{"title": <"Title B">, "host": <"Service B"} ]
# }


def get_available_recs(user_data):
    # Make a list of the titles of movies I've watched
    watched_titles = []
    for movie in user_data["watched"]:
        watched_titles.append(movie["title"])

    # Now gather friend's movies that:
    # - Are available on my servies
    # - that I haven't watched
    recommended_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["host"] in user_data["subscriptions"] and movie["title"] not in watched_titles:
                recommended_movies.append(movie)
                watched_titles.append(movie["title"])

    return recommended_movies

# ************   Wave 5   ************


"""
user_data= {
        "favorites": [],
        "watched": [
            {"title": "Title A",
            "genre": "Intrigue"
            },
            {"title": "Title B",
            "genre": "Intrigue"
            }],
        "friends": [
            {"watched": [
                    {"title": "Title D",
                    "genre": "Intrigue"}]
            },
            {"watched": [
                    {"title": "Title C",
                    "genre": "Fantasy"
                    }]
            }
        ]
    }

"""

# - add to list if user hasn't watched the movies
# - at least one friend has watched it.
# - most frequent genre


def get_new_rec_by_genre(user_data):
    # calling most watched genre function
    favorite_genre = get_most_watched_genre(user_data)

    watched_titles = []
    for movie in user_data["watched"]:
        watched_titles.append(movie["title"])

    recommended_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == favorite_genre and movie["title"] not in watched_titles:
                recommended_movies.append(movie)
                watched_titles.append(movie["title"])

    return recommended_movies


def get_rec_from_favorites(user_data):
    # add to list if movie is in user's favorite
    # movies that friends haven't watched it
    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movies:
                friends_movies.append(movie)

    recommended_movies = []
    for movie in user_data["favorites"]:
        if movie not in friends_movies:
            recommended_movies.append(movie)

    return recommended_movies
