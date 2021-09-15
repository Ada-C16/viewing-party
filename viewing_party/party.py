# Wave 1
def create_movie(title, genre, rating):
    # title = str, genre = str, rating = float
    movie_dict = {}
    if title and genre and rating:
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
    else:
        return None
    return movie_dict

def add_to_watched(user_data, movie_info):
    # user_data: a dictionary that contains a list of movies
        # example: {"watched": [{title: xxx, genre: xxx, rating: xxx}, {title: yyy, genre: yyy, rating: zzz}]}
    # movie: a dictionary with keys: title, genre, rating; these are inside user_data
    # movie_info = create_movie()
    user_data['watched'].append(movie_info)
    return user_data

def add_to_watchlist(user_data, movie):
    # user_data: dictionary that contains a list of movies
        # example: {'watchlist': [{title: zzz, genre: zzz, rating: zzz}, {title: aaa, genre: aaa, rating: aaa}] }
    # movie: dict with keys: title, genre, rating; these will live inside user_data
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"] # This is a list
    watched = user_data["watched"] # This is a list
    for movie in watchlist:
        if movie['title'] == title:
            watched.append(movie)
            watchlist.remove(movie)
        else:
            continue
    return user_data

# Wave 2
def get_watched_avg_rating(user_data):
    avg_rating = 0
    watched = user_data["watched"]
    if len(watched) == 0:
        return 0.0
    else:
        for movie in watched:
            avg_rating += movie["rating"]
        return avg_rating/len(watched)

def get_most_watched_genre(user_data):
    genre_dict = {}
    most_watched = 0
    most_watched_genre = " "
    watched = user_data["watched"]
    if len(watched) == 0:
        return None
    for movie in watched:
        if movie["genre"] not in genre_dict:
            genre_dict[movie["genre"]] = 1
        else: 
            genre_dict[movie["genre"]] += 1
    for genre, count in genre_dict.items():
        if count > most_watched:
            most_watched = count
            most_watched_genre = genre
    return most_watched_genre

# Wave 3
# This function consolidates friends' watched list values into one list. 
def get_movie_list_from_watched_dict(list):
    all_movies_watched_by_friends = []
    for friend_movie_list in list:
        for i in range(len(friend_movie_list["watched"])):
            popped_movie = friend_movie_list["watched"].pop()
            all_movies_watched_by_friends.append(popped_movie)
    return all_movies_watched_by_friends

def get_unique_watched(user_data):
    unique_movies = []
    watched = user_data["watched"]
    friends_list = user_data["friends"]
    friends_movie_list = get_movie_list_from_watched_dict(friends_list)
    for movie in watched:
        if movie in friends_movie_list:
            continue
        else:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    watched = user_data["watched"]
    friends_list = user_data["friends"]
    friends_movie_list = get_movie_list_from_watched_dict(friends_list)
    for movie in friends_movie_list:
        if movie in watched or movie in friends_unique_movies:
            continue 
        else:
            friends_unique_movies.append(movie)
    return friends_unique_movies

# Wave 4



def get_available_recs(user_data):
    pass
