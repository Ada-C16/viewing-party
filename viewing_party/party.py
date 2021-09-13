def create_movie(title, genre, rating):
    dictionary_template = {}
    if title and genre and rating:
        dictionary_template["title"] = title
        dictionary_template["genre"] = genre
        dictionary_template["rating"] = rating
        return dictionary_template
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    index = 0
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            watched_movie = user_data["watchlist"].pop(index)
            user_data["watched"].append(watched_movie)
        index += 1
    return user_data

def get_watched_avg_rating(user_data):
    num_of_movies = 0
    sum_of_movie_ratings = 0.0
    average_rating = 0
    if not user_data["watched"]:
        return average_rating
    else:
        for movie in user_data["watched"]:
            sum_of_movie_ratings += movie["rating"]
            num_of_movies += 1
    average_rating = sum_of_movie_ratings/num_of_movies
    return average_rating

def get_most_watched_genre(user_data):
    genre_dict = {}
    genre_list = []
    previous_highest_times_watched = 1
    if not user_data["watched"]:
        return None
    else:
        for movie in user_data["watched"]:
            if genre_dict.get(movie["genre"]):
                genre_dict[movie["genre"]] += 1
            else:
                genre_dict[movie["genre"]] = 1
        for genre, times_watched in genre_dict.items():
            if times_watched > previous_highest_times_watched:
                genre_list.clear()
                genre_list.append(genre)
                previous_highest_times_watched = times_watched
            elif times_watched == previous_highest_times_watched:
                genre_list.append(genre)
                previous_highest_times_watched = times_watched
        if len(genre_list) == 1:
            return genre_list[0]
        elif len(genre_list) > 1: #code to account for more than 1 most popular genre
            multiple_highest_genre = ""
            for genre in genre_list:
                if multiple_highest_genre == "":
                    multiple_highest_genre += f"{genre} "
                else: 
                    multiple_highest_genre += f"& {genre} "
            return multiple_highest_genre

#*****************************************
def get_unique_watched(user_data):
  
    #creation of 2 independent lists, one for watched for freidns and another for watched for user to be able to manipulate the data without changing the original user_data data and to be able to more easily compare user & friend data

    user_watched_list =[]
    friends_watched_list = []

    if not user_data["watched"]:
        return user_data["watched"]
    else:
        for movie in user_data["watched"]:
            user_watched_list.append(movie)

    i=0
    while i < len(user_data["friends"]):
        for movie in user_data["friends"][i]["watched"]:
            friends_watched_list.append(movie)
        i += 1
    

    user_watched_set = set()
    friends_watched_set = set()
    #convert friend_list and User-List to a list of strings, then to sets of strings
    i = 0
    while i < len(user_watched_list):
        user_watched_set.add(str(user_watched_list[i]))
        i += 1

    j = 0
    while j < len(friends_watched_list):
        friends_watched_set.add(str(friends_watched_list[j]))
        j += 1


    user_only_watched_set = user_watched_set - friends_watched_set


    #converting difference set back to a list of dictionaries
    import ast
    user_only_watched_list = list(user_only_watched_set)
    user_only_watched_list_final = []

    k=0
    while k < len(user_only_watched_set):
        convert_to_dict = ast.literal_eval(user_only_watched_list[k])
        user_only_watched_list_final.append(convert_to_dict)
        k += 1

    return user_only_watched_list_final


def get_friends_unique_watched(user_data):
    user_watched_list =[]
    friends_watched_list = []

    for movie in user_data["watched"]:
        user_watched_list.append(movie)

    i = 0
    while i < len(user_data["friends"]):
        for movie in user_data["friends"][i]["watched"]:
            friends_watched_list.append(movie)
        i += 1
    

    user_watched_set = set()
    friends_watched_set = set()
    #convert friend_list and User-List to a list of strings, then to sets of strings
    i = 0
    while i < len(user_watched_list):
        user_watched_set.add(str(user_watched_list[i]))
        i += 1

    j = 0
    while j < len(friends_watched_list):
        friends_watched_set.add(str(friends_watched_list[j]))
        j += 1


    friends_only_watched_set = friends_watched_set - user_watched_set  


    #converting difference set back to a list of dictionaries
    import ast
    friends_only_watched_list = list(friends_only_watched_set)
    friends_only_watched_list_final = []

    k=0
    while k < len(friends_only_watched_set):
        convert_to_dict = ast.literal_eval(friends_only_watched_list[k])
        friends_only_watched_list_final.append(convert_to_dict)
        k += 1

    return friends_only_watched_list_final

amand_data = {
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title B"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title C"
                    }
                ]
            }
        ]
    }

get_friends_unique_watched(amand_data)

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

user_data = {
    "watchlist": [{
  "title": "Title A",
  "genre": "Horror",
  "rating": 3.5
},
{
  "title": "Title B",
  "genre": "Horror",
  "rating": 3.5
}], 
  "watched": [{
  "title": "Title A",
  "genre": "Horror",
  "rating": 3.5
},
{
  "title": "Title B",
  "genre": "Horror",
  "rating": 3.5
}]
}