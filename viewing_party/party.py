def create_movie(title,genre,rating):
    new_movie = {}
    empty = None
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return empty



def add_to_watched(user_data,movie):
    user_list = user_data["watched"]
    user_list.append(movie)
    return user_data


def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    watch_list = user_data["watchlist"]

    for movie in watch_list:
        if title in movie.values():
            watched_movie = watch_list.pop()
            user_data["watched"].append(watched_movie)
    return user_data