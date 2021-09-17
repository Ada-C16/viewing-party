def create_movie(title, genre, rating):
    movie = {}
    if not None in [title, genre, rating]:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating

        return movie

    else:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title): 
    movie_to_transfer = None

    for i in range(len(user_data["watchlist"])):

        if title == user_data["watchlist"][i]["title"]:
            movie_to_transfer = i
            break

    if movie_to_transfer != None:
        user_data["watched"].append(user_data["watchlist"][movie_to_transfer])

        user_data["watchlist"].pop(movie_to_transfer)

    return user_data

# Wave 2

def get_watched_avg_rating(user_data):
#User_data is a dict with a "watched" list of movie dictionaries
    sum_all_ratings = 0.0
    count = 0
    #Should I make a list that extracts all the rating values from the user_data dictionary?
    #How to extract the ratings? user_data["watched"]["rating"]???
    for movie in user_data["watched"]:
        #Add the value for "rating" keys
        sum_all_ratings += movie["rating"] 
        count += 1

    if count == 0:
        return 0.0
    average_rating = sum_all_ratings/count
    return average_rating

def get_most_watched_genre(user_data):
    #Make a data structure to go through user_data and collect the frequency of genre.
    #Then find largest number. most_freq = {} Go through loop and compare and replace the variable to find highest freq as key:value pair?
    #Return the key for the value(most_freq)
    most_watched_genre = {}
    most_frequent_count = 0
    most_frequent_genre = None

    for movie in user_data["watched"]:
        if not movie["genre"] in most_watched_genre:
            most_watched_genre[movie["genre"]] = 0

        most_watched_genre[movie["genre"]] += 1
        
        if most_watched_genre[movie["genre"]] >= most_frequent_count:
            most_frequent_count = most_watched_genre[movie["genre"]]
            most_frequent_genre = movie["genre"]
    
    return most_frequent_genre

# Wave 3

def get_unique_watched(user_data):
    #Return a list of dictionaries that represents a list of movies. The list that the user has watched but their friends have not.
    friends_watched_titles = set()
    users_unique_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_titles.add(movie["title"])

    for movie in user_data["watched"]:
        if not movie["title"] in friends_watched_titles:
            users_unique_watched.append({"title": movie["title"]})
    return users_unique_watched


def get_friends_unique_watched(user_data):
    #Like step above, but return a list of dictionaries that at least 1 of the user's friends has watched, but the user has not.
    users_watched_titles = set()
    friends_unique_titles = set()
    friends_unique_watched = []

    for movie in user_data["watched"]:
        users_watched_titles.add(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie["title"] in users_watched_titles:
                friends_unique_titles.add(movie["title"])

    for title in friends_unique_titles:
        friends_unique_watched.append({"title": title})
    return friends_unique_watched

# Wave 4

def get_available_recs(user_data):
    #Only add movies that: user has not watched, at least 1 friend has watched, "host" of the movie is in user's "subscriptions".
    user_watched_movies = []
    available_recs_titles_only = set()
    available_recs_and_hosts = []
    title_to_host = {}


    for movie in user_data["watched"]:
        user_watched_movies.append(movie["title"])
    
    print(user_watched_movies)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie["title"] in user_watched_movies:
                if movie["host"] in user_data["subscriptions"]:
                    available_recs_titles_only.add(movie["title"])
                    title_to_host[movie["title"]] = movie["host"]
    
    for title in available_recs_titles_only:
        available_recs_and_hosts.append({"host": title_to_host[title], "title": title})

    return available_recs_and_hosts


# Wave 5

def get_new_rec_by_genre(user_data):
    #Reference most_freq genre.
    #Only add movies that: user has not watched, at least 1 friend has watched, "genre" of movie == user's most_freq genre.
    recs_by_genre = []
    return recs_by_genre

def get_rec_from_favorites(user_data):
    #Only add movies that: movie is in user's "favorites", None of the friends have watched it
    rec_from_favorites =[]
    return rec_from_favorites