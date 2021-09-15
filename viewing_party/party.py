# ********************
    # PART ONE #
# ********************

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else: 
        return None


# ********************
    # PART TWO #
# ********************



# movie_dict = {
#     "title": "The Shining",
#     "genre": "Horror",
#     "rating": 5
# }

def add_to_watched(user_data, movie):
    if "watched" in user_data.keys():
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = [movie]

    return user_data

# ********************
    # PART THREE #
# ********************

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    
    return user_data

# ********************
    # PART FOUR #
# ********************

def watch_movie(user_data, title):

    count = 0
    movie_watched = False
    
    for item in user_data["watchlist"]:
        count += 1
        if item["title"] == title:
            watched_movie = user_data["watchlist"][count-1]
            user_data["watchlist"].remove(watched_movie)
            user_data["watched"].append(watched_movie)
            movie_watched = True
            return user_data
        else: 
            pass

    if movie_watched == False:
        return user_data

# WAVE 2 #

user_info = { 
    
    "watched" : 
    [{"title": "Title A",
    "genre": "Horror",
    "rating": 3.5},
    {"title": "The Shining",
    "genre": "Horror",
    "rating": 5}],
    "watchlist":
    [{"title": "Rocky Horror",
    "genre": "Musical",
    "rating": 5},
    {"title": "Anchor Man",
    "genre": "Comedy",
    "rating": 3.8},
    ]
}

def get_watched_avg_rating(user_data):
    # calculate the avg ratings of all movies in watchlist
    # if watchlist is empty, the average rating is 0.0
    # the data structure is a dictionary where the keys include "watched", etc, and the values are a list of dictionaries
    sum = 0.0
    num_of_ratings = 0
    for watched in user_data["watched"]:
        if user_data["watched"] == []:
            return 0.0
        for key, value in watched.items():
            if key == "rating":
                sum += value
                num_of_ratings += 1

    if num_of_ratings > 0:
        average = sum / num_of_ratings
        return average
    else: 
        return 0.0

            
   
