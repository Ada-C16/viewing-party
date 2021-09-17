def create_movie(movie_title, genre, rating):
    new_movie = { }
    if movie_title==None or genre==None or rating==None:
        return None
    new_movie['title'] = movie_title
    new_movie['genre'] = genre
    new_movie['rating'] = rating
    return new_movie

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watch_list = user_data["watchlist"]
    watch_list.append(movie)
    return user_data

def watch_movie(user_data, title):
    watch_list = user_data["watchlist"]
    watched_list = user_data["watched"]
    for movie_dict in watch_list:
        if title==movie_dict["title"]:
            watched_list.append(movie_dict)
            watch_list.remove(movie_dict)
    return user_data 

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    ratings = []
    for movie_dict in watched_list:
        ratings.append(movie_dict["rating"])
    if ratings != []:
        sum_of_ratings = sum(ratings)
        num_of_ratings = len(ratings)
        average = sum_of_ratings/num_of_ratings
    else:
        average = 0
    return average

def get_most_watched_genre(user_data):
    genres = set()
    genre_dict = {}
    watched_list = user_data["watched"]
    if watched_list == []:
        return None
    for movie_dict in watched_list:
        genres.add(movie_dict["genre"])
    genre_dict = genre_dict.fromkeys(genres, 0)
    for movie_dict in watched_list:
        genre_dict[movie_dict['genre']] += 1
    max_key = max(genre_dict, key=genre_dict.get)
    return max_key

def get_unique_watched(user_data):
    friends = user_data["friends"]
    user_watched = user_data["watched"]
    unique_watched = []
    for movie_dict in user_watched:
        unique_watched.append(movie_dict)
    for friend in friends:
        friends_list = friend["watched"]
        for movie_dict in friends_list:
            if movie_dict in unique_watched:
                unique_watched.remove(movie_dict)
    return unique_watched

def get_friends_unique_watched(user_data):
    friends = user_data["friends"]
    user_watched = user_data["watched"]
    friends_unique = []
    for friend in friends:
        for movie_dict in friend["watched"]:
            if movie_dict not in user_watched and movie_dict not in friends_unique:
                friends_unique.append(movie_dict)
    return friends_unique

def get_available_recs(user_data):
    recommended_movies = []
    friends = user_data["friends"]
    user_watched = user_data["watched"]
    user_list = []
    for movie_dict in user_watched:
        user_list.append(movie_dict['title'])
    for friend in friends:
        for movie_rec in friend["watched"]:
            if movie_rec['title'] not in user_list and movie_rec not in recommended_movies and movie_rec['host'] in user_data['subscriptions']:
                recommended_movies.append(movie_rec)
    return recommended_movies

def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    recommended_movies = []
    friends = user_data["friends"]
    user_watched = user_data["watched"]
    user_list = []
    for movie_dict in user_watched:
        user_list.append(movie_dict['title'])
    for friend in friends:
        for movie_dict in friend["watched"]:
            if movie_dict['title'] not in user_list and movie_dict not in recommended_movies and movie_dict['genre'] == genre:
                recommended_movies.append(movie_dict)
    return recommended_movies

def get_rec_from_favorites(user_data):
    faves = user_data["favorites"]
    recommended_movies = []
    friends = user_data["friends"]
    friends_list = []
    for friend in friends:
        for movie_dict in friend['watched']:
            friends_list.append(movie_dict)
    for movie_rec in faves:
        if movie_rec not in friends_list and movie_rec not in recommended_movies:
            recommended_movies.append(movie_rec)
    return recommended_movies