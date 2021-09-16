def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {}
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else: 
        new_movie = None
    return new_movie
    
def add_to_watched(user_data, movie):
    if movie:
        user_data["watched"].append(movie)
    else:
        user_data["watched"]    
    return user_data

def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
    else:
        user_data["watchlist"]
    return user_data

def watch_movie(user_data, title): 
    for item in user_data["watchlist"]:   
        if item["title"] == title:
            user_data["watched"].append(item)
    for item in user_data["watchlist"]:
        if item in user_data["watched"]:
            user_data["watchlist"].remove(item)
    return user_data 

def get_watched_avg_rating(user_data):
    counter = 0
    total = 0
    if user_data["watched"] == []:
        avg = 0.0
    for item in user_data["watched"]:
        if item["rating"]:
            counter += 1
            total += item["rating"]
            avg = total/counter
    return avg

def get_most_watched_genre(user_data):
    pass
    if user_data["watched"] == []:
        genre = None
    counter = 1
    for item in user_data["watched"]:
        if item["genre"] == item["genre"]:
            counter +=1
            genre = item["genre"]
    return genre
        
def get_unique_watched(user_data): # movies only user has watched
    movies_friends_watched = set()
    unique_movies = set()
    list_unique_movies = []
    user = user_data["watched"]
    friends = user_data["friends"]
    for friend in friends: # list of dictionaries
        for movie in friend["watched"]:
            movies_friends_watched.add(movie["title"])
    for movie in user:
        unique_movies.add(movie["title"])
        for movie in movies_friends_watched:
            if movie in unique_movies:
                unique_movies.remove(movie)
    list_unique_movies = [{"title": title} for title in unique_movies ] 
    return list_unique_movies

def get_friends_unique_watched(user_data):
    user_watched = set()
    movies_friends_watched = set()
    list_movies = []# list of movies user watched
    for movie in user_data["watched"]:
        user_watched.add(movie["title"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movies_friends_watched.add(movie["title"])
            for movie in user_data["watched"]:
                if movie["title"] in movies_friends_watched:
                    movies_friends_watched.remove(movie["title"])
    list_movies = [{"title" : title} for title in movies_friends_watched]
    return list_movies

    
def get_available_recs(user_data): 
    user_watched_info = []
    index = 0
    for item in user_data["watched"]:
        item["host"] = user_data["subscriptions"][index]
        index +=1
        user_watched_info.append(item) # list of dict, added host key and value
    movies_with_sub = []
    for item in user_data["subscriptions"]:
        for friend in user_data["friends"]:
            for subs in friend["watched"]:
                if item == subs["host"]:
                    movies_with_sub.append(subs) # list of dict of movies user can watch with their host

    all_friend_movies = []
    for friends in user_data["friends"]: 
        for item in friends["watched"]:
            if item not in all_friend_movies:
                all_friend_movies.append(item)

    same_movies = []
    for movie in movies_with_sub: 
        for friends in all_friend_movies: 
            if movie["host"] == friends["host"]:
                if friends not in same_movies:
                    same_movies.append(friends) # list of possible suggestions based on user host

    suggested_movies = []
    for movie in same_movies:
        if movie not in user_watched_info:
            suggested_movies.append(movie) # final suggestions from friends
    return suggested_movies

def get_new_rec_by_genre(user_data): 
    fave = 0
    fave_genre = None # value of user's favorite genre
    user_fave_list = []
    user_fave_count = {}
    for movie in user_data["watched"]:
        user_fave_list.append(movie["genre"])
    for genre in user_fave_list:
        user_fave_count[genre] = user_fave_list.count(genre)
        for key, value in user_fave_count.items():
            if fave < value:
                fave = value
                fave_genre = key
    friend_rec = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == fave_genre:
                if movie not in friend_rec:
                    friend_rec.append(movie)
    return friend_rec

def get_rec_from_favorites(user_data):
    pass
    user_fave = [] # single variable to loop through user favorites
    for movie in user_data["favorites"]:
        user_fave.append(movie)

    fave_seen_by_friends = [] # list of favorites the user and friends have in common
    for movie in user_data["favorites"]:
        for item in user_data["friends"]:
            for friend_movie in item["watched"]:
                if friend_movie["title"] == movie["title"]:
                    if movie not in fave_seen_by_friends:
                        fave_seen_by_friends.append(movie)
                        
    suggestion = [] # favorite not seen by any friends, but seen by user
    for movie in user_fave:
        if movie not in fave_seen_by_friends:
            suggestion.append(movie)
    return suggestion
