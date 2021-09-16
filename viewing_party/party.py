#Wave 1 first 4 tests
def create_movie(movie_title, genre, rating):

    if movie_title and genre and rating:
#creating new_movie dictionary
        new_movie = {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
        return new_movie

    else:
        return None

#Wave 1 Tests 5 6 
def add_to_watched(user_data, movie):
    #adding movies to the watched list
    user_data["watched"].append(movie)
    return user_data

#Wave 1 Tests 7 8
def add_to_watchlist(user_data, movie):
    #adding movies to watchlist
    user_data["watchlist"].append(movie)
    return user_data

#wave 1 Tests 9 10 11
def watch_movie(user_data, title):
    
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            watched_dict = movie
            break
    else:
        return user_data 
    user_data["watched"].append(watched_dict)
    user_data["watchlist"].remove(watched_dict)

    return user_data

#Wave 2 Tests 1 2
def get_watched_avg_rating(user_data):
    #calculating average rating of all movies in the watched list
    if len(user_data["watched"]) <= 0:
        return 0.0
    
    else:
        user_rating = []
        for movie in user_data["watched"]:
            user_rating.append(movie["rating"])

    average = sum(user_rating)/len(user_rating)
    return average

#Wave 2 Tests 3 4 5
def get_most_watched_genre(user_data):

    most_watched = []
    
    if len(user_data["watched"]) <= 0:
        return None
    else:
        for movie in user_data["watched"]:
            most_watched.append(movie["genre"])
    
    return max(most_watched, key = most_watched.count)

#Wave 3 Tests 1 2
def get_unique_watched(user_data):
    
    #Creating variables that are not exactly necessary but make my code easier to read (at least to me)
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    friends_movies = []
    #Adding elements from friends_watched to friends_movies
    for friend in friends_watched:
        for movie in friend["watched"]:
            friends_movies.append(movie["title"])

    unique_watched_list = []
    #Adding only movies watched by user and not friends to unique_watched_list
    for movie in user_watched:
        if movie["title"] not in friends_movies:
            unique_watched_list.append(movie)

    return unique_watched_list

# Wave 3 Tests 3 4 5 
def get_friends_unique_watched(user_data):
    user_movies = user_data["watched"]
    friends_movies = user_data["friends"]
    friends_movies_list = []
    
# accesing each item(dictionary) in the friends["watched"] list
    friends_movies_first = friends_movies[0]
    friends_movies_second = friends_movies[1]
# adding each item(dictionary) to friends_movies_list
    for dictionary in friends_movies_first["watched"]:
        friends_movies_list.append(dictionary)

    for dictionary in friends_movies_second["watched"]:
        friends_movies_list.append(dictionary)
# no duplicates in the friends_movie_list
    unique_friends_list = []
    for item in friends_movies_list:
        if item not in unique_friends_list:
            unique_friends_list.append(item)

    for movie in user_movies:
        for item in unique_friends_list:
            if movie["title"] in item.values():
                unique_friends_list.remove(item)
            
    return unique_friends_list

# Wave 4 Tests 1 2 3 4 
def get_available_recs(user_data):

    unique_watched = get_friends_unique_watched(user_data)

    for movie in range(len(unique_watched)):
        for movie in unique_watched:
            print(movie["host"])
            if movie["host"] not in user_data["subscriptions"]:
                unique_watched.remove(movie)

    return unique_watched
            
#Wave 5 Tests 1 2 3 4 

def get_new_rec_by_genre(user_data):
    
    unique_watched = get_friends_unique_watched(user_data)
    rec_movies = []
    friends_watched = user_data["friends"]
    user_watched = user_data["watched"]
    friends_list = []
    print(unique_watched)
#creating unnecessary variables to make my code easier to work with 
    first_friend_movies = friends_watched[0]
    second_friend_movies = friends_watched[1]

    for dictionary in first_friend_movies["watched"]:
        friends_list.append(dictionary)
    for dictionary in second_friend_movies["watched"]:
        friends_list.append(dictionary)

    if len(user_watched) == 0:
        return user_watched
    else:
        for movie in friends_list:
            if movie not in user_watched:
                rec_movies.append(movie)
#removes duplicates
    rec_movies = [i for n, i in enumerate(rec_movies) if i not in rec_movies[n + 1:]]
    
    return rec_movies

def get_rec_from_favorites(user_data):
    user_favorites = user_data["favorites"]
    friends_watched = user_data["friends"]
    friends_list = []
    favorites = []
    
    first_friend_movies = friends_watched[0]
    second_friend_movies = friends_watched[1]

    for dictionary in first_friend_movies["watched"]:
        friends_list.append(dictionary)
    for dictionary in second_friend_movies["watched"]:
        friends_list.append(dictionary)
    print("friends list")
    print(friends_list)

    if len(user_favorites) == 0:
        return user_favorites

    else: 
        for movie in user_favorites:
            if movie not in friends_list:
                favorites.append(movie)

        return favorites