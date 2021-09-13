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

