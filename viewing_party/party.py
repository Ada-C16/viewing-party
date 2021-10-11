#Wave 1
def create_movie(title,genre,rating):
    if title and genre and rating:
        movie_dict = {"title": title, 
        "genre": genre,
         "rating": rating,
        }
        return movie_dict
    else:
        return None



def add_to_watched(user_data, movie):
    #user_data = {watched: [{}]}
    #watched = user_data["watched"]
    #watched.append(movie)
    #return user_data
    # user_data["watched"] = []
    # movie = { "title": "Title A",
    # "genre": "Horror", 
    # "rating": 3.5}
    if movie:
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = []
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)

    return user_data  

def watch_movie(user_data, title): 
    watch_list = user_data["watchlist"] 
    watched = user_data["watched"]

    #if title: #in movie["title"] :
    for movie in watch_list:
        if title in movie["title"]:
            watch_list.remove(movie)
            watched.append(movie)
        
    
    return user_data
    
#Wave 2
def get_watched_avg_rating(user_data):
    total_rating = 0
    if len(user_data["watched"]) == 0:
        return 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"] 
    return total_rating / len(user_data["watched"])



def get_most_watched_genre(user_data):
    genre_to_count_dict = {}
#dict = {genre : count} 
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_to_count_dict:
            genre_to_count_dict[movie["genre"]] = 1
        else: 
            genre_to_count_dict[movie["genre"]] += 1
    
    max_count = 0
    most_popular_genre = ""
    for genre, count in genre_to_count_dict.items():
        if count > max_count:
            max_count = count
            most_popular_genre = genre
    return most_popular_genre

#Wave 3

def get_unique_watched(user_data):
    if len(user_data["watched"]) == 0:
        return []
    
    user_movies = set()
    for watched in user_data["watched"]:
            user_movies.add(watched["title"])
    
    friends_movies = set()
    for friends_data in user_data["friends"]:
        for watched in friends_data["watched"]:
                friends_movies.add(watched["title"])

    user_unique = user_movies - friends_movies
    uni_user_movies = []
    for  watched in user_data["watched"]:
        if watched["title"] in user_unique:
            uni_user_movies.append(watched)

    return uni_user_movies

def get_friends_unique_watched(user_data):
    user_movies = set()
    for watched in user_data["watched"]:
            user_movies.add(watched["title"])

    
    friends_movies = set()
    for friends_data in user_data["friends"]:
        for watched in friends_data["watched"]:
                friends_movies.add(watched["title"])


    friends_unique = friends_movies - user_movies

    uni_friends_movies = []
    for movie in friends_unique:
        uni_friends_movies.append({"title": movie})
        if len(uni_friends_movies) == 0:
            return []
    
    return uni_friends_movies

#Wave 4

def user_has_not_watched(movie, watched_movies):
    if movie in watched_movies:
        return True
    else:
        return False

def in_friends_watchlist(movie, watched_by_friends):
    if movie in watched_by_friends:
        return True
    else:
        return False

def in_user_subscriptions(host, subscriptions):
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
    friends_movies = get_friends_movies(user_data)
    movie_recs = []

    if len(friends_movies) == 0:
        return []

    titles_of_movies_user_watched = set()
    for movie in user_data["watched"]:
        titles_of_movies_user_watched.add(movie["title"])

    for movie in friends_movies:
        if movie["title"] not in titles_of_movies_user_watched:
            if in_user_subscriptions(movie["host"], user_data["subscriptions"]):
                movie_recs.append(movie)

    return movie_recs

#wave 5
def get_new_rec_by_genre(user_data):
    most_frequent_watched = get_most_watched_genre(user_data)
    user_not_watched = get_friends_unique_watched(user_data)
    recommended_movies = []

    if len(user_data["watched"]) == 0:
        return []
    
    user_movies = []
    for watched in user_data["watched"]:
            user_movies.append(watched)
    
    friends_movies = []
    for friends_data in user_data["friends"]:
        for watched in friends_data["watched"]:
                friends_movies.append(watched)

    
    recommend_movies = []
    most_frequent_watched = get_most_watched_genre(user_data)
    
    for movie in friends_movies:
        if movie not in user_movies and movie["genre"] == most_frequent_watched:
            if movie in recommend_movies:
                pass
            else:
                recommend_movies.append(movie)
            

    return recommend_movies

def get_rec_from_favorites(user_data):
    fav_movies = []
    user_fav_movies = user_data["favorites"]
    movies = get_unique_watched(user_data)

    
    for movie in movies: 
        if movie in user_fav_movies:
            fav_movies.append(movie)
    
    return fav_movies


#     def get_available_recs(user_data):
# #favorites = user_data["favorites"]
#         return get_available_recs


# list = []
#if not in watched:
# if in friends_watchlist:
# if genre == max(genre):
#return list

#     def get_available_recs(user_data):
# #favorites = user_data["favorites"]
#         return get_available_recs