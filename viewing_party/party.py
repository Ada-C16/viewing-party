# ************ WAVE 1 ************ #

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title": title, "genre": genre, "rating": rating}
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data


# ************ WAVE 2 ************ #

def get_watched_avg_rating(user_data):
    total = 0
    count = 0
    
    if len(user_data["watched"])==0:
        return 0
    else:
        for movie in user_data["watched"]:
            total += float(movie["rating"])
            count += 1
        return total/count

def get_most_watched_genre(user_data):
    genre_dict={}
    
    if len(user_data["watched"]) == 0: # This loop covers if the watched list is empty
        return None

    for movie in user_data["watched"]: # This loop creates a frequency dictionary
        genre = movie["genre"]
        if genre in genre_dict.keys():
            genre_dict[genre]+=1
        else:
            genre_dict[genre]=1
    
    highest_count = max(genre_dict.values())  # Calculates what the highest frequency is  
    for genre, count in genre_dict.items(): # This loop finds which genre has the highest frequency
        if count == highest_count: # This if statement does not work if there are multiple generes that == the ma freq
            return genre


# ************ WAVE 3 ************ #

def get_title_only_set(user_data): 
# Created this function because both the functions below use this info
    user_set = set()
    friend_set = set()
    
    for movie in user_data["watched"]: # Creates set of movie titles user has watched
        user_set.add(movie["title"])
    
    for friend in user_data["friends"]: # Creates set of movie titles friends have watched, used a set so no repeats 
        for movie in friend["watched"]:
            friend_set.add(movie["title"])
    
    return user_set, friend_set 

def get_unique_watched(user_data):
    user_only_movies = []
    user_set, friend_set = get_title_only_set(user_data)

    movies_user_only = user_set.difference(friend_set)  # This creates a set of the movies that only the user has watched
    for title in movies_user_only: # This loop adds movie dictionaries to a list
        user_only_movies.append({"title":title})
    
    return user_only_movies

def get_friends_unique_watched(user_data):
    friend_only_movies = []
    user_set, friend_set = get_title_only_set(user_data)

    movies_friend_only = friend_set.difference(user_set)  # This creates a set of the movies that only the friends have watched
    for title in movies_friend_only: # This loop adds movie dictionaries to a list
        friend_only_movies.append({"title":title})
    
    return friend_only_movies


# ************ WAVE 4 ************ #

def get_available_recs(user_data):
    titles_watched_list = []
    rec_list = []
    
    for movie in user_data["watched"]: # This loop creates a list of movies user has watched (list of movie titles as strings)
        titles_watched_list.append(movie["title"])

    for friend in user_data["friends"]: 
        for movie in friend["watched"]:
            if (movie["title"] not in titles_watched_list) and (movie["host"] in user_data["subscriptions"]): # This block only adds reccomendations to a list of dictionaries if user has subscripting, and hasn't watched movie
                movie_rec_dict = {"title":movie["title"], "host": movie["host"]}
                if movie_rec_dict not in rec_list: # This ensures that there are no repeat recs
                    rec_list.append(movie_rec_dict)
    
    return rec_list


# ************ WAVE 5 ************ #

def get_new_rec_by_genre(user_data):
    titles_watched_list = []
    rec_list = []
    genre = get_most_watched_genre(user_data)

    for movie in user_data["watched"]: # This loop creates a list of movies user has watched (list of movie titles as strings)
        titles_watched_list.append(movie["title"])

    for friend in user_data["friends"]: 
        for movie in friend["watched"]:
            if (movie["title"] not in titles_watched_list) and (movie["genre"] == genre): # This block only adds reccomendations to a list of dictionaries if the genre matches users most frequent genre, and the user hasn't watched movie
                movie_rec_dict={"title":movie["title"], "genre": movie["genre"]}
                if movie_rec_dict not in rec_list: # This ensures that there are no repeat recs
                    rec_list.append(movie_rec_dict)
    
    return rec_list

def get_rec_from_favorites(user_data):
    friend_watch_list = []
    user_favories_list = []
    
    for movie in user_data["favorites"]:
        user_favories_list.append({"title":movie["title"]})
    
    for friend in user_data["friends"]: 
        for movie in friend["watched"]:
            friend_watch_list.append({"title":movie["title"]})
    
    for fav_movie in user_favories_list:
        if fav_movie in friend_watch_list:
            user_favories_list.remove(fav_movie)
    
    return user_favories_list