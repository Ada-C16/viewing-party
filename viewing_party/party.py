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

def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
    else:
        user_data["watchlist"]
    return user_data


def watch_movie(user_data, title): # still working on this for 1 test
    
    for item in user_data["watchlist"]:
        if not title:
            user_data = user_data["watchlist"].copy()
        if title:
            change = user_data["watchlist"].pop()
            user_data["watched"].append(change)
        # else:
        #     user_data = user_data["watchlist"].copy()
        # if title not in user_data["watchlist"]:
        #     user_data
    return user_data