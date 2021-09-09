# Wave 1 
def create_movie(title, genre, rating):
    if bool(title) == True & bool(genre) == True & bool(rating) == True:
        movie_to_watch = {
                "title" : title,
                "genre" : genre,
                "rating" : rating 
                }    
        return movie_to_watch      
    else: 
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    length_watchlist = len(user_data["watchlist"])
    for i in range(length_watchlist):
        if user_data["watchlist"][i]["title"] == title:
            movie_to_be_added = user_data["watchlist"][i]
            add_to_watched(user_data, movie_to_be_added)
            user_data["watchlist"].pop(i)
    return user_data



#main
