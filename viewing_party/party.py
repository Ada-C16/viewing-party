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