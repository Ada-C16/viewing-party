def create_movie(title, genre, rating):        
    if title and genre and rating:
        movie_dict ={}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    elif not title or genre or rating:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return(user_data)

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return(user_data)

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    if len(user_data["watched"]) > 0:
        sum_of_ratings = 0.0
        for movie in user_data["watched"]:
            sum_of_ratings += movie["rating"]
        avg_rating = sum_of_ratings / len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    most_watched_genre = None
    most_watched_genre_stat_dict = {}
    #iterate thru the list of watched movies and add value (num of watched) key (genre of movie) pair to most_watched_genre_stat_dict
    for movie_dict in user_data["watched"]:  
        if movie_dict["genre"] in  most_watched_genre_stat_dict:
            most_watched_genre_stat_dict[movie_dict["genre"]] += 1
        else:
            most_watched_genre_stat_dict[movie_dict["genre"]] = 1

    #determine the most watched genre
    if len(user_data["watched"]):
        most_watched_genre = max(most_watched_genre_stat_dict, key=most_watched_genre_stat_dict.get)

    return most_watched_genre

def get_unique_watched(user_data):
    #collect list of titles that the user has watched
    user_watched_movie_titles = []
    for user_movie in user_data["watched"]:
        user_watched_movie_titles.append(user_movie["title"])

    #collect list of titles that the friends have watched
    friends_watched_movie_titles = []
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            friends_watched_movie_titles.append(movie["title"])
    
    #compare user and friends titles
    user_unique_watched_movie_titles = set(user_watched_movie_titles).difference(set(friends_watched_movie_titles))

    #add dictionary of user uniques titles to a list
    unique_watched = []
    for title in list(user_unique_watched_movie_titles):
        dict = {"title": title}
        unique_watched.append(dict)

    #return list of dictionaries that rep the movies
    return unique_watched

def get_friends_unique_watched(user_data):
    #collect list of titles that the user has watched
    user_watched_movie_titles = []
    for user_movie in user_data["watched"]:
        user_watched_movie_titles.append(user_movie["title"])

    #collect list of titles that the friends have watched
    friends_watched_movie_titles = []
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            friends_watched_movie_titles.append(movie["title"])
    
    #compare friends and user titles
    friend_unique_watched_movie_titles = set(friends_watched_movie_titles).difference(set(user_watched_movie_titles))

    #add dictionary of friends uniques titles to a list
    friend_unique_watched = []
    for title in list(friend_unique_watched_movie_titles):
        dict = {"title": title}
        friend_unique_watched.append(dict)

    #return list of dictionaries of movies that friends have seen but user has not.
    return friend_unique_watched


#print(create_movie("green mile", "action", None))
#create_movie("green mile", "action", None)
#movie1 = create_movie("Title A", "Horror", 3.5)
#movie2 = create_movie("CATS", "Musical", 100)
#add_to_watched(vange_data, movie1)
#add_to_watched(vange_data, movie2)
#add_to_watchlist(vange_data, movie1)
#add_to_watchlist(vange_data, movie2)
#watch_movie(vange_data, "Title A")
# ************************************************************* ~
#pytest tests/test_wave_03.py

vange_data = {
    "watched": [
        {"title": "lasagna"},
        {"title": "chicken"},
        {"title": "cow"},
        {"title": "shrimp"},
        {"title": "catfish"},
        {"title": "whale"}
	],
    
    "friends": [
        {
            "watched": [
                {"title": "shrimp"},
                {"title": "catfish"}
            ]
        },
        {
            "watched": [
                {"title": "whale"},
                {"title": "shark"},
                {"title": "octopus"}
            ]
        }
    ]
}

amandas_data = {
            "watched": [
                {
                    "title": "Title A"
                },
                {
                    "title": "Title B"
                },
                {
                    "title": "Title C"
                },
                {
                    "title": "Title D"
                },
                {
                    "title": "Title E"
                },
            ],
            "friends": [
                {
                    "watched": [
                        {
                            "title": "Title A"
                        },
                        {
                            "title": "Title C"
                        }
                    ]
                },
                {
                    "watched": [
                        {
                            "title": "Title A"
                        },
                        {
                            "title": "Title D"
                        },
                        {
                            "title": "Title F"
                        }
                    ]
                }
            ]
        }

#print(get_friends_unique_watched(vange_data))