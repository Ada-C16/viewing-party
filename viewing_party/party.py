# Wave 1 
def create_movie(title, genre, rating):
    if bool(title) == True & bool(genre) == True & bool(rating) == True:
        movie_to_watch = {
                "title" : title,
                "genre" : genre,
                "rating" : rating 
                }    
        return movie_to_watch      
    else: 
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    length_list_watchlist = len_list(user_data, "watchlist")
    for i in range(length_list_watchlist):
        if user_data["watchlist"][i]["title"] == title:
            movie_to_be_added = user_data["watchlist"][i]
            add_to_watched(user_data, movie_to_be_added)
            user_data["watchlist"].pop(i)
    return user_data

# helper func (length of list)
def len_list(user_data, key):
    return len(user_data[key])

# Wave 2 
def get_watched_avg_rating(user_data):
    sum_rating = 0 
    avg_rating = 0 
    length_list_watched = len_list(user_data, "watched")
    if length_list_watched != 0:
        for i in range(length_list_watched):
            sum_rating += user_data["watched"][i]["rating"]
        avg_rating = sum_rating / length_list_watched
    return avg_rating

def get_most_watched_genre(user_data):
    length_watched = len_list(user_data, "watched")
    if length_watched == 0:
        return None
    dict_genre = {}
    for i in range(length_watched):
        genre_counted = user_data["watched"][i]["genre"]  #str
        if genre_counted in dict_genre:
            dict_genre[genre_counted] = dict_genre.get(genre_counted) + 1
        else:
            dict_genre[genre_counted] = 1
# get the most genre
    cur_most_genre = user_data["watched"][0]["genre"]
    count_cur_most_genre = dict_genre[cur_most_genre]
    for count in dict_genre.values():
        if count > count_cur_most_genre:
            count_cur_most_genre = count
# get the key
    for key_genre in dict_genre:
        if dict_genre[key_genre] == count_cur_most_genre:
            return key_genre

        

# Wave 3
def get_unique_watched(user_data):
    set_user_watched = set()
    set_friends_watched = set()
    list_unique_user_watched = []
    length_user_watched = len_list(user_data, "watched")

    for i in range(length_user_watched):
        user_watched = user_data["watched"][i]["title"]
        set_user_watched.add(user_watched)

    # length_friends_watched = len(user_data["frieneds"]["watched"])
    for friends_data in user_data["friends"]:
        for movie in friends_data["watched"]:
            friends_watched = movie["title"]
            set_friends_watched.add(friends_watched)
    
    set_unique_user_watched = set_user_watched - set_friends_watched

    #retrieve index 
    for unique_movie in set_unique_user_watched:
        for movie in user_data["watched"]:
            if movie["title"] == unique_movie:
                list_unique_user_watched.append(movie)
    return list_unique_user_watched


def get_friends_unique_watched(user_data):
    set_user_watched = set()
    set_friends_watched = set()
    list_unique_friends_watched = []

    for friends_data in user_data["friends"]:
        for movie in friends_data["watched"]:
            friends_watched = movie["title"]
            set_friends_watched.add(friends_watched)

    for user_watched_movie in user_data["watched"]:
        set_user_watched.add(user_watched_movie["title"])
    
    set_unique_friends_watched = set_friends_watched - set_user_watched

    #append dict into list 
    for unique_movie in set_unique_friends_watched:
        for friends_data in user_data["friends"]:
            for movie in friends_data["watched"]:
                if movie["title"] == unique_movie and movie not in list_unique_friends_watched:
                    list_unique_friends_watched.append(movie)
    return list_unique_friends_watched

# Wave 4
def get_available_recs(user_data):
    list_recommended_movies = []
    list_unique_friends_watched = get_friends_unique_watched(user_data)

    for unique_movie in list_unique_friends_watched:
        for service_provider in user_data["subscriptions"]:
            if unique_movie["host"] == service_provider:
                list_recommended_movies.append(unique_movie)
    return list_recommended_movies


# Wave 5
def get_new_rec_by_genre(user_data):
    list_recommended_movies = []
    list_unique_friends_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    for movie in list_unique_friends_watched:
        if movie["genre"] == most_watched_genre:
            list_recommended_movies.append(movie)
    return list_recommended_movies


def get_rec_from_favorites(user_data):
    list_recommended_movies = []
    list_unique_user_watched = get_unique_watched(user_data)
    for unique_movie in list_unique_user_watched:
        for movie in user_data["favorites"]:
            if unique_movie == movie:
                list_recommended_movies.append(unique_movie)
    return list_recommended_movies



