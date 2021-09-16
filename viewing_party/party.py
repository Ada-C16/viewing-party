# Wave One 
# Part One 
from statistics import mode 

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    else:
        movie_list = {
                "title" : title, 
                "genre" : genre, 
                "rating" : rating 
        }
        return movie_list
        
                                # wave 1 part 2
def add_to_watched(user_data,movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    #user_data["watched"].append(movie)
    return user_data
                                # wave 1 part 3 
def add_to_watchlist(user_data, movie):
    add_list = user_data["watchlist"]
    add_list.append(movie)
    #user_data["watchlist"].append(movie)
    return user_data
                               # wave 1 part 4 
def watch_movie(user_data,title): 
    for i,d in enumerate(user_data['watchlist']):
       if d['title'] == title:
          user_data['watched'].append(d)
          del user_data['watchlist'][i]      
    return user_data


# WAVE TWO  - Part 1 
def get_watched_avg_rating(user_data): 
        if len(user_data["watched"]) == 0: 
            return float(0.0)
        else:
          return sum(d["rating"] for d in user_data['watched']) / len(user_data['watched'])

        # Part 2 
def get_most_watched_genre(user_data):
    most_watched = user_data['watched']
    genres = []
    if len(most_watched) == 0:
        return None
    for movie in most_watched:
        genres.append(movie["genre"])
        #genres.append(movie)
    return mode(genres)

#wave 3 
def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    
    friends_titles = []
    for friend in friends_watched:
        for title in friend["watched"]:
            friends_titles.append(title['title'])

    unique_watched = []
    for title in user_watched:
        if title["title"] not in friends_titles:
            unique_watched.append(title)

    return unique_watched

# part two 
def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    
    user_titles = [title["title"] for title in user_watched]
    friends_unique_watched = []

    for friend in friends_watched:
        for title in friend["watched"]:
            if title["title"] not in user_titles:
                if title not in friends_unique_watched:
                    friends_unique_watched.append(title)

    return friends_unique_watched   
    
#wave 4 
# user has not watched 
def user_has_watched(movie, watched_movies):
    if movie in watched_movies:
        return True 
    else:
        return False 

#atleast one friend has watched 
def user_has_watched(movie, watched_movies):
    if movie in watched_movies:
        return True
    else:
        return False

# at least 1 friend has watched it
def in_friends_watchlist(movie, watched_by_friends):
    if movie in watched_by_friends:
        return True
    else:
        return False

# host of the movie is a service that is a service subscription
def in_users_subscriptions(host, subscriptions):
    if host in subscriptions:
        return True
    else:
        return False


def get_friends_movies(user_data):
    titles = set()
    friends = user_data["friends"]
    movies = []
    for friend in friends:
        for movie in friend["watched"]:
            if movie["title"] not in titles:
                movies.append(movie)
                titles.add(movie["title"])
    return movies


def get_available_recs(user_data):
    user_watched = user_data["watched"]
    friends_movies = get_friends_movies(user_data)
    available_recs = []

    if len(friends_movies) == 0:
        return []

    user_watched_titles = set()
    for movie in user_watched:
        user_watched_titles.add(movie["title"])

    for movie in friends_movies:
        if movie["title"] not in user_watched_titles:
            if in_users_subscriptions(movie["host"], user_data["subscriptions"]):
                available_recs.append(movie)

    return available_recs

#wave 5 
# part 1 

#create a function named "get_new_rec_by_genre" 
# takes one parameter "user_data"

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    user_genre = get_most_watched_genre(user_data)
    user_hasnt_watched = get_friends_unique_watched(user_data)
    for movie in user_hasnt_watched:
        if movie["genre"] ==  user_genre:
            recommended_movies.append(movie)   
    return recommended_movies
    

def get_rec_from_favorites(user_data):
    favorites_movies = []
    #user_genre = # users most watched genre 
    user_movies = user_data["favorites"] # users favorite movies 
    #friends genres 
    friends_movie = get_friends_movies(user_data)# friends movies 

    if len(user_movies) == 0:
        return []
    for movie in user_movies:
        if movie not in friends_movie:
            favorites_movies.append(movie)
    return favorites_movies
       

    


   