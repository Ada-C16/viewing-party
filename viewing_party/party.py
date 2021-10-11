# Wave 01

"""
The create_movie function takes the information 
that is passed in to create a movie dictionary.
"""

def create_movie(title, genre, rating):
    if title and genre and rating:
        # Return a dictionary that has three key-value pairs
        # The three keys are title, genre, and rating
        movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie_dict
    else:
        return None

"""
The add_to_watched function is adding movies 
to a user's watched movie list.
"""

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

"""
The add_to_watchlist is adding movies that the user 
has not seen but wants to watch to a watchlist.
"""

def add_to_watchlist(user_data, movie):
    add_watchlist = user_data["watchlist"]
    add_watchlist.append(movie)
    return user_data

"""
The watch_movie function will identify movies 
in the watchlist that the user has seen and add
them to the watched_list and remove them from the 
watchlist.
"""

def watch_movie(user_data, title):
    movies_watched = user_data["watched"]
    movies_to_watch = user_data["watchlist"]
    remove_list = []

    for movie in movies_to_watch:
        if title == movie["title"]:
            movies_watched.append(movie)
            remove_list.append(movie)

    for movie in remove_list:
        movies_to_watch.remove(movie)

    return user_data

# Wave 02

"""
The get_watched_avg_rating function is calculating 
the average rating of all the movie the given user 
has watched.
"""

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    total_rating = 0
    avg_rating = 0
    
    if watched_list == []:
        avg_rating = 0.0
        return avg_rating
    
    for movie in watched_list:
        if movie["rating"]:
            total_rating += movie["rating"]
        else:
            total_rating += 0
    
    avg_rating = total_rating/len(watched_list)
    return avg_rating

"""
The get_most_watched_genre is going to return 
the genre that is most watched by the given user.
"""

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    
    genre_list = []
    max_genre = None
    genre_count = {}
    highest_count = 0
    
    for movie in watched_list:
        genre_list.append(movie["genre"])
    
    if genre_list == []:
        return None 

    for genre in genre_list:
        if genre not in genre_count:
            genre_count[genre] = 1
        elif genre in genre_count:
            genre_count[genre] += 1
    
    for genre, count in genre_count.items():
        if count > highest_count:
            highest_count = count
            max_genre = genre
    return max_genre

# Wave 03

"""
The get_unique_watched function returns a list of movies
that the user has watched but the user's friends have not.
"""

def get_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_list = user_data["friends"]

    friends_watched_lists = []
    unique_watch_list = []

    for friend in friends_list:
        for friend_movie in friend["watched"]:
            friends_watched_lists.append(friend_movie)
    
    for user_movie in user_watched_list:
        if user_movie not in friends_watched_lists:
            unique_watch_list.append(user_movie)
    
    return unique_watch_list

"""
The get_friends_unique_watched function returns a 
list of movies that a least one of the user's friends
has watched but the user themself has not watched. 
"""

def get_friends_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    
    friends_list = user_data["friends"]
    friends_watched_lists = []
    list_of_friends_movies = []
    no_dups = []

    user_not_watched = []

    for friend in friends_list:
        for watched_lists in friend.values():
            friends_watched_lists.append(watched_lists)
    
    for list in friends_watched_lists:
        for movie in list:
            list_of_friends_movies.append(movie)

    for movie in list_of_friends_movies:
        if movie not in no_dups:
            no_dups.append(movie)
    
    for friend_movie in no_dups:
        if friend_movie not in user_watched_list:
            user_not_watched.append(friend_movie)
    
    return user_not_watched

# Wave 04

"""
The get_available_recs function returns a list of
movies (1) that the user has not watched (2) that at 
least one of the user's friends has watched and 
(3) that has a host that is available in the user's
subscription.
"""

def get_available_recs(user_data):
    user_has_not_watched = []
    available_recs = []

    available_movies = get_friends_unique_watched(user_data)
    user_watched_list = user_data["watched"]

    for movie in available_movies:
        watched = False
        for user_movie in user_watched_list:
            if user_movie["title"] == movie["title"]:
                watched = True
        
        if watched == False:
            user_has_not_watched.append(movie)
    
    for movie in user_has_not_watched:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)
    
    return available_recs

# Wave 05 

"""
The get_new_rec_by_genre funtion returns a list of 
movies (1) that the user has not watched, (2) that
at least one of the user's friends has watched, and (3)
that has the genre of a movie that is the same as the 
user's most frequent genre.
"""

def get_new_rec_by_genre(user_data):
    freq_genre = get_most_watched_genre(user_data)
    user_not_watched = get_friends_unique_watched(user_data)
    rec_list = []

    for movie in user_not_watched:
        if movie["genre"] == freq_genre:
            rec_list.append(movie)
    
    return rec_list

"""
The get_rec_from_favorites function returns a list of 
movies that are in the user's favorite movies list that 
none of the user's friends have watched.
"""

def get_rec_from_favorites(user_data):
    user_favs = user_data["favorites"]

    if user_favs == []:
        return user_favs
    
    favorite_recs = get_unique_watched(user_data)

    return favorite_recs