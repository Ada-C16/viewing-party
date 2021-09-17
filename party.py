import statistics

def create_movie(title, genre, rating):
#if all reqs are there then add it to the dict
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie


def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
# if they've seen it, get it off the watcvhlist, and add it to "watched" 
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data


## WAVE 2 ##

def get_watched_avg_rating(user_data):
# #this ones ina dictionary, 
# # bitch  dont forget youre missing to return if the rating is 0.. causing 2 errors because\
#  stats needs at least one parameter entered    
    ratings = [movie["rating"]for movie in user_data["watched"]]
    if len(ratings) != 0:
        avg_rating = statistics.mean(ratings) 
        return avg_rating
    else: 
        return 0.0
  
def get_most_watched_genre(user_data):
    genre = [movie["genre"]for movie in user_data["watched"]]
    if len(genre) != 0:
        most_watched_genre = statistics.mode(genre)
        return most_watched_genre
    

## WAVE 3 ##

#  I had to make a helper function... 
def find_movies_watched(user_data):
    user_watched = [movie["title"] for movie in user_data["watched"]]
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie["title"])

    return user_watched, friends_watched


def get_unique_watched(user_data):
    user_movies, friend_movies = find_movies_watched(user_data)
    user_unique_movies = set(user_movies) - set(friend_movies)
    
    return [{"title": movie} for movie in user_unique_movies]

def get_friends_unique_watched(user_data):

    user_movies, friend_movies = find_movies_watched(user_data)
    friend_unique_movies = set(friend_movies) - set(user_movies)
    
    return [{"title": movie} for movie in friend_unique_movies]



## WAVE  4 ##
##CAN YOU REFACTOR ? 

def get_available_recs(user_data):
    """
    returns list of movie dictionaries the user has not watched but has the subscription for
    """
    recommendations = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title, host = movie["title"], movie["host"]
            rec = {"title": title, "host": host}
            if title not in find_movies_watched(user_data)[0] and host in user_data["subscriptions"] and rec not in recommendations:
                recommendations.append(rec)

    return recommendations


## WAVE 5 ##
# AGAIN, CAN YOU REFACTOR? WHAT IS THIS? O(n^3,0000000th power) 
def get_new_rec_by_genre(user_data):
    top_genre = get_most_watched_genre(user_data)
    recommendations =  []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title, genre = movie["title"], movie["genre"]
            rec = {"title": title, "genre": genre}
           
            if title not in find_movies_watched(user_data)[0] and genre == top_genre  and rec not in recommendations:
                recommendations.append(rec)

    return recommendations


def get_rec_from_favorites(user_data):
    recommendations = []

    for movie in get_unique_watched(user_data):
        if movie in user_data["favorites"]:
            recommendations.append(movie)
    
    return recommendations























