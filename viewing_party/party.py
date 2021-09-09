def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] =  genre
    new_movie["rating"] = rating
    if title == True and genre == True and rating == False:
        return new_movie
    else:
        return None
    
    


def add_to_watched(user_data, movie):
    user_data["watched"] = []
    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist():
    pass

def watch_move():
    pass