def valid_str(inp):
    # is it a string
    str_stat = isinstance(inp, str)
    # is it nonempty
    str_exists = bool(inp)
    return str_stat and str_exists

def valid_rating(rating):
    # is it a number
    rating_stat = isinstance(rating, (int, float))
    if rating_stat:
        # is it in range
        lower = 0
        upper = 5
        if lower <= rating <= upper:
            return True
        else:
            return False
    return False # not a number

def create_movie(title, genre, rating):
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
    if len(user_data["watched"])> 0:
        genres = dict()
        for movie in user_data["watched"]:
            if movie["genre"] in genres:
                genres[movie["genre"]] += 1
            else:
                genres[movie["genre"]] = 1
        return max(genres, key=genres.get)
    else:
        return None

def movie_list(person):
    persons_movies = []
    for movie in person["watched"]:
        persons_movies.append(movie["title"])
    return persons_movies

def friends_watched_movies(user_data):
    friends_movie_list = []
    for friend in user_data["friends"]:
        friends_movie_list+=movie_list(friend)
    friends_movie_set = set(friends_movie_list)
    return friends_movie_set

def get_unique_watched(user_data):
    user_movies = set(movie_list(user_data))
    friends_movie_set = friends_watched_movies(user_data)
    unique_movies = user_movies - friends_movie_set
    diff_dict = []
    for movie in unique_movies:
        diff_dict.append({"title":movie})
    return diff_dict

def get_friends_unique_watched(user_data):
    user_movies = set(movie_list(user_data))
    friends_movie_set = friends_watched_movies(user_data)
    unique_movies = friends_movie_set - user_movies 
    diff_dict = []
    for movie in unique_movies:
        diff_dict.append({"title":movie})
    return diff_dict


def get_available_recs(user_data):
    # user hasn't watched but 1+ friend has
    rec_list_unfiltered = []
    for rec in get_friends_unique_watched(user_data):
        rec_list_unfiltered.append(rec["title"])
    print(rec_list_unfiltered)
    # list of subscriptions
    subs = user_data["subscriptions"]
    # pair rec with service
    movie_with_sub = []
    for movie in rec_list_unfiltered:
        for friend in user_data["friends"]:
            for watched in friend["watched"]:
                if movie == watched["title"]:
                    movie_with_sub.append([movie,watched["host"]])
    # get movies that match users subs
    print(movie_with_sub)
    recs = []
    for movie in movie_with_sub:
        if movie[1] in subs:
            entry = {"title": movie[0], "host":movie[1]}
            if entry not in recs:
                recs.append(entry)
    return recs


def get_new_rec_by_genre(user_data):
    # user hasnt watched & 1+ friends has
    unwatched = get_friends_unique_watched(user_data)
    #print("unwatched:\n", unwatched)
    # in users max genre
    genre = get_most_watched_genre(user_data)
    #print("genre:\n", genre)
    movie_in_genre = []
    for movie in unwatched:
        for friend in user_data["friends"]:
            for watched in friend["watched"]:
                #print("movie", movie, "title", watched["title"], watched["genre"])
                if movie["title"] == watched["title"] and genre == watched["genre"]:
                    entry = {"title": movie["title"],"genre": watched["genre"]}
                    if entry not in movie_in_genre:
                        movie_in_genre.append(entry)
    #print(movie_in_genre)
    return movie_in_genre

def get_rec_from_favorites(user_data):
    # unique watched from favorites
    user_favs = []
    for movie in user_data["favorites"]:
        user_favs.append(movie["title"])
    user_favs = set(user_favs)
    friends_movie_set = friends_watched_movies(user_data)
    fav_recs = user_favs - friends_movie_set
    diff_dict = []
    for movie in fav_recs:
        diff_dict.append({"title":movie})
    return diff_dict