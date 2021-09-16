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



# # ***** Converting WAVE 3 to return host in dictionary as Well *******

# # Step 1: Get combined friend's watched list
# z = ("title", "Title A")

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

# # # Step 4: Convert set to list of dictionaries & Find Source
# unique_watched_list = []

# for item in unique_watched_set:
#     # Find Host since this was lost in the set
#     for movie in combined_friends_list:
#         if movie["title"] == item:
#             host = movie["host"]
#     movie_dict = {"title": item, "host": host}
#     unique_watched_list.append(movie_dict)

# print(unique_watched_list)
# >>> my_dict = {"a": 1, "b": 2}
# >>> my_dict.items()
# dict_items([('a', 1), ('b', 2)])
# >>> tuple(my_dict.items())
# (('a', 1), ('b', 2))
# >>> set(tuple(my_dict.items()))
# {('b', 2), ('a', 1)}
# >>> my_tuple = tuple(my_dict.items())
# >>> dict(my_tuple)
# {'a': 1, 'b': 2}

# print(get_friends_unique_watched(user_data))

def get_friends_unique_watched(user_data):
    # Step 1: Get combined friend's watched list
    combined_friends_title_only = set() # originally set()
    combined_friends_list = []
    for friend in user_data["friends"]:
        for friend_watched in friend["watched"]:
            combined_friends_title_only.add(friend_watched["title"])
            combined_friends_list.append(friend_watched)
    # Step 2: Get User's watched list
    user_watched_set = set()
    for movie_watched in user_data["watched"]:
        user_watched_set.add(movie_watched["title"])
    # Step 3: Find Friend's difference with Users's
    unique_watched_set = combined_friends_title_only.difference(user_watched_set)
    # Step 4: Convert set to list of dictionaries & Find Source
    unique_watched_list = []
    for item in unique_watched_set:
        # Find Host since this was lost in the set
        # Try block to cover cases when Host is not provided in friend's dataset
        try:
            for movie in combined_friends_list:
                if movie["title"] == item:
                    host = movie["host"]
                    movie_dict = {"title": item, "host": host}
                    unique_watched_list.append(movie_dict)
                    break  # Breaking to avoid adding multiple times if duplicates in combined_friends_list
        except KeyError:
            movie_dict = {"title": item}
            unique_watched_list.append(movie_dict)
    return unique_watched_list


# # # # ********************** WAVE 4 ******************
# def get_available_recs(user_data):
    # friends_unwatched_list = get_friends_unique_watched(user_data)
    # print(friends_unwatched_list)
    # for movie in friends_unwatched_list:
    #     print(movie)
    # available_services = user_data["subscriptions"]
    # final_recommendations = []
    # # print(available_services)
    # # print(friends_unwatched_list)
    # for movie in friends_unwatched_list:
    #     if movie["host"] in available_services:
    #         final_recommendations.append(movie)
    # # print("******** FINAL RESULT *********")
    # return(final_recommendations)

# ********************** WAVE 5 ***********************
def get_available_recs(user_data):
    friends_unwatched_list = get_friends_unique_watched(user_data)
    available_services = user_data["subscriptions"]
    final_recommendations = []
    for movie in friends_unwatched_list:
        if movie["host"] in available_services:
            final_recommendations.append(movie)
    return final_recommendations

def get_most_watched_genre(user_data):
    # Create Frequency Table
    frequency_table = {}
    for movie in user_data["watched"]:
        if movie["genre"] in frequency_table:
            print(movie["genre"])
            frequency_table[str(movie["genre"])] += 1
        else:
            print(movie["genre"])
            frequency_table[str(movie["genre"])] = 1
    # Find Max Value
    current_high = -1  # TODO: Might need to return None if watched is empty
    max_genre = None  # TODO: Might need to change this to a list for ties
    for genre, frequency in frequency_table.items():
        if frequency > current_high:
            current_high = frequency
            max_genre = genre
    return(max_genre)



friends_unwatched_list = get_friends_unique_watched(user_data)
frequent_genre = get_most_watched_genre(user_data)
final_recommendations = []
if friends_unwatched_list and user_data["watched"]: 
    for movie in friends_unwatched_list:
        print(movie)
#         if movie["genre"] == frequent_genre:
#             final_recommendations.append(movie)
# print(final_recommendations)


