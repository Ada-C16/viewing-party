# wave01

def create_movie(title, genre, rating):
    # creates a dictionary with information on the movie entered
    if bool(title and genre and rating) == False:
        return None
    
    movie = dict()
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    # adds a movie to a user's watched list
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    # adds a movie (dict) to the user's watchlist
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    # removes movie dict from watchlist and adds it to watched
    for i in range(len(user_data["watchlist"])):
        current_movie = user_data["watchlist"][i]
        if current_movie["title"] == title:
            user_data["watchlist"].remove(current_movie)
            user_data["watched"].append(current_movie)
    return user_data

# wave02

def get_watched_avg_rating(user_data):
    # takes ratings from user_data's watched list of movie dicts and takes the average
    avg_rating = 0.0
    rating_sum = 0
    for i in range(len(user_data["watched"])):
        rating_sum += user_data["watched"][i]["rating"]
    try:
        avg_rating = rating_sum / len(user_data["watched"])
    except ZeroDivisionError:
        return avg_rating
    return avg_rating

def get_most_watched_genre(user_data):
    # calculates which genre appears most frequenly in watched and returns it
    genre_frequencies = {}
    for i in range(len(user_data["watched"])):
        if user_data["watched"][i]["genre"] not in genre_frequencies:
            genre_frequencies[user_data["watched"][i]["genre"]] = 1
        else:
            genre_frequencies[user_data["watched"][i]["genre"]] += 1
    if genre_frequencies != {}:
        most_watched_genre = max(genre_frequencies, key = lambda genre : genre_frequencies[genre])
        return most_watched_genre
    else:
        return None

# wave03

def get_unique_watched(user_data):
    # determines which movies the user has seen that friends have not and returns a list of them
    all_friends_watched = get_all_friends_watched_no_duplicates(user_data)
    in_common_watched = []
    unique_watched = []
    # makes a list of the movie dicts the friends have watched that user has also watched
    for i in range(len(user_data["watched"])):
        for j in range(len(all_friends_watched)):
            if user_data["watched"][i]["title"] == all_friends_watched[j]["title"]:
                in_common_watched.append(user_data["watched"][i])
    # removes the movie dicts friends and user have in common
    unique_watched = user_data["watched"]
    for movie in in_common_watched:
        unique_watched.remove(movie)
    return unique_watched
    
def get_friends_unique_watched(user_data):
    all_friends_watched = get_all_friends_watched_no_duplicates(user_data)
    in_common_watched = []
    friend_unique_watched = []
    # makes a list of the movie dicts the friends have watched that user has also watched
    for i in range(len(user_data["watched"])):
        for j in range(len(all_friends_watched)):
            if user_data["watched"][i]["title"] == all_friends_watched[j]["title"]:
                in_common_watched.append(all_friends_watched[j])
    # removes the movie dicts friends and user have in common  
    friend_unique_watched = all_friends_watched
    for movie in in_common_watched:
        friend_unique_watched.remove(movie)
    return friend_unique_watched

# wave04

def get_available_recs(user_data):
    available_recs = []
    if get_friends_unique_watched(user_data):
        all_recs = get_friends_unique_watched(user_data)
    for movie in all_recs:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)
    return available_recs

# wave 05

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    possible_recs = get_friends_unique_watched(user_data)
    recs_by_genre = []
    for movie in possible_recs:
        if movie["genre"] == most_watched_genre:
            recs_by_genre.append(movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    recs_from_favorites = []
    all_friends_watched = get_all_friends_watched_no_duplicates(user_data)
    for i in range(len(user_data["favorites"])):
        if user_data["favorites"][i] not in all_friends_watched:
            recs_from_favorites.append(user_data["favorites"][i])
    return recs_from_favorites

def get_all_friends_watched_no_duplicates(user_data):
    # makes a list of the movie dicts the friends have watched, removing duplicates
    all_friends_watched = []
    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            if user_data["friends"][i]["watched"][j] not in all_friends_watched:
                all_friends_watched.append(user_data["friends"][i]["watched"][j])
    return all_friends_watched