def create_movie(title, genre, rating):
    if (title) and (genre) and (rating):
        new_movie = {
            "title": title, 
            "genre": genre,
            "rating": rating
            }

        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    return user_data

def get_watched_avg_rating(user_data):
    total_rating = 0
    if len(user_data["watched"]) == 0:
        return 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"] 
    return total_rating / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_to_count_dict = {}
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_to_count_dict:
            genre_to_count_dict[movie["genre"]] = 1
        else: 
            genre_to_count_dict[movie["genre"]] += 1
    
    max_count = 0
    most_popular_genre = ""
    for genre, count in genre_to_count_dict.items():
        if count > max_count:
            max_count = count
            most_popular_genre = genre
    return most_popular_genre

# #Wave 2
def get_unique_watched(user_data):
    if len(user_data["watched"]) == 0:
        return []
    
    user_movies = set()
    for watched in user_data["watched"]:
        for title, movie_title in watched.items():
            user_movies.add((title, movie_title))
    
    friends_movies = set()
    for friends_data in user_data["friends"]:
        for watched in friends_data["watched"]:
            for title, movie_titles in watched.items():
                friends_movies.add((title, movie_titles))

    user_unique = user_movies - friends_movies
    
    uni_user_movies = []
    for movie in user_unique:
        x, y = movie
        uni_user_movies.append({x : y})

    return uni_user_movies

def get_user_movies(user_data):
    user_movies = set()
    for watched in user_data["watched"]:
        for title, movie_title in watched.items():
            user_movies.add((title, movie_title))
    return user_movies

def get_friends_movies(user_data):
    friends_movies = set()
    for friends_data in user_data["friends"]:
        for watched in friends_data["watched"]:
            for title, movie_titles in watched.items():
                friends_movies.add((title, movie_titles))
    return friends_movies 

def get_friends_unique_watched(user_data):
    user_movies = set()
    for watched in user_data["watched"]:
        for title, movie_title in watched.items():
            user_movies.add((title, movie_title))
    
    friends_movies = set()
    for friends_data in user_data["friends"]:
        for watched in friends_data["watched"]:
            for title, movie_titles in watched.items():
                friends_movies.add((title, movie_titles))

    friends_unique = friends_movies - user_movies

    uni_friends_movies = []
    for movie in friends_unique:
        x, y = movie
        uni_friends_movies.append({x : y})
    ##Why though??##
    if len(uni_friends_movies) == 0:
        return []

    return uni_friends_movies

#wave 4

#user has not watched
def user_has_watched(movie, watched_movies):
    if movie in watched_movies:
        return True
    else:
        return False 
    
    #at least 1 friend has watched it
def in_friends_watchlist(movie, watched_by_friends):
    if movie in watched_by_friends:
        return True
    else:
        return False
    #the host of the movie is a service that is a service in subscription
def in_users_subcriptions(host, subscriptions):
    if host in subscriptions:
        return True
    else:
        return False

def get_friends_movies(user_data):
    titles = set()
    friends = user_data["friends"]
    movies = []
    for friend in friends:
        for movie in friend["watched"]:
            if movie["title"] not in titles:
                movies.append(movie)
                titles.add(movie["title"])
    return movies

def get_available_recs(user_data):
    friends_movies = get_friends_movies(user_data)
    movie_recs = []

    if len(friends_movies) == 0:
        return []

    titles_of_movies_user_watched = set()
    for movie in user_data["watched"]:
        titles_of_movies_user_watched.add(movie["title"])

    for movie in friends_movies:
        if movie["title"] not in titles_of_movies_user_watched:
            if in_users_subcriptions(movie["host"], user_data["subscriptions"]):
                movie_recs.append(movie)
    return movie_recs


##wave 5
def get_new_rec_by_genre(user_data):
    friends_movies = get_friends_movies(user_data)
    
    if len(user_data["watched"]) == 0:
        return []

    if len(friends_movies) == 0:
        return []
    
    titles_of_movies_user_watched = set()
    for movie in user_data["watched"]:
        titles_of_movies_user_watched.add(movie["title"])
    
    recommended_by_genre = []
    for movie in friends_movies:
        if movie["title"] not in titles_of_movies_user_watched:
            if movie["genre"] == get_most_watched_genre(user_data):
                recommended_by_genre.append(movie)
    return recommended_by_genre

def get_rec_from_favorites(user_data):
    if len(user_data["watched"]) and len(user_data["favorites"])== 0:
        return []

    friends_movies = get_friends_movies(user_data)
    favorite_movies = []
    for movie in user_data["favorites"]:
        if movie not in friends_movies:
            favorite_movies.append(movie)
    return favorite_movies
