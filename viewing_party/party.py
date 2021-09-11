def create_movie(title, genre, rating):
    pass 
    create_movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if title and genre and rating:
      return create_movie_dict 
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
    remove_list = []
   
    for movie in movies_to_watch:
        if title == movie["title"]:
            movies_watched.append(movie)
            remove_list.append(movie)

    return user_data 