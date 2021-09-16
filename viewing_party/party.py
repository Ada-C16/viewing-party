#wave 1
def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        movie_dict = {
            "title" : movie_title,
            "genre" : genre,
            "rating" : rating,
        }
        return movie_dict
    else:
        return None

#wave 2
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if movie in user_data["watchlist"]:
        print("This movie is already in the watchlist!")
    else:     
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
    all_ratings = 0
    if len(user_data["watched"]) == 0: 
        print("We haven't started watching yet!")
        return 0
    for movie in user_data["watched"]:
        all_ratings += movie["rating"]
    return all_ratings / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_dict = {}
    if len(user_data["watched"]) == 0: 
        print("We haven't started watching yet!")
        return None
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_dict:
            genre_dict[movie["genre"]] = 1
        else:
            genre_dict[movie["genre"]] += 1

    genre_tally = 0
    fave_genre = ""
    for genre, count in genre_dict.items():
        if count > genre_tally:
            genre_tally = count
            fave_genre = genre
    return fave_genre


#wave 3
def get_unique_watched(user_data):
    only_friends_watched =[]
    my_unique_watched = []
    for watched in user_data["friends"]:
        for movie in watched["watched"]:
            only_friends_watched.append(movie["title"])
    for movie in user_data["watched"]:
        if movie["title"] not in only_friends_watched:
            my_unique_watched.append(movie)
    return my_unique_watched


def get_friends_unique_watched(user_data):
    their_movies = []
    for movie in user_data["watched"]:
        their_movies.append(movie)

    friends_watched = []
    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            if movie not in user_data["watched"]:
                friends_watched.append(movie)

    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in user_data["watched"]:
            if movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
    return friends_unique_watched


def approved_user_subs(host, subscriptions):
    if host in subscriptions:
        return True
    else:
        return False


def get_friends_movies(user_data):
    friends_titles = set()
    friends = user_data["friends"]
    friends_movies = []
    for friend in friends:
        for movie in friend["watched"]:
            if movie["title"] not in friends_titles:
                friends_movies.append(movie)
                friends_titles.add(movie["title"])
    return friends_movies

#wave 4
def get_available_recs(user_data):
    friends_recs = []
    my_rec_list = []
    user_watched = []
    user_subs = user_data["subscriptions"]
    for friend in user_data["friends"]:
        for film in friend["watched"]:
            friends_recs.append(film)
    for item in user_data["watched"]:
        user_watched.append(item["title"])
        user_subs = user_data["subscriptions"]
    for movie in friends_recs:
        if movie["title"] not in user_watched and movie["host"] in user_subs and movie not in my_rec_list:
            my_rec_list.append(movie)
    if len(friends_recs) == 0:
        return []
    return my_rec_list

#wave 5
def get_new_rec_by_genre(user_data):
    friends_recs_by_genre = get_friends_movies(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    my_rec_list_by_genre = []
    for movie in friends_recs_by_genre:
        if movie["genre"] == most_watched_genre:
            my_rec_list_by_genre.append(movie)
    return my_rec_list_by_genre


def get_rec_from_favorites(user_data):
    my_favorites = []
    unique_watched = get_unique_watched(user_data)
    for movie in unique_watched:
        if movie in user_data["favorites"]:
            my_favorites.append(movie)
    return my_favorites 


