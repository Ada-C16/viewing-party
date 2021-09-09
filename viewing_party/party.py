def create_movie(title, genre, rating):
    movie_dict = {}
    if title == True: #replace nested conditional with ands 
        if genre == True:
            if rating == True:
                movie_dict = {
                    "title" : title,
                    "genre" : genre,
                    "rating" : rating
                }
                return movie_dict
    else:
        return None



def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data



def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data



def watch_movie(user_data, title):
    if title in user_data["watchlist"]:
        #remove that from watchlist
        #add to watched list
        #return user_data dict
        user_data["watchlist"].remove(title)
        user_data["watched"].append(title)
        return user_data
    else:
        return user_data
