#wave 1
def create_movie(title, genre, rating): 
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]

    for i in range(len(watchlist)):
        if title in watchlist[i].values():
            movie = watchlist.pop(i)
            add_to_watched(user_data, movie)
    
    return user_data
