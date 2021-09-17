import statistics

# Wave 1
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating,
             }
        return movie_dict
    else:
        return None


def add_to_watched(user_data, movie):
    if movie:
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = []
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    
    for movie in watchlist:
        if title in movie["title"]:
            watchlist.remove(movie)
            watched.append(movie)
            break
    
    return user_data


# Wave 2
def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    rating_sum = 0
    
    if len(watched) == 0:
        return 0
    for movie in watched:
        rating_sum += movie["rating"]  
        average_rating = rating_sum / len(watched)
    return average_rating


def get_most_watched_genre(user_data):
    most_watched = user_data["watched"]
    genres = []
    if len(most_watched) == 0:
        return None
    for movie in most_watched:
        genres.append(movie["genre"])
    return statistics.mode(genres)


# Wave 3
def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    
    friends_titles = []
    for friend in friends_watched:
        for title in friend["watched"]:
            friends_titles.append(title['title'])

    unique_watched = []

    for title in user_watched:
        if title["title"] not in friends_titles:
            unique_watched.append(title)

    return unique_watched
    
    
def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    
    user_titles = [title["title"] for title in user_watched]
    friends_unique_watched = []

    for friend in friends_watched:
        for title in friend["watched"]:
            if title["title"] not in user_titles:
                if title not in friends_unique_watched:
                    friends_unique_watched.append(title)

    return friends_unique_watched


# Wave 4
# user has not watched
def user_has_watched(movie, watched_movies):
    if movie in watched_movies:
        return True
    else:
        return False

# at least 1 friend has watched it
def in_friends_watchlist(movie, watched_by_friends):
    if movie in watched_by_friends:
        return True
    else:
        return False

# host of the movie is a service that is a service subscription
def in_users_subscriptions(host, subscriptions):
    if host in subscriptions:
        return True
    else:
        return False


def get_friends_movies(user_data):
    titles = set()
    friends = user_data["friends"]
    movies = []
    for friend in friends:
        for movie in friend["watched"]:
            if movie["title"] not in titles:
                movies.append(movie)
                titles.add(movie["title"])
    return movies


def get_available_recs(user_data):
    user_watched = user_data["watched"]
    friends_movies = get_friends_movies(user_data)
    available_recs = []

    if len(friends_movies) == 0:
        return []

    user_watched_titles = set()
    for movie in user_watched:
        user_watched_titles.add(movie["title"])

    for movie in friends_movies:
        if movie["title"] not in user_watched_titles:
            if in_users_subscriptions(movie["host"], user_data["subscriptions"]):
                available_recs.append(movie)

    return available_recs


# Wave 5
def get_new_rec_by_genre(user_data):
    # assign user_watched to watched list
    user_watched = user_data["watched"]
    # assign friends_movies to function call get_friends_movies
    friends_movies = get_friends_movies(user_data)

    # if watched list is empty
    # or if friends_movies is empty
    # return an empty list
    if len(user_data["watched"]) == 0 or len(friends_movies) == 0:
        return []

    # assign titles_of_movies_user_watched to any empty set
    user_watched_titles = set()
    # for every movie in the watched list
    for movie in user_watched:
        # add it to the user titles set
        user_watched_titles.add(movie["title"])

    # initialize an new list called new_rec_by_genre
    new_rec_by_genre = []
    # for every title in friends_movies
    for movie in friends_movies:
        # if the title is not in 
        if movie["title"] not in user_watched_titles:
            if movie["genre"] == get_most_watched_genre(user_data):
                new_rec_by_genre.append(movie)
    return new_rec_by_genre


def get_rec_from_favorites(user_data):
    # if watched list & favorites list is empty, return empty list
    if len(user_data["watched"]) and len(user_data["favorites"])== 0:
        return []

    # friends movies is the return value of get_friends_movies
    friends_movies = get_friends_movies(user_data)
    # initialize a new list, rec_from_favorites
    rec_from_favorites = []
    # for every movie in user's favorites list
    for movie in user_data["favorites"]:
        # if the movie is not in friends_movies
        if movie not in friends_movies:
            # append to rec_from_favorites list
            rec_from_favorites.append(movie)
    # return the rec_from_favorites_list
    return rec_from_favorites