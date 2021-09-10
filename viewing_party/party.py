def create_movie(title, genre, rating):
  if title and genre and rating:
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
  else: 
    new_movie = None
  return new_movie
    


def add_to_watched(user_data, movie):
    if user_data["watched"] == []:
        user_data = None
    else:
        user_data["watched"] = []
        movie = {
            "title": "Title A",
            "genre": "Horror",
            "rating": 3.5
        }
        (user_data["watched"]).append(movie)
    return user_data
    # return user_data
    # return user_data

def add_to_watchlist():
    pass

def watch_move():
    pass