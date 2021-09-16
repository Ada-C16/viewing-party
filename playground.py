from typing import final


user_data =  {
        "watched": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            },
            {
                "title": "Title C"
            }
        ],
        "favorites": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            }
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title B"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title C"
                    },
                    {
                        "title": "Title D"
                    }
                ]
            }
        ]
    }


def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        new_movie = {"title": movie_title, "genre": genre, "rating": rating}
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].pop()
    return user_data

def get_watched_avg_rating(user_data):
    ratings_list = []
    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])
    if len(ratings_list) == 0:
        return 0
    else:
        avg_rating = sum(ratings_list)/len(ratings_list)
        return avg_rating

def get_most_watched_genre(user_data):
    # Create Frequency Table
    frequency_table = {}
    for movie in user_data["watched"]:
        if movie["genre"] in frequency_table:
            frequency_table[str(movie["genre"])] += 1
        else:
            frequency_table[str(movie["genre"])] = 1
    # Find Max Value
    current_high = -1  # TODO: Might need to return None if watched is empty
    max_genre = None  # TODO: Might need to change this to a list for ties
    for genre, frequency in frequency_table.items():
        if frequency > current_high:
            current_high = frequency
            max_genre = genre
    return(max_genre)

 # ************* WAVE 3 ******************   
def helper_combined_friends_list(user_data):
    """
    Returns list of dictionaries containing all movies friends have watched.
    Will contain duplicates if more than one friend has watched the same movie.
    """
    combined_friends_list = []
    for friend in user_data["friends"]:
        for friend_watched in friend["watched"]:
            combined_friends_list.append(friend_watched)
    return combined_friends_list

def helper_add_key_to_movie_dict(list_of_dictionaries, key_to_add, user_data):
    """This function takes in a list of dictionaries which contain only the key 'title' then
    returns an updated list of dictionaries containing the keys title along with either 'host' or
    'genre' depending on which value was entered for the parameter key_to_add."""
    combined_friends_list = helper_combined_friends_list(user_data)
    updated_movie_list = []
    for item in list_of_dictionaries:
        for movie in combined_friends_list:
            if movie["title"] == item["title"]:
                movie_dict = {"title": item["title"], key_to_add: movie[key_to_add]}
                updated_movie_list.append(movie_dict)
                break  # Break to avoid adding movie twice if in combined_friends_list multiple times
    return updated_movie_list

 #  TODO: Consider creating a helper function for finding unique movies
 #  TODO: Look into list comprehension to make smoother
def get_unique_watched(user_data):
    # Step 1: Get combined friend's watched list
    combined_friends = set()
    for friend in user_data["friends"]:
        for friend_watched in friend["watched"]:
            combined_friends.add(friend_watched["title"])
    # Step 2: Get User's watched list
    watched_set = set()
    for movie_watched in user_data["watched"]:
        watched_set.add(movie_watched["title"])
    # Step 3: Find user's difference with Friend's
    unique_watched_set = watched_set.difference(combined_friends)
    # Ste 4: Convert to Dictionary
    unique_watched_list = []
    for item in unique_watched_set:
        title_dict = {"title": item}
        unique_watched_list.append(title_dict)
    return unique_watched_list

# def get_friends_unique_watched(user_data):
#     # Step 1: Get combined friend's watched list
#     combined_friends = set()
#     for friend in user_data["friends"]:
#         for friend_watched in friend["watched"]:
#             combined_friends.add(friend_watched["title"])
#     # Step 2: Get User's watched list
#     watched_set = set()
#     for movie_watched in user_data["watched"]:
#         watched_set.add(movie_watched["title"])
#     # Step 3: Find Friend's difference with Users's
#     unique_watched_set = combined_friends.difference(watched_set)
#     # Ste 4: Convert to Dictionary
#     unique_watched_list = []
#     for item in unique_watched_set:
#         title_dict = {"title": item}
#         unique_watched_list.append(title_dict)
#     return unique_watched_list

