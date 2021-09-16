
def create_movie(title, genre, rating):
    #initialize dictionary and add key value pairs if truthy
    movie = {}

    if title and genre and rating:
        movie['title'] = title
        movie['genre'] = genre
        movie['rating'] = rating
    else:
        return None

    #returns movie dictionary
    return movie


def add_to_watched(user_data, movie):
    # add movie dictionary to value at key "watched"
    user_data["watched"].append(movie)
    
    return user_data


def add_to_watchlist(user_data, movie):
    # add movie dictionary to value at key "watchlist"
    user_data["watchlist"].append(movie)
    
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data['watchlist'] 

    for movie in watchlist:
        
        if title in movie.values():
            add_to_watched(user_data, movie) # use add_to_watched to add movie to watched if in watchlist
            watchlist.pop() # remove from watchlist once added to watched

    return user_data


def get_watched_avg_rating(user_data):
    # list at the key "watched"
    watched_list = user_data["watched"]
    sum = 0.0

    # if the list at "watched" is empty average rating should be 0.0
    # if not, add int at key rating to sum and average it
    if len(watched_list) < 1:
        average_rating = 0.0
    else:
        for movie in watched_list:
            sum += movie["rating"]
            average_rating = sum / len(watched_list)
    
    return average_rating


def get_most_watched_genre(user_data):
    # list at the key "watched"
    watched_list = user_data["watched"]

    # dictionary to store genres & their frequency 
    frequency = {}

    # if the list at "watched" is empty return None
    # if not, add genre to dict with frequency
    if len(watched_list) < 1:
        return None
    else:
        for movie in watched_list:
            genre = movie["genre"]
            if genre in frequency:
                frequency[genre] += 1
            else:
                frequency[genre] = 1
        
        # getting key @ genre with the largest value 
        most_frequent_genre = max(frequency, key = frequency.get)
    
        return most_frequent_genre


def get_unique_watched(user_data):
    #initialize a list for all of the items under the key "friends"
    friends_list = user_data["friends"]
    user_movie_list = []
    result_list = []
    
    # sets initialized to hold unique movie titles 
    friends_set = set()
    user_set = set()

    # iterate through each item in friends_list 
    for friend in friends_list:
        # iterate through each movie in the friends at "watched"
        for movie in friend['watched']:
                # add the title of each movie to a set initialized above 
                friends_set.add(movie["title"])

    # adding users watched movie titles to a set
    for movie in user_data["watched"]:
        user_set.add(movie["title"])
        user_movie_list.append(movie)

    # difference of user and friends sets to find titles not watched by friends
    user_watched_not_watched_by_friends = user_set.difference(friends_set)

    for movie in user_movie_list:
        if movie["title"] in user_watched_not_watched_by_friends:
            result_list.append(movie)  # append the movie(dict) to the result_list 

    result = [dict(s) for s in set(frozenset(d.items()) for d in result_list)]  # get only unique elements of the result_list

    return result


def get_friends_unique_watched(user_data):
    #initialize a list for all of the items under the key "friends"
    friends_list = user_data["friends"]
    friends_movies_list = []
    result_list = []
    
    friends_set = set()
    user_set = set()

    # iterate through each item in friends_list 
    for friend in friends_list:
        # iterate through each movie in the friends "watched"
        for movie in friend['watched']:
                # add the title of each movie to a set initialized above 
                friends_set.add(movie["title"])
                friends_movies_list.append(movie)

    # adding users watched movie titles to a set
    for movie in user_data["watched"]:
        user_set.add(movie["title"])

    watched_by_friends = friends_set.difference(user_set) # use set differnece to get movies watched by friends

    for movie in friends_movies_list:
        if movie["title"] in watched_by_friends:
            result_list.append(movie)  # append the movie(dict) to the result list

    result = [dict(s) for s in set(frozenset(d.items()) for d in result_list)]  # get only unique elements in the result list
    
    return result


def get_available_recs(user_data):
    user_subscriptions = user_data["subscriptions"]  # list of movies(dicts) and host 
    friends_unique_watched = get_friends_unique_watched(user_data) # returns list of movies(dicts) that at least one friend has watched but the user has not
    result_list = []
    
    for movie in friends_unique_watched:
        if movie["host"] in user_subscriptions:
            result_list.append(movie)  # append the movie dict to the result list 

    result = [dict(s) for s in set(frozenset(d.items()) for d in result_list)]  # only get unique elements in the list

    return result


def get_new_rec_by_genre(user_data):
    recommended = []

    most_watched_genre = get_most_watched_genre(user_data) # returns a string of user's most watched genre
    watched_by_friend = get_friends_unique_watched(user_data) # returns list of movies(dicts) that at least one friend has watched but user has not

    for movie in watched_by_friend:
        if movie["genre"] == most_watched_genre:
            recommended.append(movie)

    # returns list of recommended movies if genre matches the most watched 
    return recommended


def get_rec_from_favorites(user_data):
    recommended = []

    user_watched = get_unique_watched(user_data) # returns list of movies(dicts) that only the user has watched
    user_favorites = user_data["favorites"] # list of movies in user's favorites

    for favorite in user_favorites:
        for movie in user_watched:
            if favorite["title"] in movie["title"]:
                recommended.append(movie)
                
    return recommended