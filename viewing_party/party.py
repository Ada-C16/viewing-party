# Wave 1 #
def create_movie(title, genre, rating):
    if title == None:
        return None
    if genre == None:
        return None
    if rating == None:
        return None
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating   
    
    return new_movie
    print(create_movie("Title A", "horror", None))
    
def add_to_watched(user_data, movie):
    user_data_list = user_data["watched"]
    user_data_list.append(movie)
    return user_data 
    #create a dictionary with watched as the key
    #add movie to watched list inside the user data and return user data
def add_to_watchlist(user_data, movie):
    #user_data["watchlist"] IS a list
    #user_data["watched"][0] IS a dictionary
    user_data["watchlist"].append(movie) 
    return user_data

def watch_movie(user_data, title):
#we want take movies from the watchlist(key in user_data dict) and put it in the watched list 
#find the movie title if in watchlist 
#add it to watched list
#the remove fromt the watchlist 
    for movie in user_data["watchlist"]: #movie(IS a dict) is temp variable standing for each watchlist element 
        for key, value in movie.items():
            if title == value:
                user_data["watched"].append(movie)
                user_data["watchlist"].remove(movie)
                return user_data
    return user_data    

## WAVE 2 ## 
def get_watched_avg_rating(user_data):
#Every rating has number and every movie has a rating 
#find average sum the values then divide by the numver of the values 
    if len(user_data["watched"]) == 0:
        return 0
    rating_list = []
    for movie in user_data["watched"]:
        rating_list.append(movie["rating"])
    return sum(rating_list) / len(rating_list) 

def get_most_watched_genre(user_data):
    #look through all the movies in watched list and grab the most frequent genre 
    movie_genre_dict = {}
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]:
            genre = movie["genre"]
            if genre not in movie_genre_dict:
                movie_genre_dict[genre] = 1
            else:
                movie_genre_dict[genre] += 1
    else:
        return None

    #loop over movie_genre_dict and have 2 temp variables and 
    max_genre = 0
    max_genre_key = ""
    for genre, genre_freq in movie_genre_dict.items():
        if genre_freq > max_genre:
            max_genre_key = genre
            max_genre = genre_freq

    return max_genre_key

    # UnboundLocalError: local variable 'max_genera' referenced before assignment
    # look at each one to see which number is bigger
    #need two variables most seen and number of times 
    
### WAVE 3 ###
# determine which movies user has watched that listed friends have not watched.
#Returns a list of dictionaries that represents a list of unique movies
def get_unique_watched(user_data):
    for item in user_data["watched"]:
        print(item)
    for item in user_data["friends"]:
        print(item["watched"])
        for watched_movie in item["watched"]:
            print(user_data["watched"])
            if watched_movie in user_data["watched"]:
                user_data["watched"].remove(watched_movie)
    return user_data["watched"]

            
def get_friends_unique_watched(user_data):
    
    unique_movies = []
    
    user_movies = set()
    for watched_movie in user_data["watched"]:  
        user_movies.add(watched_movie["title"])  
        
    friends_movies = set()    
    for friend_data in user_data["friends"]:
        for watched_movie in friend_data["watched"]:
            friends_movies.add(watched_movie["title"])
            
    movies_unique_to_friends = friends_movies.difference(user_movies)
    
    for title in movies_unique_to_friends:
        format_dict = {}
        format_dict["title"] = title
        unique_movies.append(format_dict)
        
    return unique_movies

#### WAVE 4 ####
        
def get_available_recs(user_data):
    #create list to store reccomendations 
    recommendations = []
    #create veriable to refer to subscriptions list
    user_subscriptions = user_data["subscriptions"]
    friend_recommendations = get_friends_unique_watched(user_data)
    friends_movies = []
    for movie in friend_recommendations:
        friends_movies.append(movie["title"])
    
    #next find friend-recs with channels user is subscirbed to
    for friend_data in user_data["friends"]:
        for watched_movie_data in friend_data["watched"]:
            #if that user is subsciebed to the host 
            if watched_movie_data["host"] in user_subscriptions and watched_movie_data["title"] in friends_movies:
                if watched_movie_data not in recommendations:
                    recommendations.append(watched_movie_data)
    return recommendations

##### WAVE 5 #####
def get_new_rec_by_genre(user_data):
    recommendations = []
    most_freq_genre = get_most_watched_genre(user_data) #returns a string
    friends_movie_recs = get_friends_unique_watched(user_data) #returns a list
    friends_movies = []    
    for friend_data in user_data["friends"]:
        for watched_movie in friend_data["watched"]:
            friends_movies.append(watched_movie)

    for movie_data in friends_movies:
        if {"title": movie_data["title"]} in friends_movie_recs:
            if movie_data["genre"] == most_freq_genre:
                if movie_data not in recommendations:
                    recommendations.append(movie_data)
    
    return recommendations


def get_rec_from_favorites(user_data):
    # Create a list of user's favorite movies
    fav_movies = [movie for movie in user_data['favorites']]

    # Create a list of user's watched-movies that friends haven't viewed
    users_unique_movies = get_unique_watched(user_data)
    
    # Find user's favorite movies that friends haven't viewed
    recommendations = [movie for movie in fav_movies if \
        movie in users_unique_movies]

    return recommendations