def get_friends_unique_watched(user_data):
    # Step 1: Get combined friend's watched list
    combined_friends = set()
    for friend in user_data["friends"]:
        for friend_watched in friend["watched"]:
            combined_friends.add(friend_watched["title"])

    # Step 2: Get User's watched list
    user_watched_set = set()
    for movie_watched in user_data["watched"]:
        user_watched_set.add(movie_watched["title"])
    # Step 3: Find Friend's difference with Users's
    unique_watched_set = combined_friends.difference(user_watched_set)
    # Ste 4: Convert to Dictionary
    unique_watched_list = []
    for item in unique_watched_set:
        title_dict = {"title": item}
        unique_watched_list.append(title_dict)
    return unique_watched_list


# ************* WAVE 4 ******************   
def get_available_recs(user_data):
    friends_unwatched_list = get_friends_unique_watched(user_data)
    friends_unwatched_list_with_host = helper_add_key_to_movie_dict(friends_unwatched_list, "host", user_data)
    available_services = user_data["subscriptions"]
    final_recommendations = []
    for movie in friends_unwatched_list_with_host:
        if movie["host"] in available_services:
            final_recommendations.append(movie)
    return final_recommendations

# ************* WAVE 5 *******************
# def get_new_rec_by_genre(user_data):
# friends_unwatched_list = get_friends_unique_watched(user_data)
# friends_unwatched_list_with_genre = helper_add_key_to_movie_dict(friends_unwatched_list, "genre", user_data)
# print("************* FIRST PRINT STATEMENT ***********")
# print(friends_unwatched_list_with_genre)
# frequent_genre = get_most_watched_genre(user_data)
# print("****** Frequent Genre ********")
# print(frequent_genre)
# final_recommendations = []
# if friends_unwatched_list_with_genre and user_data["watched"]:
#     for movie in friends_unwatched_list_with_genre:
#         print("****** MOVIE *********")
#         print(movie)
#         if movie["genre"] == frequent_genre:
#             final_recommendations.append(movie) 
# print(final_recommendations)



# print(get_friends_unique_watched(user_data))
# # print(get_available_recs(user_data))

# # ************* WAVE 4 ******************   
# # def get_available_recs(user_data):
# friends_unwatched_list = get_friends_unique_watched(user_data)
# print("***** FRIENDS Unwatched List ***********")
# print(friends_unwatched_list)
# # Add Host to friends_unwatched_list
# friends_unwatched_list_with_host = helper_add_key_to_movie_dict(friends_unwatched_list, "host", user_data)
# print("************ Available Services *******")
# available_services = user_data["subscriptions"]
# print(available_services)
# final_recommendations = []
# for movie in friends_unwatched_list_with_host:
#     if movie["host"] in available_services:
#         final_recommendations.append(movie)
# print("********** Final Rec ***********")
# print(final_recommendations)

# ************** WAVE 5.2 ******************
# def  get_rec_from_favorites(user_data):
# user_not_in_friends_list = get_unique_watched(user_data)
# # favorites_set = user_data["favorites"]

# print(user_not_in_friends_list)
# # friends_unwatched_list_with_genre = helper_add_key_to_movie_dict(friends_unwatched_list, "genre", user_data)
# final_recommendations = []
# if user_not_in_friends_list and user_data["favorites"]:
#     for movie in user_not_in_friends_list:
#         print(movie)
#         print(user_data["favorites"])
#         if movie in user_data["favorites"]:
#             final_recommendations.append(movie) 
# print(final_recommendations)

def get_unique_watched(user_data):
    # Step 1: Get combined friend's watched list
    # combined_friends = set(helper_combined_friends_list(user_data))
    # Step 1: Get combined friend's watched list
    combined_friends = set()
    for friend in user_data["friends"]:
        for friend_watched in friend["watched"]:
            combined_friends.add(friend_watched["title"])
    # Step 2: Get User's watched list
    watched_set = set()
    for movie_watched in user_data["watched"]:
        watched_set.add(movie_watched["title"])
    # Step 3: Find user's difference with Friend's
    unique_watched_set = watched_set.difference(combined_friends)
    # Step 4: Convert to Dictionary
    unique_watched_list = []
    for item in unique_watched_set:
        title_dict = {"title": item}
        unique_watched_list.append(title_dict)
    return unique_watched_list

print(get_unique_watched(user_data))



combined_friends = []
for friend in user_data["friends"]:
    for friend_watched in friend["watched"]:
        combined_friends.append(friend_watched["title"])
print(combined_friends)

print("combined Friends function")
print(helper_combined_friends_list(user_data))

