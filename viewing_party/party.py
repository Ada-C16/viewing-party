
def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None

    return {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie_title):
    # loop through user data watchlist
    # if movie found, move it to watched
    # if not found, do nothing
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
            break
    
    return user_data

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0

    # sum all ratings and then divide by length of the list to get the average
    sum = 0

    for movie in user_data["watched"]:
        sum += movie["rating"]

    average = sum / len(user_data["watched"])

    return average

# get user's most watched genre
def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    # iterate over user's watched movies; create a new dictionary of genres;
    # if genre already exists in the dictoinary, incremement up the value
    # if genre does not already exist in the dictionary, add it and set the value as one
    # create a most_watched variable to contain the most-watched genre and return it later
    fav_genre = None
    fav_genre_count = 0
    genre_dict = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_dict.keys():
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1

        if genre_dict[genre] > fav_genre_count:
            fav_genre = genre
            fav_genre_count = genre_dict[genre]

    return fav_genre

# get movies user has watched that friends have not
def get_unique_watched(user_data):

    set_unique_movies_watched = set()

    for movie in user_data["watched"]:
        set_unique_movies_watched.add(movie["title"])

    for friend in user_data["friends"]:
        temp_set = set()
        for movie in friend["watched"]:
            temp_set.add(movie["title"])
        set_unique_movies_watched = set_unique_movies_watched - temp_set

    list_unique_watched = [{"title": title} for title in list(set_unique_movies_watched)]

    return list_unique_watched

# return movies friends have watched that user has not
def get_friends_unique_watched(user_data):

    set_friends_unique_movies_watched = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            set_friends_unique_movies_watched.add(movie["title"])

    set_user_unique_movies_watched = set()
    for movie in user_data["watched"]:
        set_user_unique_movies_watched.add(movie["title"])

    set_friends_unique_movies_watched = set_friends_unique_movies_watched - set_user_unique_movies_watched

    list_unique_watched = [{"title": title} for title in list(set_friends_unique_movies_watched)]

    return list_unique_watched

# return movies friends have watched on services the user subscribes to
def get_available_recs(user_data):

    # first task is to get a list of movies only the users' friends have watched
    unwatched_friends_movies = get_friends_unique_watched(user_data)

    if not unwatched_friends_movies:
        return unwatched_friends_movies # return an empty list if no available movies
    
    # get a list of just titles friends have watched
    unwatched_friends_titles = [element['title'] for element in unwatched_friends_movies]

    # get a list of just the user's subscriptions
    user_subscriptions = user_data["subscriptions"]
    available_recs = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in unwatched_friends_titles and movie["host"] in user_subscriptions:
                available_recs.append(movie)
                # remove to avoid duplicates
                unwatched_friends_titles.remove(movie["title"])

    return available_recs

def get_new_rec_by_genre(user_data):

    # plan
    # initialize an empty list to store recommendations by genre
    recs_by_genre = []
    # use previously written helper function to get favorite genre
    # i believe this returns a string
    fav_genre = get_most_watched_genre(user_data)
    # use previously written helper function to get friends' movies the user has not watched
    # returns a list of dictionaries
    unwatched_friends_movies = get_friends_unique_watched(user_data)
    
    # return an empty list if no valid data available at this point
    if not unwatched_friends_movies or not fav_genre:
        return recs_by_genre

    unwatched_friends_titles = [element['title'] for element in unwatched_friends_movies]
    # iterate over friends movies using nested loops
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in unwatched_friends_titles and movie["genre"] == fav_genre:
                recs_by_genre.append(movie)
                unwatched_friends_titles.remove(movie["title"])
    
    return recs_by_genre

def get_rec_from_favorites(user_data):

    # get the list of favorites and return if empty
    user_favs = user_data["favorites"]

    if not user_favs:
        return [] # return an empty list if no user favorites

    # if not empty, convert it to a set of titles
    user_fav_titles_set = set([movie['title'] for movie in user_favs])
    # get list of user unique watched
    user_unique_watched = get_unique_watched(user_data)
    # convert it to a set of titles
    user_unique_watched_set = set([movie['title'] for movie in user_unique_watched])

    # get the intersection of favorites and movies unique to the user
    recs_for_friends = user_unique_watched_set & user_fav_titles_set
    # convert to list of dictionaries with list comprehension
    recs_for_friends = [{"title": movie} for movie in list(recs_for_friends)]

    return recs_for_friends
