# # Wave

# 1.create movie
# if parameters are truthy, retrurn a dict
# dict should have three key-value pairs keys: tittle, genre, and rating
def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    else: 
        movie = None
    return movie

# 2. user_data is a dict key-"watched" and val-list of dict(movie)
# (empty list means user ha no movies in watched list)
# add movie to watched list inside of user_data and return user data
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# 3. add movie(dict) to user_data indexed at "watchlist"
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# 4. if title(str) is a movie in "watchlist", 
# remove movie(dict) from "watchlist"
# and add to "watched"
# return user_data
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data


# # Wave 2

# 1. calculate avg rating for movies in "watched" within user_data(dict)
def get_watched_avg_rating(user_data):
    watched_ratings = []
    for movie in user_data["watched"]:
        watched_ratings.append(movie["rating"])
    number_watched = len(watched_ratings)
    if number_watched:
        watched_avg_rating = sum(watched_ratings)/number_watched
    else:
        watched_avg_rating = 0.0
    return watched_avg_rating

# 2. for movie in user_data["watched"] add genre as key to genres dict
#    value at genres["genre"] is +1 every time genre appears
def get_most_watched_genre(user_data):
    watched_genres = {}
    # if we've watched any movies (else return None)
    if user_data["watched"]:
        # populate watched_genres freq map
        for movie in user_data["watched"]:
                genre = movie["genre"]
                if genre in watched_genres:
                    watched_genres[genre] += 1
                else:
                    watched_genres[genre] = 1
        # find max frequency and paired genre
        max_watched_genre_freq = max(watched_genres.values())
        for genre, freq in watched_genres.items():
            if freq == max_watched_genre_freq:
                most_watched_genre = genre
        return most_watched_genre


# # Wave 3

# non-assigned helper function
def create_user_watched_set(user_data):
    user_watched_set = set()
    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])
    return user_watched_set

# non-assigned helper function
def create_friends_watched_set(user_data):
    friends_watched_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_set.add(movie["title"])
    return friends_watched_set

# 1. get user watched - friends watched and return as list of movie dicts
def get_unique_watched(user_data):
    user_watched_set = create_user_watched_set(user_data)
    friends_watched_set = create_friends_watched_set(user_data)
    
    user_unique_watched_list = []
    user_unique_watched_set = user_watched_set - friends_watched_set
    for movie in user_unique_watched_set:
        user_unique_watched_list.append({"title": movie})
    return user_unique_watched_list

# 2. get friends watched - user watched and return as list of movie dicts
def get_friends_unique_watched(user_data):
    user_watched_set = create_user_watched_set(user_data)
    friends_watched_set = create_friends_watched_set(user_data)
    
    friends_unique_watched_list = []
    friends_unique_watched_set = friends_watched_set - user_watched_set
    for movie in friends_unique_watched_set:
        friends_unique_watched_list.append({"title": movie})
    return friends_unique_watched_list


# # Wave 4

# 1. return a list of recommended movies
#    if they are not in user watched
#    if in at least one friends watched
#    if host in user's subscriptions
def get_available_recs(user_data):
    recommended_movies = []
    user_watched_set = create_user_watched_set(user_data)
    movie_rec = {}
    already_recommended = []
    # movies in friends watched
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # is movie in user watched
            if not movie["title"] in user_watched_set:
                movie_not_in_user_watched = True
            else:
                movie_not_in_user_watched = False
            # is movie host in subscriptions
            if movie["host"] in user_data["subscriptions"]:
                host_available = True
            else:
                host_available = False
            if movie_not_in_user_watched and host_available:
                if not movie["title"] in already_recommended:
                    movie_rec = {"title": movie["title"], "host": movie["host"]}
                    recommended_movies.append(movie_rec)
                    already_recommended.append(movie["title"])
    return recommended_movies


# # Wave 5

# 1. 
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    user_watched_set = create_user_watched_set(user_data)
    recommended_movies = []
    already_recommended = []
    # movies in friends watched
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # is movie in user watched
            if not movie["title"] in user_watched_set:
                movie_not_in_user_watched = True
            else:
                movie_not_in_user_watched = False
            # is movie genre most watched
            if movie["genre"] == most_watched_genre:
                matching_genre = True
            else:
                matching_genre = False
            if movie_not_in_user_watched and matching_genre:
                if not movie["title"] in already_recommended:
                    movie_rec = {"title": movie["title"], "genre": movie["genre"]}
                    recommended_movies.append(movie_rec)
                    already_recommended.append(movie["title"])
    return recommended_movies

# 2. 
def get_rec_from_favorites(user_data):
    recommended_movies = []
    # add to list if in favorites and if not in any friends' watched
    friends_watched_set = create_friends_watched_set(user_data)
    for movie in user_data["favorites"]:
        if not movie["title"] in friends_watched_set:
            movie_rec = {"title": movie["title"]}
            recommended_movies.append(movie_rec)
    return recommended_movies