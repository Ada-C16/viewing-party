
#Test Wave 01 functions

#Function returns a dictionary containing movie details
def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        movie={
            "title": movie_title,
            "genre": genre,
            "rating" : rating
        }
        return movie
    else:
        return None

#Function to add movie to user's watched list    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

#Function to add movie to user's watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

#Function to move movie from user's watchlist to watched list
def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        for key, movie_tit in movie.items():
            if movie_tit == movie_title:
                user_data["watched"].append(movie)
                user_data["watchlist"].remove(movie)       
    return user_data

# Test wave 02 functions

#Function returns avg rating from user's watched list
def get_watched_avg_rating(user_data):
    
    avg = 0
    if user_data["watched"]:
        ratings = [movie["rating"] for movie in user_data["watched"]]
        avg = sum(ratings) / len(ratings)
    return avg



#Function returns most frequent genre from watched list

def get_most_watched_genre(user_data):
    
    if user_data["watched"]:

        #Create a list of all watched genres
        watched_genres = [movie["genre"] for movie in user_data["watched"]]

        #Create a frequency dictionary for all watched genres
        freq = {}
        for genre in watched_genres:
            freq[genre] = watched_genres.count(genre)

        #finding the most watched genre and accounting for the edge case of multiple genres tying
        max_genre_list = []
        max_genre = 0
        for genre in set(watched_genres):
            if freq[genre] > max_genre:
                max_genre_list = [genre]
                max_genre = freq[genre]
            elif freq[genre] == max_genre:
                max_genre_list.append(genre)
        return ', '.join(max_genre_list)
    return

#Test wave 03 functions

#Function returns list of movies that user has watched but friends haven't

def get_unique_watched(user_data):
   
    user_titles = [movie["title"] for movie in user_data["watched"]]

    friend_titles = [movie["title"] for friend in user_data["friends"] for movie in friend["watched"]]

    #use set diffrence to create a list of unique titles
    unique_titles_list = list(set(user_titles)-set(friend_titles))

    #iterate through user's watched list and return a list of a movie dictionary
    unique_movies_list = [movie for movie in user_data["watched"] for title in unique_titles_list if title == movie["title"]]

    return unique_movies_list
        


#Function returns list of movies that friends have watched but user hasn't

def get_friends_unique_watched(user_data):

    unique_movies_list = []

    user_titles = [movie["title"] for movie in user_data["watched"]]

    friend_titles = [movie["title"] for friend in user_data["friends"] for movie in friend["watched"]]

    #Use set difference to create a list of unique titles
    unique_titles_list = list(set(friend_titles)-set(user_titles))

    #iterate through user's friend's watched list and return a list of a movie dictionary
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            for title in unique_titles_list:
                if title == movie["title"] and not (movie in unique_movies_list):
                    unique_movies_list.append(movie)

    return unique_movies_list


#Test wave 04 functions

#Function returns a list of movie's based on what their friend's have seen and what subcriptions they have

def get_available_recs(user_data):
    
    friends_unique_watched = get_friends_unique_watched(user_data)

    movie_recs = [movie for movie in friends_unique_watched if movie["host"] in user_data["subscriptions"]]

    return movie_recs


#Test wave 05 functions

#Function returns a list of movie's based on what their friend's have seen and what the user's most watched genre is

def get_new_rec_by_genre(user_data):

    fav_genre = get_most_watched_genre(user_data)
    available_recs = get_friends_unique_watched(user_data)

    movie_recs = []

    if user_data["watched"]:
        movie_recs = [movie for movie in available_recs if movie["genre"] in fav_genre]
    
    return movie_recs

#Function returns a list of movie dictionaries that the user has watched and is also in their favorites list

def get_rec_from_favorites(user_data):
    
    unique_user_movies = get_unique_watched(user_data)
    rec_list = []

    if user_data["favorites"]:
        rec_list = [movie for movie in unique_user_movies if movie in user_data["favorites"]]
    
    return rec_list