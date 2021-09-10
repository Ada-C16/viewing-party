def create_movie(title, genre, rating):
    new_movie = {}
    if  title == True:
        new_movie["title"] = title
    elif genre == True:
        new_movie["genre"] = genre
    elif rating == True:
        new_movie["rating"] = rating
    else:
        new_movie  is None
    return new_movie
    
    


def add_to_watched(user_data, movie):
    user_data["watched"] = []
    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    return user_data["watched"].append(movie)
    # return user_data

def add_to_watchlist():
    pass

def watch_move():
    pass