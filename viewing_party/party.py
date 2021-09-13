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
    