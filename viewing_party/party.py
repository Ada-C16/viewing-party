def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        new_movie = {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_to_watch):
    for movie_data in user_data["watchlist"]:
        if movie_data["title"] == movie_to_watch:
            user_data["watched"].append(movie_data)
            user_data["watchlist"].remove(movie_data)
    
    return user_data

def get_watched_avg_rating(user_data):
    average_data = []

    for movie_data in user_data["watched"]:
        average_data.append(movie_data["rating"])

    if not average_data:
        return 0

    return sum(average_data)/len(average_data)
        
def get_most_watched_genre(user_data):
    most_watched = {}

    for movie_data in user_data["watched"]:
        if movie_data["genre"] not in most_watched:
            most_watched[movie_data["genre"]] = 1
        else:
            most_watched[movie_data["genre"]] += 1

    if most_watched:
        return max(most_watched, key=most_watched.get)

    return None
    
def get_unique_watched(user_data):
    unique_watched = []
    unique_watched += user_data["watched"]

    for friend_data in user_data["friends"]:
        for movie_data in friend_data["watched"]:
            if movie_data in unique_watched:
                unique_watched.remove(movie_data)

    return unique_watched

def get_friends_unique_watched(user_data):
    unique_watched = []

    for friend_data in user_data["friends"]:
        unique_watched += friend_data["watched"]
    
    for movie_data in user_data["watched"]:
        if movie_data in unique_watched:
            unique_watched.remove(movie_data)

    real_unique =[]
    [real_unique.append(x) for x in unique_watched if x not in real_unique]

    return real_unique

def get_available_recs(user_data):
    available_recommendations = []
    user_watched = []

    for user_movie_data in user_data["watched"]:
        user_watched.append(user_movie_data["title"])

    for friend_data in user_data["friends"]:
        for friend_movie_data in friend_data["watched"]:
            if friend_movie_data["title"] not in user_watched and friend_movie_data["host"] in user_data["subscriptions"] and friend_movie_data not in available_recommendations:
                available_recommendations.append(friend_movie_data)

    return available_recommendations

def get_new_rec_by_genre(user_data):
    user_fave_genre = get_most_watched_genre(user_data)
    user_watched = []

    for user_movie_data in user_data["watched"]:
        user_watched.append(user_movie_data["title"])

    new_recs = []

    for friend_data in user_data["friends"]:
        for friend_movie_data in friend_data["watched"]:
            if friend_movie_data["title"] not in user_watched and friend_movie_data["genre"] == user_fave_genre and friend_movie_data not in new_recs:
                new_recs.append(friend_movie_data)

    return new_recs
    
def get_rec_from_favorites(user_data):
    rec_faves = []

    for user_fave in user_data["favorites"]:
        rec_faves.append(user_fave)

    for friend_data in user_data["friends"]:
        for friend_movie_data in friend_data["watched"]:
            if friend_movie_data in rec_faves:
                rec_faves.remove(friend_movie_data)

    return rec_faves

    