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
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    # user_data: dictionary that contains a list of movies
        # example: {'watchlist': 'xxx' , 'watched': 'xxx'}
    # title: string
    # if title in watchlist
    if title in watchlist.values():
        # remove that dict from watchlist key
        del title
        # add dict to watched key
        watched = f"{watched}, {title}"
        # if title not in watchlist, return user_data
    else:
        return user_data
    return user_data