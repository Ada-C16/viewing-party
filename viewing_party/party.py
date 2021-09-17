#wave 1

def create_movie(title, genre, rating):
    if title ==  None:
        return None
    if genre == None:
        return None
    if rating == None:
        return None
    else:
        movie = {"title": title, "genre": genre, "rating": rating}
        return movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            user_data['watchlist'].remove(movie)
            user_data["watched"].append(movie)
        if user_data['watched'] == []:
            user_data["watched"].append(movie)

    return user_data

#wave 2 pt 1 

def get_watched_avg_rating(user_data): 
    if len(user_data["watched"]) == 0:
        return 0 
    else:
        ratings = []
        for movie in user_data['watched']:
            ratings.append(movie["rating"])
        average = sum(ratings)/len(ratings)
        return average 

 # wave 2 pt 2
 
def get_most_watched_genre(user_data):
    genres_watched = []

    if len (user_data["watched"]) == 0:
        return None

    for movie in user_data["watched"]:
        genres_watched.append(movie["genre"])

    freq = {}

    for genre in genres_watched:
        if not genre in freq:
            freq.update({genre:1})
        else:
            freq[genre] += 1 

    popular_genre = max(freq, key = freq.get)

    return popular_genre

#wave 3 pt 1

def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    friend_titles = []
    unique = []
    for friend in friends_watched:
        for title in friend["watched"]:
            friend_titles.append(title["title"])
    for title in user_watched:
        if title['title'] not in friend_titles:
            unique.append(title)
    return unique 

#wave 3 pt 2

def get_friends_unique_watched(user_data):
    unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not is_movie_in_list(user_data["watched"], movie) and not is_movie_in_list(unique_movies, movie):
                unique_movies.append(movie)
    return unique_movies

# wave 4 

def get_available_recs(user_data):
    host_list = []
    user_subscriptions = user_data["subscriptions"]
    rec = []
    friends_unique = get_friends_unique_watched(user_data)
    for movie in friends_unique:
        if movie["host"] in user_subscriptions:
            rec.append(movie)
        return rec


# #wave 5 pt1

def get_new_rec_by_genre(user_data):
    fav = get_most_watched_genre(user_data)
    friends_unique = get_friends_unique_watched(user_data)
    rec =[]
    for movie in friends_unique:
        if movie["genre"] == fav and not is_movie_in_list(rec, movie):
            rec.append(movie)
    return rec 

# wave 5 pt 2

def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    favorites = user_data['favorites']
    return [movie for movie in unique_watched if movie in favorites]

# helper

def is_movie_in_list(list, movie): 
    for item in list:
        if item["title"] == movie["title"]:
            return True
        return False 