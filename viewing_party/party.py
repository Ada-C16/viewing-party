# W A V E  1
def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating
            }
        return new_movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title): 
    watch_list = user_data["watchlist"] 
    watched = user_data["watched"]

    #if title: #in movie["title"] :
    for movie in watch_list:
        if title in movie["title"]:
            watch_list.remove(movie)
            watched.append(movie)
    return user_data




# W A V E  2
def get_watched_avg_rating(user_data):
    watched = user_data["watched"] 
    total_rating = 0
    if len(watched) == 0:
        return 0
    for movie in watched:
            total_rating += movie["rating"]
    avg_rating = total_rating/len(watched)
    return avg_rating
        

def get_most_watched_genre(user_data):
    watched = user_data["watched"] 
    genre_count_dict = {}
    if len(watched) == 0:
        return None
    for movie in watched:
        if movie["genre"] not in genre_count_dict:
            genre_count_dict[movie["genre"]] = 1
        else:
            genre_count_dict[movie["genre"]] += 1

    # to return which genre is most frequently occurring from the above genre_count_dict 
    max_count = 0
    most_watched_genre = ""
    for genre, count in genre_count_dict.items():
        if count > max_count:
            max_count = count
            most_watched_genre = genre
    return most_watched_genre 





# W A V E  3
def get_unique_watched(user_data):
    # if len(user_data["watched"]) == 0:
    #     return []
    user_movies = set()
    # for title, movie_title in watched.items():
    for watched in user_data["watched"]:
            user_movies.add(watched["title"])
    friends_movies = set()
    for friends_data in user_data["friends"]:
        for watched in friends_data["watched"]:
                friends_movies.add(watched["title"])
    user_unique = user_movies - friends_movies

    uni_user_movies = []
    for  watched in user_data["watched"]:
        if watched["title"] in user_unique:
            uni_user_movies.append(watched)
    return uni_user_movies


def get_friends_unique_watched(user_data):
    user_movies = []
    for watched in user_data["watched"]:
            user_movies.append(watched["title"])
    
    friends_movies = []
    for friends_data in user_data["friends"]:
        friends_movies.extend(friends_data["watched"])

    friends_unique = []
    for movie in friends_movies:
            if movie["title"] not in user_movies:
                if movie not in friends_unique:
                    friends_unique.append(movie)
    
    return friends_unique




# W A V E  4
def get_available_recs(user_data):
    user_data_subscriptions = user_data.get("subscriptions")
    friends_unique_movies = get_friends_unique_watched(user_data)

    movie_recs_list = []
    for subscription in user_data_subscriptions:
        for movie in friends_unique_movies:
            if subscription == movie.get("host"):
                movie_recs_list.append(movie)

    return movie_recs_list




# W A V E  5
def get_new_rec_by_genre(user_data):
    user_most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_list = get_friends_unique_watched(user_data)
    movie_recs_list = []

    for movie in friends_unique_list:
        if movie["genre"] ==  user_most_watched_genre:
            if movie not in movie_recs_list:
                movie_recs_list.append(movie)

    return movie_recs_list


def get_rec_from_favorites(user_data):
    user_unique_list = get_unique_watched(user_data)
    movie_recs_list = []

    for movie in user_unique_list:
        if movie in user_data["favorites"]:
            movie_recs_list.append(movie)
    return movie_recs_list





