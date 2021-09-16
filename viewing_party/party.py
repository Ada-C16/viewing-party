# Helper Functions
def user_has_watched(movie, watched_movies):
    if movie in watched_movies:
        return True
    else:
        return False 
    
def in_friends_watchlist(movie, watched_by_friends):
    if movie in watched_by_friends:
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

# Wave 1
def create_movie(movie_title, genre, rating):

    if movie_title and genre and rating:
        movie_dict = {
            'title' : movie_title, 
            'genre' : genre, 
            'rating' : rating
        }
        return movie_dict
    else: 
        return None

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    add_watchlist = user_data["watchlist"]
    add_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    movies_watched = user_data["watched"]
    movies_to_watch = user_data["watchlist"]

    for movie in list(movies_to_watch):
        if title == movie["title"]:
            movies_watched.append(movie)
            movies_to_watch.remove(movie)
    return user_data


# Wave 2
def get_watched_avg_rating(user_data):
    
    avg_rating_list = [a_dict['rating'] for a_dict in user_data['watched']]

    list_length = len(avg_rating_list)
    list_total = sum(avg_rating_list)
    
    if list_length == 0:
        return float(0)
    else:
        avg_rating = list_total/list_length
        return avg_rating

def get_most_watched_genre(user_data):

    popular_genre_list = [a_dict['genre'] for a_dict in user_data['watched']]
    most_common_genre = max(popular_genre_list, key = popular_genre_list.count, default = None)
    
    return most_common_genre

# Wave 3
def get_unique_watched(user_data):
    
    friends_movies = get_friends_movies(user_data)
    friend_movie_recs = []
    for movie in user_data['watched']:
        if movie not in friends_movies:
            friend_movie_recs.append(movie)

    if len(user_data['watched']) == None:
        return 0
    else:
        return friend_movie_recs

def get_friends_unique_watched(user_data):
    friends_movies = get_friends_movies(user_data)

    user_need_to_watch_list = []
    for movie in friends_movies:
        if movie not in user_data['watched']:
            user_need_to_watch_list.append(movie)

    user_need_to_watch_list_no_dup = []
    [user_need_to_watch_list_no_dup.append(x) for x in user_need_to_watch_list if x not in user_need_to_watch_list_no_dup]
    
    return user_need_to_watch_list_no_dup

# Wave 4
def in_users_subcriptions(host, subscriptions):
    if host in subscriptions:
        return True
    else:
        return False

def get_available_recs(user_data):
    friends_movies = get_friends_movies(user_data)
    movie_recs = []

    if len(friends_movies) == 0:
        return []

    titles_of_movies_user_watched = set()
    for movie in user_data["watched"]:
        titles_of_movies_user_watched.add(movie["title"])

    for movie in friends_movies:
        if movie["title"] not in titles_of_movies_user_watched:
            if in_users_subcriptions(movie["host"], user_data["subscriptions"]):
                movie_recs.append(movie)
    return movie_recs

# Wave 5
def get_new_rec_by_genre(user_data):

    genre_list = [a_dict['genre'] for a_dict in user_data['watched']]
    most_common_genre = max(genre_list, key = genre_list.count, default = 0)
    
    friends_movies = get_friends_movies(user_data)

    titles_of_movies_user_watched = set()
    for movie in user_data["watched"]:
        titles_of_movies_user_watched.add(movie["title"])

    movie_recs = []
    for movie in friends_movies:
        if movie["title"] not in titles_of_movies_user_watched:
            if most_common_genre in movie.values():
                movie_recs.append(movie)

    movie_recs_no_dups = []
    [movie_recs_no_dups.append(x) for x in movie_recs if x not in movie_recs_no_dups]
    return movie_recs_no_dups

def get_rec_from_favorites(user_data):

    friends_movies = get_friends_movies(user_data)

    titles_of_movies_user_watched = set()
    for movie in user_data["favorites"]:
        titles_of_movies_user_watched.add(movie["title"])

    movie_recs = []
    for recommended_movies in user_data['favorites']:
        if recommended_movies not in friends_movies:
            movie_recs.append(recommended_movies)
    
    if movie_recs == False:
        return 0
    else:
        return movie_recs