import math

# wave 1 Creating new movie dictionary 

def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre 
        new_movie["rating"] = rating
    return new_movie

# wave 1/2 Adding movie to the user's watched 

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# wave 1/3 Adding movie to the user's watchlist 

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data 

# wave 1/4 Remove title from a watchlist and add to watched 

def watch_movie(user_data, title):
    for index in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][index]["title"]:
            movie =(user_data["watchlist"][index])
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return  user_data    

# wave 2/1 Calcualte the average rating of all movies in the watched list

def get_watched_avg_rating(user_data):
    sum = 0
    average_rating = 0
    if len(user_data["watched"]) < 1:
        average_rating = 0.0 
    else:
        for index in range(len(user_data["watched"])):
            sum += (user_data["watched"][index]["rating"])
            average_rating = sum / (len(user_data["watched"]))
    return average_rating

# wave 2/1 Get the most watched genre 

def get_most_watched_genre(user_data):
    most_watched_list = []
    most_watch_dict = {}
    most_watched_genre_string = ""
    
    if len(user_data["watched"]) == 0:
        return None
    else:
        for index in range(len(user_data["watched"])):
            capitalize_genre = user_data["watched"][index]["genre"].capitalize()
            if capitalize_genre in most_watch_dict:
                most_watch_dict[capitalize_genre] += 1
            else:
                most_watch_dict[capitalize_genre] = 1
                most_watch_dict = most_watch_dict 
        
        most_watched_list = most_watch_dict.values()
        # for key, value in most_watch_dict.items():
        #     most_watched_list.append(value)

        most_watch_genre = max(most_watched_list)
        for movie, count in most_watch_dict.items():
            if count == most_watch_genre:
                most_watched_genre_string = movie
    return most_watched_genre_string


# wave 3/1 Get movies that the user has watched but none of their friends have watched

def store_watched_title_from_friends(user_data):
    
    unique_watched_list = []
    for index in range(len(user_data["friends"])): 
        for key, value in user_data["friends"][index].items():
            for movie in value: 
                unique_watched_list.append((movie["title"]))
    return (unique_watched_list)


def get_unique_watched(user_data):
    unique_movie_list = []
    watched_list_from_friends = store_watched_title_from_friends(user_data)
    
    for index in range(len(user_data["watched"])):
        unique_movie_dic = {}
        if user_data["watched"][index]["title"] not in watched_list_from_friends:
            unique_movie_dic["title"] = user_data["watched"][index]["title"]
            unique_movie_list.append(unique_movie_dic) 
    return unique_movie_list
   

# Wave 3/2 Get movies which at least on of the user's friends have watched, but user has not watched

def store_user_watched_in_list(user_data):
    user_watched_list = []
    for index in range(len(user_data["watched"])):
        user_watched_list.append(user_data["watched"][index]["title"])
    return (user_watched_list) 

def get_friends_unique_watched(user_data):
    unique_movie_list = []
    friends_watched_list = store_watched_title_from_friends(user_data)
    user_watched_list = store_user_watched_in_list(user_data)
    
    for movie in friends_watched_list:
        unique_movie_dic = {}
        if movie not in user_watched_list:
            unique_movie_dic["title"] = movie
            if unique_movie_dic not in unique_movie_list: 
                unique_movie_list.append(unique_movie_dic) 
    return (unique_movie_list)



# wave 4 Create a list of recommended movies 
def store_watched_movie_from_friends(user_data):
    
    unique_watched_list = []
    for index in range(len(user_data["friends"])): 
        for key, value in user_data["friends"][index].items():
            for movie in value: 
                unique_watched_list.append((movie))
    return (unique_watched_list)

def get_friends_unique_title_host(user_data):
    unique_movie_list = []
    friends_watched_list = store_watched_movie_from_friends(user_data)
    user_watched_list = store_user_watched_in_list(user_data)
    
    for movie in friends_watched_list:
        unique_movie_dic = {}
        if movie["title"] not in user_watched_list:
            unique_movie_dic["title"] = movie["title"]
            unique_movie_dic["host"] = movie["host"]
            if unique_movie_dic not in unique_movie_list: 
                unique_movie_list.append(unique_movie_dic) 
    return (unique_movie_list)

def get_available_recs(user_data):
    recommended_movie_list = []
    user_subscription_list = user_data["subscriptions"]

    sorted_friends_watched_movies = get_friends_unique_title_host(user_data)
    for sorted_movie in sorted_friends_watched_movies:
        if sorted_movie["host"] in user_subscription_list:
            recommended_movie_list.append(sorted_movie)
    return(recommended_movie_list)


# wave 5/1 Create a lsit of recommended movies based on most most watched genre

def store_user_watched_movies_genre(user_data):
    user_watched_list = []
    for index in range(len(user_data["watched"])):
        user_watched_list.append(user_data["watched"][index])
    return (user_watched_list) 

def get_friends_unique_title_genre(user_data):
    unique_movie_list = []
    friends_watched_list = store_watched_movie_from_friends(user_data)
    user_watched_list = store_user_watched_movies_genre(user_data)
    for movie in friends_watched_list:
        print(f" MOVIES {movie}")
        if movie not in user_watched_list:
            if movie not in unique_movie_list: 
                    unique_movie_list.append(movie) 
    return (unique_movie_list)


def get_new_rec_by_genre(user_data):
    recommended_movies_genre = []
    if len(user_data["watched"]) == 0:
        return recommended_movies_genre
    else:
        frequently_watched_genre = get_most_watched_genre(user_data)
        print(f" FREQ GENRE{frequently_watched_genre}" ) 
        sorted_movies_genre = get_friends_unique_title_genre(user_data) 
        print(f" SORTED MOVIES GENRE{sorted_movies_genre}")
        for movie in sorted_movies_genre:
            if movie["genre"] == frequently_watched_genre and (movie not in recommended_movies_genre):
                print(movie)
                recommended_movies_genre.append(movie) 
        print(recommended_movies_genre )
        return recommended_movies_genre 


# wave 5/2 create a list of recommended movies from users favorites 

def get_rec_from_favorites(user_data):
    recommended_movies_list = []
    unique_movie_list = get_unique_watched(user_data)
    
    for index in range(len(user_data["favorites"])):
        if user_data["favorites"][index] in unique_movie_list:
            recommended_movies_list.append(user_data["favorites"][index])
    return unique_movie_list
