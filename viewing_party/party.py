import statistics

# Wave 1
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating,
             }
        return movie_dict
    else:
        return None


def add_to_watched(user_data, movie):
    if movie:
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = []
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    


# def watch_movie(user_data,title): 
#     for i,d in enumerate(user_data['watchlist']):
#        if d['title'] == title:
#           user_data['watched'].append(d)
#           del user_data['watchlist'][i]      
#     return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    
    for movie in watchlist:
        if title in movie["title"]:
            watchlist.remove(movie)
            watched.append(movie)
            break
    
    return user_data


# Wave 2
def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    rating_sum = 0
    
    if len(watched) == 0:
        return 0
    for movie in watched:
        rating_sum += movie["rating"]  
        average_rating = rating_sum / len(watched)
    return average_rating


def get_most_watched_genre(user_data):
    most_watched = user_data["watched"]
    genres = []
    if len(most_watched) == 0:
        return None
    for movie in most_watched:
        genres.append(movie["genre"])
    return statistics.mode(genres)


# Wave 3
def get_unique_watched(user_data):
    pass





def get_friends_unique_watched(user_data):
    pass



# Wave 4

# Wave 5
def get_new_rec_by_genre(user_data):
    pass



