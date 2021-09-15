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
        
def get_unique_watched(user_data):
    movies_friends_watched = []
    unique_movies = []
    friend = []
    watched = []
    user = user_data["watched"]
    for item in user_data["friends"]: # list of dictionaries
        friend.append(item) 
        for item in friend: 
            watched.append(item["watched"])
        for friend_list in watched:
            for movie in friend_list:
                movies_friends_watched.append(movie)
    # print(f"{movies_friends_watched}=")
    for item in user:
        if item not in movies_friends_watched:
            unique_movies.append(item)
    return unique_movies

def get_friends_unique_watched(user_data):
    pass
    movies_friends_watched = []
    friend_unique_movies = []
    friend = []
    watched = []
    user = user_data["watched"]
    for item in user_data["friends"]: # list of dictionaries
        friend.append(item) 
        for item in friend: 
            watched.append(item["watched"])
            for friend_list in watched:
                for movie in friend_list:
                    movies_friends_watched.append(movie)
    for movie in movies_friends_watched:
        if movie not in user and movie not in friend_unique_movies:
            friend_unique_movies.append(movie)
    # print(f"{friend_unique_movies}=")
    return friend_unique_movies
    
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
            # print(f"{item}=")
            for subs in friend["watched"]:
                # print(f"{subs}=")
                if item == subs["host"]:
                    movies_with_sub.append(subs) # list of dict of movies user can watch with their host

    all_friend_movies = [] 
    for friends in user_data["friends"]: 
        for item in friends["watched"]:
            if item not in all_friend_movies:
                all_friend_movies.append(item) # list of all movies friends watched

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
    
    print(suggested_movies)
    return suggested_movies

def get_new_rec_by_genre(user_data): # list of recommended movies, based on what genre user has seen most of
    # choose genre and choose movie from friend's lists
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
    # print(fave_genre)
    friend_rec = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == fave_genre:
                if movie not in friend_rec:
                    friend_rec.append(movie)
    # print(friend_rec)
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
    # print(suggestion)
    return suggestion
