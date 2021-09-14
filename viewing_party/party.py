#WAVE 1
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    updated_data = user_data["watched"]
    updated_data.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    add_watchlist = user_data["watchlist"]
    add_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    movies_watched = user_data["watched"]
    movies_to_watch = user_data["watchlist"]
    remove_list = []

    for movie in movies_to_watch:
        if title == movie["title"]:
            movies_watched.append(movie)
            remove_list.append(movie)   

    for movie in remove_list:
        movies_to_watch.remove(movie)
    
    return user_data

#WAVE 2
def get_watched_avg_rating(user_data):
    list_of_user_watched_movies = user_data["watched"]
    score = 0
    average_rating = 0.0

    if list_of_user_watched_movies == []:
        return average_rating 
    for movie in list_of_user_watched_movies:
        score += movie["rating"]
    average_rating = score/len(list_of_user_watched_movies)
    return average_rating
    

def get_most_watched_genre(user_data):
    list_of_user_watched_movies = user_data["watched"]
    list_of_genres = []

    if list_of_user_watched_movies == []:
            return None
    
    for movie in list_of_user_watched_movies:
        list_of_genres.append(movie["genre"])

    popular_genre = max(list_of_genres,key=list_of_genres.count)
    return popular_genre


#WAVE 3
def get_unique_watched(user_data):
    list_of_user_watched_movies = user_data["watched"]
    friend_movie_list = []
    unique_movie_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movie_list.append(movie) 
    for movie in list_of_user_watched_movies:
        if movie not in friend_movie_list:
            unique_movie_list.append(movie)

    return unique_movie_list 


def get_friends_unique_watched(user_data):
    list_of_user_watched_movies = user_data["watched"]
    friends_movie_list = []
    friends_unique_movie_list = []
    final_friends_unique_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_list.append(movie) 

    for movie in friends_movie_list:
        if not movie in list_of_user_watched_movies:
            friends_unique_movie_list.append(movie)
        
    for movie in friends_unique_movie_list:
        if not movie in final_friends_unique_list:
            final_friends_unique_list.append(movie)

    return final_friends_unique_list


#WAVE 4
def get_available_recs(user_data):
    # LIST OF MOVIES WATCHED BY THE USER
    list_of_user_watched_movies = user_data["watched"]



    #LIST OF SUBSCRIPTIONS OF THE USER
    list_of_user_subscriptions = user_data["subscriptions"]

    #LOOP TO GET SUBSCIPTONS OF THE FRIENDS
    list_of_friends_subscriptions = []
    friends_movie_list = []
    friends_unique_movie_list = []
    final_friends_unique_list = []


    #LIST OF RECOMMENDED MOVIES
    list_of_rec_movies = []

    #CONDITIONAL FOR EMPTY LIST
    if len(list_of_rec_movies) == 0:
        return []

    #LOOP GETS ALL THE MOVIES IN FRIENDS LIST
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_list.append(movie) 

    #LOOP GETS THE MOVIES IN FRIENDS LIST THAT USER HAS NOT SEEN
    for movie in friends_movie_list:
        if not movie in list_of_user_watched_movies:
            friends_unique_movie_list.append(movie)

    #LOOP GETS ALL THE FRIENDS UNIQUE MOVIES WITHOUT DUPLICATES  
    for movie in friends_unique_movie_list:
        if not movie in final_friends_unique_list:
            final_friends_unique_list.append(movie)

    #LOOP GETS THE FRIENDS SUBSCRIPTIONS
    for friend in user_data["friends"]:
        for sub in friend["watched"]:
          list_of_friends_subscriptions.append(sub)

    #LOOP COMPARES THE FRIENDS SUBS WITH THE USERS
    for movie in final_friends_unique_list:
        if list_of_user_subscriptions == list_of_friends_subscriptions:
            list_of_rec_movies.append(movie)

    #RETURNS THE LIST OF RECOMMENEDED MOVIES
    return list_of_rec_movies


    
    #FINAL FRIENDS UNIQUE LIST GIVES THE LIST OF MOVIES THAT USER HAS NOT SEEN
    #LOOP THROUGH BOTH THE USER AND FRIENDS SUBSCRIPTIONS TO GET COMPARISON
    #APPEND TO RECOMMENDED MOVIE LIST 
    #RETURN THE LIST










#WAVE 5
def get_new_rec_by_genre(user_data):
    pass
    
    
