user_data = {
        "watched": [
            {
                "title": "Title A",
                "genre": "Intrigue"
            },
            {
                "title": "Title B",
                "genre": "Intrigue"
            },
            {
                "title": "Title C",
                "genre": "Fantasy"
            }
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title D",
                        "genre": "Intrigue"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title C",
                        "genre": "Fantasy"
                    },
                    {
                        "title": "Title E",
                        "genre": "Intrigue"
                    }
                ]
            }
        ]
    }

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

# *********** WAVE 3 ********************
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


# *************** WAVE 4 *********************
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
    return updated_movie_list

friends_unwatched_list = get_friends_unique_watched(user_data)
print(friends_unwatched_list)
print(helper_add_key_to_movie_dict(friends_unwatched_list, "genre", user_data))





# def get_available_recs(user_data):
#     friends_unwatched_list = get_friends_unique_watched(user_data)
#     available_services = user_data["subscriptions"]
#     final_recommendations = []
#     for movie in friends_unwatched_list:
#         if movie["host"] in available_services:
#             final_recommendations.append(movie)
#     return final_recommendations

# print(get_friends_unique_watched(user_data))

# # def get_friends_unique_watched(user_data):
# # Step 1: Get combined friend's watched list
# combined_friends_title_only = set() # originally set()
# combined_friends_list = []
# for friend in user_data["friends"]:
#     for friend_watched in friend["watched"]:
#         combined_friends_title_only.add(friend_watched["title"])
#         combined_friends_list.append(friend_watched)
# # Step 2: Get User's watched list
# user_watched_set = set()
# for movie_watched in user_data["watched"]:
#     user_watched_set.add(movie_watched["title"])
# # Step 3: Find Friend's difference with Users's
# unique_watched_set = combined_friends_title_only.difference(user_watched_set)
# # Step 4: Convert set to list of dictionaries & Find Source
# unique_watched_list = []
# for item in unique_watched_set:
#     # Find Host since this was lost in the set
#     # return NONE for host 
#     # Try block to cover cases when Host is not provided in friend's dataset
#     try:
#         for movie in combined_friends_list:
#             if movie["title"] == item:
#                 host = movie["host"]
#                 movie_dict = {"title": item, "host": host}
#                 unique_watched_list.append(movie_dict)
#                 break  # Breaking to avoid adding multiple times if duplicates in combined_friends_list
#     except KeyError:
#         movie_dict = {"title": item}
#         unique_watched_list.append(movie_dict)
# print(unique_watched_list)