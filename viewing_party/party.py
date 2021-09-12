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
        # updated_data = []
        if item["title"] == title:
            user_data["watched"].append(item)
    for item in user_data["watchlist"]:
        if item in user_data["watched"]:
            user_data["watchlist"].remove(item)
    return user_data 
    # still not working, returns empty list if title not in watchlist

def get_watched_avg_rating(user_data):
    counter = 0
    total = 0
    if user_data["watched"] == []:
        avg = 0.0
    for item in user_data["watched"]:
        if item["rating"]:
            counter += 1
            total += item["rating"]
            avg = total/counter
    return avg

def get_most_watched_genre(user_data):
    pass
    count = 0
    genre_list = []
    # for item in user_data["watched"]:
        # if item["genre"] not in genre_list:
        #     genre_list.append(item[])
