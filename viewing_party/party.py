def create_movie(movie_title, genre, rating):
    if movie_title is None:
        return None
    if genre is None:
        return None
    if rating is None:
        return None
    movie = {}
    movie["title"] = movie_title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for item in user_data["watchlist"]:
        if title == item["title"]:
            user_data["watched"].append(item)
            user_data["watchlist"].remove(item)
    return user_data    

def get_watched_avg_rating(user_data):
    if user_data["watched"] == []:
        avg_rating = 0.0
    else:
        sum_score = 0.0
        for item in user_data["watched"]:
            sum_score += item["rating"]
        avg_rating = sum_score/len(user_data["watched"])
    return avg_rating
    # user_data ={"watched": [{"genre": "comedy"},{},]}
    
def get_most_watched_genre(user_data):
    if user_data["watched"] == []:
        return None
    genre_type = {}
    for item in user_data["watched"]:
        if item["genre"] in genre_type:
            genre_type[item["genre"]] += 1
        else:
            genre_type[item["genre"]] = 1
    return max(genre_type, key=genre_type.get)

def get_unique_watched(user_data):
    friends_watched_title = []
    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched_title.append(movie["title"])
    userwatched_friendsnot = []
    for item in user_data["watched"]:
        if not item["title"] in friends_watched_title:
            userwatched_friendsnot.append(item)
    return userwatched_friendsnot
    # genre_type = {
    #     "action":2
    #     "love": 1
    # }
    # movie = {"title": xxx, 
    #           "host": service   
    #           }
    # user_data={
    #     "watchlist" : [{movie}, {movie}, {movie}]
    #     "watched" : [{movie}, {movie}, {movie}]
    #     "friends" : [{"watched": [{movieA}, {movieB}, {movieC}]},
    #                   {"watched": [{movieA}, {movieB}, {movieC}]},
    #                   {"watched": [{movieA}, {movieB}, {movieC}]},
    #                    ],
    #     "subscritions": [service, service, service]
    #      "favorites" : [{movie}, {movie}, {movie}]
def get_friends_unique_watched(user_data):
    friends_watched_movie = []
    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched_movie.append(movie)
    user_watched_title = []
    for item in user_data["watched"]:
        user_watched_title.append(item["title"])
    friends_watched_movie_no_duplicates = []
    for item in friends_watched_movie:
        if item not in friends_watched_movie_no_duplicates:
            friends_watched_movie_no_duplicates.append(item)
    
    friendswatched_usernot = []
    for item in friends_watched_movie_no_duplicates:
        if not item["title"] in user_watched_title:
            friendswatched_usernot.append(item)
    return friendswatched_usernot
    
def get_available_recs(user_data):
    rec_movies_to_user = []
    friendswatched_usernot = get_friends_unique_watched(user_data)
    for item in friendswatched_usernot:
        if item.get("host") in user_data["subscriptions"]:
            rec_movies_to_user.append(item)
    return rec_movies_to_user

def get_new_rec_by_genre(user_data):
    rec_movies_by_genre = []
    friendswatched_usernot = get_friends_unique_watched(user_data)
    most_freq_genre = get_most_watched_genre(user_data)
    for item in friendswatched_usernot:
        if item["genre"] == most_freq_genre:
            rec_movies_by_genre.append(item)
    return rec_movies_by_genre

def get_rec_from_favorites(user_data):
    rec_movies_by_fav =[]
    userwatched_friendsnot = get_unique_watched(user_data)
    for item in user_data["favorites"]:
        if item in userwatched_friendsnot:
            rec_movies_by_fav.append(item)
    return rec_movies_by_fav




