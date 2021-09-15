def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    if new_movie["title"] == None:
        return None
    elif new_movie["genre"] == None:
        return None
    elif new_movie["rating"] == None:
        return None
    return new_movie


def add_to_watched(user_data,movie):
    # user_data = {"watched":[]}
    # movie = {"title": "Title A","genre":"Horror","rating":3.5}
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    for item in user_data["watchlist"]:
        if item["title"] == title:
            user_data["watchlist"].remove(item)
            user_data["watched"].append(item)
    return user_data


def get_watched_avg_rating(user_data):
    #look at the value that is a list
    #looping thru the list
    # get the value of  "rating"
    #user_data = {"watched":[]}
    moviesList = user_data["watched"]
    if moviesList == []:
            return 0.0
    sum = 0
    for item in moviesList:
        # print(f"Looking at {item=}")
        sum += item["rating"]
        
    avg = sum/len(moviesList)
    return avg

def get_most_watched_genre(user_data):
    # user_data = {"watched":[{"genre":"something"},
    # {"genre":"romantic"},{"genre":"something"}]
    genre_count = {}
    max_watched = None
    
    for item in user_data["watched"]:
        if (item["genre"] in genre_count):
            genre_count[item["genre"]] += 1
        else:
            genre_count[item["genre"]] = 1
        for key,value in genre_count.items():
            max_watched = max(genre_count, key =genre_count.get)
            # genre_max_list.append(value)

    return max_watched


def get_unique_watched(user_data):
    for movies in user_data["friends"]:
        for friend_watched in movies["watched"]:
            if friend_watched in user_data["watched"]:
                user_data["watched"].remove(friend_watched)
    return user_data["watched"]
            


def get_friends_unique_watched(user_data):
    friend_watched_list = []
    for friend in user_data["friends"]:
        for friend_watched in friend["watched"]:
            print(f"friend watched is {friend_watched}")
            print("user watched movies are",user_data["watched"])
            if friend_watched not in user_data["watched"] and\
                friend_watched not in friend_watched_list:
                friend_watched_list.append(friend_watched)
    return friend_watched_list



def get_available_recs(user_data):
    friend_just_watched = []
    print("user data watched are :",user_data["watched"])
    for friend in user_data["friends"]:
        for friend_watched in friend["watched"]:
            print(friend_watched)
            if {"title":friend_watched["title"]} not in user_data["watched"]\
                and friend_watched["host"] in user_data["subscriptions"]:
                if friend_watched not in friend_just_watched:
                    friend_just_watched.append(friend_watched)
    return friend_just_watched



def get_new_rec_by_genre(user_data):
    friends_rec = get_friends_unique_watched(user_data)
    favorite_genre = get_most_watched_genre(user_data)
    favor_genre = []
    for movie in friends_rec:
        if not user_data["watched"]:
            return favor_genre
        elif movie["genre"] in favorite_genre:
            favor_genre.append(movie)
    return favor_genre



def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    user_fav = user_data["favorites"]
    fav_unique = []

    for movie in unique_watched:
        if not user_fav:
            fav_unique
        elif movie in user_fav:
            fav_unique.append(movie)

    return fav_unique
