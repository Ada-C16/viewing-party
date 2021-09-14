#Wave_One part 1 
def create_movie (title, genre, rating):
    
    if title and genre and rating:
        movie_dict = {
        "title": title, 
        "genre": genre, 
        "rating": rating }
        return movie_dict 
    else:
        return None

#Wave_One part 2 
def add_to_watched(user_data, movie): 
    user_data["watched"].append(movie)
    return user_data
# add_to_watched ({"watched":[{},{},{}]}, { "title": "Title A",
#   "genre": "Horror",
#   "rating": 3.5})


#Wave_One part 3 

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data

#  add_to_watchlist({"watchlist":[{},{},{}]} ,{{
#   "title": "Title A",
#   "genre": "Horror",
#   "rating": 3.5
# }})

#Wave_One part 4 

def watch_movie (user_data, title): 

    for film in user_data["watchlist"]:
        if film["title"] == title:
        #if title["title"] in user_data["watchlist"]:

            user_data["watched"].append(film)
            user_data["watchlist"].remove(film)
    return user_data





        







watch_movie ({"watchlist":[], "watched":[]}, "title")