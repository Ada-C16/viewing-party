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


create_movie("Lost Boys", "drama", 5)

# ********************
    # PART TWO #
# ********************

user_info = { 
    
    "watched" : 
    [{"title": "Title A",
    "genre": "Horror",
    "rating": 3.5}],
    "watchlist":
    [{"title": "Rocky Horror",
    "genre": "Musical",
    "rating": 5},
    {"title": "Anchor Man",
    "genre": "Comedy",
    "rating": 3.8},
    ]
}

movie_dict = {
    "title": "The Shining",
    "genre": "Horror",
    "rating": 5
}

def add_to_watched(user_data, movie):
    if "watched" in user_data.keys():
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = [movie]

    # print(user_data)

add_to_watched(user_info, movie_dict)

# ********************
    # PART THREE #
# ********************

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    print(user_data)

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
            print("moved")
            movie_watched = True
            return user_data
        else: 
            pass

    if movie_watched == False:
        return user_data

            
   

watch_movie(user_info, "Anchor Man")
print(user_info)