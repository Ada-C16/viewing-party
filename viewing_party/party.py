#WAVE 1
def create_movie(title, genre, rating):
    if bool(title) == True and bool(genre) == True and bool(rating) == True:
        movie_details_dict = {"title": title, "genre": genre, "rating": rating}
        return movie_details_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data 

def watch_movie(user_data, title):   
    for movie in user_data['watchlist']:
        if title == movie['title']:
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
    return user_data



#WAVE 2
def get_watched_avg_rating(user_data):
    if len(user_data['watched']) == 0:
        return 0.0

    watched_ratings = []
    for movie in user_data['watched']: 
        rating_value = movie['rating']
        watched_ratings.append(rating_value)
    
    watched_rating_avg = sum(watched_ratings)/len(watched_ratings)
    return watched_rating_avg

def get_most_watched_genre(user_data):
    if len(user_data['watched']) == 0:
        return None
    
    watched_genre = []
    for movie in user_data['watched']: 
        genre_value =  movie['genre']
        watched_genre.append(genre_value)
    most_frequent_genre = max(set(watched_genre), key=watched_genre.count)
    return most_frequent_genre
    #get the value of genre from user_data watched movie list
    #append all the genre values to a list
    #find most common genre and return



#WAVE 3
def get_unique_watched(user_data):
    unique = []
    friends_watched = []
    friends_watched_titles = []
    for friend in user_data['friends']:
        friends_watched.extend(friend['watched'])
    for movie in friends_watched:
        friends_watched_titles.append(movie['title'])
    for movie in user_data['watched']:
        if movie['title'] not in friends_watched_titles:
            unique.append(movie)
    return unique

def get_friends_unique_watched(user_data):
    unique = []
    friends_watched = []
    user_watched_titles = []
    for friend in user_data['friends']:
        friends_watched.extend(friend['watched'])
    for movie in user_data['watched']:
        user_watched_titles.append(movie['title'])
    for movie in friends_watched:
        if movie['title'] not in user_watched_titles:
            if movie not in unique:
                unique.append(movie)
    return unique



#WAVE 4
def get_available_recs(user_data):
    recs_list = []
    friends_unique = get_friends_unique_watched(user_data)
    for movie in friends_unique:
        if movie['host'] in user_data['subscriptions']:
            if movie not in recs_list:
                recs_list.append(movie)
    return recs_list

    #start empty list of recs
    #loop through friends unique watched
    #if movie host is in users subs and not already in recs list
    #then append movie to recs list
    #return recs list



#WAVE 5
def get_new_rec_by_genre(user_data):
    user_genre_most_watched = get_most_watched_genre(user_data)
    friends_unique = get_friends_unique_watched(user_data)  
    recs_list = []
    for movie in friends_unique:
                if movie['genre'] == user_genre_most_watched:
                    if movie not in recs_list:
                        recs_list.append(movie)        
    return recs_list

def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    recs_list = []
    for movie in user_data['favorites']:
        if movie in unique_watched:
            recs_list.append(movie)
    return recs_list