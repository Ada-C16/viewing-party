import statistics

# Wave 1
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating,
             }
        return movie_dict
    else:
        return None


def add_to_watched(user_data, movie):
    if movie:
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = []
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    


# def watch_movie(user_data,title): 
#     for i,d in enumerate(user_data['watchlist']):
#        if d['title'] == title:
#           user_data['watched'].append(d)
#           del user_data['watchlist'][i]      
#     return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    
    for movie in watchlist:
        if title in movie["title"]:
            watchlist.remove(movie)
            watched.append(movie)
            break
    
    return user_data


# Wave 2
def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    rating_sum = 0
    
    if len(watched) == 0:
        return 0
    for movie in watched:
        rating_sum += movie["rating"]  
        average_rating = rating_sum / len(watched)
    return average_rating


def get_most_watched_genre(user_data):
    most_watched = user_data["watched"]
    genres = []
    if len(most_watched) == 0:
        return None
    for movie in most_watched:
        genres.append(movie["genre"])
    return statistics.mode(genres)


# Wave 3
def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    
    friends_titles = []
    for friend in friends_watched:
        for title in friend["watched"]:
            friends_titles.append(title['title'])

    unique_watched = []

    for title in user_watched:
        if title["title"] not in friends_titles:
            unique_watched.append(title)

    return unique_watched
    
    

    

def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    
    user_titles = [title["title"] for title in user_watched]
    friends_unique_watched = []

    for friend in friends_watched:
        for title in friend["watched"]:
            if title["title"] not in user_titles:
                if title not in friends_unique_watched:
                    friends_unique_watched.append(title)

    return friends_unique_watched


# Wave 4
# user has not watched
def user_has_watched(movie, watched_movies):
    if movie in watched_movies:
        return True
    else:
        return False

# at least 1 friend has watched it
def in_friends_watchlist(movie, watched_by_friends):
    if movie in watched_by_friends:
        return True
    else:
        return False

# host of the movie is a service that is a service subscription
def in_users_subscriptions(host, subscriptions):
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
    user_watched = user_data["watched"]
    friends_movies = get_friends_movies(user_data)
    available_recs = []

    if len(friends_movies) == 0:
        return []

    user_watched_titles = set()
    for movie in user_watched:
        user_watched_titles.add(movie["title"])

    for movie in friends_movies:
        if movie["title"] not in user_watched_titles:
            if in_users_subscriptions(movie["host"], user_data["subscriptions"]):
                available_recs.append(movie)

    return available_recs


# Wave 5
def get_new_rec_by_genre(user_data):
    pass
    #return new_rec_by_genre

    # determine most_watched_genre
    new_rec_by_genre = []
    # add to new_rec if & only if:
    #   if user has not watched it
    # if user_has_watched(movie, watched_movies) is True
    # at least 1 friend has watched
    # if in_friends_watchlist(movie, watched_by_friends) is True
    # if 'genre' of movie == as most_watched_genre
    



def get_rec_from_favorites(user_data):
    pass
    # return rec_from_favorites
    # list of dictionaries called 'favorites'
    # user_favorites = user_data["favorites"]
    rec_from_favorites = []
    # append to rec_from_favorites
    # if movie in user_favorites


