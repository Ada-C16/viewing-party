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

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    add_watchlist = user_data["watchlist"]
    add_watchlist.append(movie)
    return user_data

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

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    total_rating = 0
    num_ratings = 0
    avg_rating = 0
    
    if watched_list == []:
        avg_rating = 0.0
        return avg_rating
    
    for movie in watched_list:
        if movie["rating"]:
            total_rating += movie["rating"]
            num_ratings += 1
        else:
            total_rating += 0
            num_ratings += 1
    
    avg_rating = total_rating/num_ratings
    return avg_rating

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
        else:
            pass
    return max_genre

def get_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    
    friends_list = user_data["friends"]
    friends_watched_lists = []
    list_of_friends_movies = []
    
    unique_watch_list = []

# Isolate and extract lists/dicts

    for friend in friends_list:
        for watched_lists in friend.values():
            friends_watched_lists.append(watched_lists)
    
    for list in friends_watched_lists:
        for movie in list:
            list_of_friends_movies.append(movie)
    
    for user_movie in user_watched_list:
        if user_movie not in list_of_friends_movies:
            unique_watch_list.append(user_movie)
        else:
            pass
    
    return unique_watch_list

def get_friends_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    
    friends_list = user_data["friends"]
    friends_watched_lists = []
    list_of_friends_movies = []
    no_dups = []

    user_not_watched = []

# Isolate and extract lists/dicts

    for friend in friends_list:
        for watched_lists in friend.values():
            friends_watched_lists.append(watched_lists)
    
    for list in friends_watched_lists:
        for movie in list:
            list_of_friends_movies.append(movie)

    for movie in list_of_friends_movies:
        if movie not in no_dups:
            no_dups.append(movie)
        else:
            pass
    
    for friend_movie in no_dups:
        if friend_movie not in user_watched_list:
            user_not_watched.append(friend_movie)
        else:
            pass
    
    return user_not_watched

def get_available_recs(user_data):
    user_watched_list = user_data["watched"]
    user_watched_titles = []
    friends_list = user_data["friends"]
    friends_watched_lists = []
    list_of_friends_movies = []
    no_dups = []
    watched = None
    user_not_watched = []
    available_recs = []

# Isolate and extract lists/dicts

    for friend in friends_list:
        for watched_lists in friend.values():
            friends_watched_lists.append(watched_lists)
    
    for list in friends_watched_lists:
        for movie in list:
            list_of_friends_movies.append(movie)

    for movie in list_of_friends_movies:
        if movie not in no_dups:
            no_dups.append(movie)
        else:
            pass
    
    for movie in no_dups:
        watched = False
        for user_movie in user_watched_list:
            if user_movie["title"] == movie["title"]:
                watched = True
        if watched == False:
            user_not_watched.append(movie)
    
    for movie in user_not_watched:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)
    
    return available_recs