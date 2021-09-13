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
    list_of_watched_movies = user_data["watched"]
    score = 0
    average_rating = 0.0

    if list_of_watched_movies == []:
        return average_rating 
    for movie in list_of_watched_movies:
        score += movie["rating"]
    average_rating = score/len(list_of_watched_movies)
    return average_rating
    

def get_most_watched_genre(user_data):
    list_of_watched_movies = user_data["watched"]
    list_of_genres = []

    if list_of_watched_movies == []:
            return None
    
    for movie in list_of_watched_movies:
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
    pass
    list_of_user_watched_movies = user_data["watched"]
    friend_movie_list = []
    friends_unique_movie_list = []
    final_friends_unique_list = []


    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movie_list.append(movie) 

    for movie in friend_movie_list:
        if not movie in list_of_user_watched_movies:
            friends_unique_movie_list.append(movie)
        
    for movie in friends_unique_movie_list:
        if not movie in final_friends_unique_list:
            final_friends_unique_list.append(movie)

    return final_friends_unique_list

#WAVE 4
def get_available_recs(user_data):
    pass

#WAVE 5
def get_new_rec_by_genre(user_data):
    pass
    
    
