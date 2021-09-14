#WAVE_01
def create_movie(movie_title, genre, rating):
    new_movie = {}
    if movie_title and genre and rating != None:
        new_movie["title"]= movie_title   
        new_movie["genre"]= genre
        new_movie["rating"]= rating
        return(new_movie)
    else:
        return None

def add_to_watched(user_data, movie):
    if user_data["watched"] == []:
        movies_list = [movie]
        user_data["watched"] = movies_list

    else:
        movies_list = user_data["watched"]
        movies_list.append(movie)
        user_data["watched"]= movies_list

    updated_data = user_data
    return updated_data

def add_to_watchlist(user_data, movie):
    if user_data["watchlist"] == []:
        movies_list = [movie]
        user_data["watchlist"] = movies_list

    else:
        movies_list = user_data["watchlist"]
        movies_list.append(movie)
        user_data["watchlist"]= movies_list

    updated_data = user_data
    return updated_data

def watch_movie(user_data, title):
    watch_list = user_data['watchlist']
    viewed_list = user_data['watched']
    for movie in user_data["watchlist"]: 
        if movie["title"] == title:
            unwatched = movie["title"]
            if unwatched == title:
                watch_list.remove(movie)
                viewed_list.append(movie)
                updated_data = {"watchlist": watch_list, "watched": viewed_list}
                return updated_data
    else:
        return user_data