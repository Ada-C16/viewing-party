def valid_str(inp):
    ''' 
    check for valid string imput
    '''
    # is it a string
    str_stat = isinstance(inp, str)
    # is it nonempty
    str_exists = bool(inp)
    return str_stat and str_exists

def valid_rating(rating):
    '''
    check for valid numeric input (notably for rating)
    '''
    # is it a number
    rating_stat = isinstance(rating, (int, float))
    if rating_stat:
        # is it in range
        if 0 <= rating <= 5:
            return True
        else:
            return False
    return False # not a number

def create_movie(title, genre, rating):
    '''
    if valid inputs for title, genre, & rating, return movie dict
    else: return None
    '''
    if valid_str(title) and valid_str(genre) and valid_rating(rating):
        # build dict
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else:
        return None


def add_to_watched(user_data, movie):
    '''
    the value of user_data will be a dictionary with a key 
    "watched", and a value which is a list of dictionaries 
    representing the movies the user has watched
    add the movie to the "watched" list inside of user_data
    '''
    # verify 'watched' is a key in user_data
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    '''
    the value of user_data will be a dictionary with a 
    key "watchlist", and a value which is a list of 
    dictionaries representing the movies the user wants to watch
    & add the movie to the "watchlist" list inside of user_data
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    user_data: dictionary with a "watchlist" and a "watched"
    title: string that represents the title of the movie 
        the user has watched
    if movie in watchlist, remove from watchlist, add to watched
    returns user_data
    '''
    for movie in user_data["watchlist"]: 
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

def get_watched_avg_rating(user_data):
    num_movies = len(user_data["watched"])
    if num_movies > 0:
        sum = 0
        for movie in user_data["watched"]:
            sum += movie["rating"]
        avg = sum / num_movies
    else:
        avg = 0.0
    return avg


def get_most_watched_genre(user_data): 
    '''
    determines which genre is most frequently occurring
    return most frequently watched
    if not applicable, return None
    '''
    # if there are watched movies, count genre freq
    if len(user_data["watched"])> 0:
        # store counters in genres
        genres = dict()
        for movie in user_data["watched"]:
            if movie["genre"] in genres:
                genres[movie["genre"]] += 1
            else:
                genres[movie["genre"]] = 1
        # get max genre freq
        return max(genres, key=genres.get) 
    else:
        return None

def movie_list(person):
    '''
    return list of a users watched movies
    '''
    persons_movies = [movie["title"] for movie in person["watched"]]
    return persons_movies

def friends_watched_movies(user_data):
    '''
    return set of all friends movies combined
    '''
    friends_movie_list = []
    for friend in user_data["friends"]:
        friends_movie_list+=movie_list(friend)
    friends_movie_set = set(friends_movie_list)
    return friends_movie_set

def get_unique_watched(user_data):
    ''' 
    return movies user has watched but no friend has
    '''
    # get users watched movies
    user_movies = set(movie_list(user_data))
    # get friends watched movies
    friends_movie_set = friends_watched_movies(user_data)
    # get difference between user and friends
    unique_movies = user_movies - friends_movie_set
    # store difference in dict
    diff_dict = [{"title":movie} for movie in unique_movies]
    return diff_dict

def get_friends_unique_watched(user_data):
    ''' 
    return movies at least one of the user's 
    friends have watched, but the user has not watched.
    '''
    # get movies watched by user
    user_movies = set(movie_list(user_data))
    # get movies watched by friends
    friends_movie_set = friends_watched_movies(user_data)
    # get diff between friends and user
    unique_movies = friends_movie_set - user_movies 
    # store diff in dict
    diff_dict = [{"title":movie} for movie in unique_movies]
    return diff_dict


def get_available_recs(user_data):
    ''' 
    return list of recommended movies
    recommended movies are not watched by user, 
        a friend has watched it, & the user has the
        subscription service
    '''
    # user hasn't watched but 1+ friend has
    #rec_list_unfiltered = [rec["title"] for rec in get_friends_unique_watched(user_data)]
    # list of subscriptions
    subs = user_data["subscriptions"]
    # pair rec with service
    movie_with_sub = []
    for movie in get_friends_unique_watched(user_data):
        for friend in user_data["friends"]:
            for watched in friend["watched"]:
                entry = {"title": movie["title"],"host":watched["host"]}
                if movie["title"] == watched["title"] and \
                    watched["host"] in subs and \
                    entry not in movie_with_sub:
                    movie_with_sub.append(entry)
    # get movies that match users subs
    '''
    recs = []
    for movie in movie_with_sub:
        if movie[1] in subs:
            entry = {"title": movie[0], "host":movie[1]}
            if entry not in recs:
                recs.append(entry)
    '''
    return movie_with_sub

def get_new_rec_by_genre(user_data):
    ''' 
    return list of recommended movies
    recommended movies are not in users watched,
        1+ friend has seen it, it is in the users top genre
    '''
    # user hasnt watched & 1+ friends has
    unwatched = get_friends_unique_watched(user_data)
    # in users max genre
    genre = get_most_watched_genre(user_data)
    movie_in_genre = []
    for movie in unwatched:
        for friend in user_data["friends"]:
            for watched in friend["watched"]:
                if movie["title"] == watched["title"] and genre == watched["genre"]:
                    entry = {"title": movie["title"],"genre": watched["genre"]}
                    if entry not in movie_in_genre:
                        movie_in_genre.append(entry)
    return movie_in_genre

def get_rec_from_favorites(user_data):
    ''' 
    return list of recommended movies
    recommended movies are in users favs,
        none of the friends have watched it
    '''
    # unique watched from favorites
    user_favs = set([movie["title"] for movie in user_data["favorites"]])
    friends_movie_set = friends_watched_movies(user_data)
    fav_recs = user_favs - friends_movie_set
    diff_dict = [{"title":movie} for movie in fav_recs]
    return diff_dict