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
    
    if movie:
        user_data["watched"].append(movie)
    else:
        user_data["watched"]    
    return user_data

def add_to_watchlist():
    pass

def watch_move():
    pass