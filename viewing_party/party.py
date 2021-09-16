def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating: 
        new_movie = {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    else: 
        return None
# Creates Movie Function

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
# Creates a watched list

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
# Creates a watchlist

def watch_movie(user_data, title):
    for movie_data in user_data["watchlist"]:
        if movie_data["title"] == title:
            user_data["watched"].append(movie_data)
            user_data["watchlist"].remove(movie_data)
    return user_data

def get_watched_avg_rating(user_data):
    average_data = []
    for movie_data in user_data["watched"]:
        average_data.append(movie_data["rating"])

    if not average_data:
            return 0
    else: 
        return sum(average_data)/len(average_data)

def get_most_watched_genre(user_data):
    most_genre = {}
    for movie_data in user_data["watched"]:
        current_genre = movie_data["genre"]
        if current_genre in most_genre:
            most_genre[current_genre] += 1
        else:
            most_genre[current_genre] = 1
    #alternative way
    # most_watched_num = 0
    # for key, value in most_genre:
    #     if value > 0:
    #         most_watched_num = value
    
    # for key, value in most_genre:
    #     if value == most_watched_num:
    #         return key 
    if most_genre:
        return max(most_genre, key=most_genre.get)
    else:
        return None

def get_unique_watched(user_data):
# user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
# "friends" is a list, where each item in the list is a dictionary
# This dictionary has a key "watched", which has a list of movie dictionaries
# Each movie dirctionary has a "title"
# Return a list of dictionaries that the user has watched, but none of their friends have watched
    unique_watched = []
    unique_watched += user_data["watched"]

    for friend in user_data["friends"]:
        for movie_data in friend["watched"]:
            if movie_data in unique_watched:
                unique_watched.remove(movie_data)
    return unique_watched

def get_friends_unique_watched(user_data):
    # Makes a list of what the user's friends have watched that the user has not watched
    friends_unique_watched = []

    for friend in user_data["friends"]:
        friends_unique_watched += friend["watched"]

    for user_watched in user_data["watched"]:
        if user_watched in friends_unique_watched:
            friends_unique_watched.remove(user_watched)

    true_unique = []
    for movie in friends_unique_watched:
        if movie not in true_unique:
            true_unique.append(movie)

    return true_unique

def get_available_recs(user_data):
    # Return a list of dictionaries that has "title" key and the "movie title" as value
    user_watched_titles = [] 
    rec_movies = []

    for user_movie_data in user_data["watched"]:
        user_watched_titles.append(user_movie_data["title"])

    for friend in user_data["friends"]:
        for friend_movie_data in friend["watched"]:
            if friend_movie_data["title"] not in user_watched_titles:
                if friend_movie_data["host"] in user_data["subscriptions"]:
                    if friend_movie_data not in rec_movies:
                        rec_movies.append(friend_movie_data)    

    return rec_movies

def user_watched_titles(user_data):
    # Helper Function for user's watched titles
    user_watched_titles = []
    
    for user_movie_data in user_data["watched"]:
        user_watched_titles.append(user_movie_data["title"])
    
    return user_watched_titles

def get_new_rec_by_genre(user_data):
    # Makes a list where at least one of the user's friends have watched it and
    # The genre is the same as the user's most frequent genre
    most_watched_genre = get_most_watched_genre(user_data)
    user_movies = user_watched_titles(user_data)
    if not user_movies:
        return user_movies
    rec_movies = []
    
    for friend_movie_data in user_data["friends"]:
        for movie_data in friend_movie_data["watched"]:
            if movie_data["title"] not in user_movies:
                if movie_data["genre"] in most_watched_genre:
                    if movie_data["title"] not in user_movies:
                        if movie_data not in rec_movies:
                            rec_movies.append(movie_data)
                    
    return rec_movies

def get_rec_from_favorites(user_data):
    # Makes a list of recommendations if the movie is a user's favorite and if none of their friends have watched it
    favorite_movies = []
    friends_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for user_movie in user_data["favorites"]:
        if user_movie not in friends_watched:
            if user_movie not in favorite_movies:
                favorite_movies.append(user_movie)

    return favorite_movies