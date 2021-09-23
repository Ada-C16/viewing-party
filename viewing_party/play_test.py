# # def get_available_recs(user_data):
    
#     # Create an empty list that can hold all of the movie recommendations
#     # from viewing_party.party import get_new_rec_by_genre


# # recommended_movies = []

#     # Figure out which movies each friend has watched
#     # user_data["friends"] gives you a list of friend-dictionaries
#     # Looping through 1 gives you a friend

#     # for friend in user_data["friends"]:
#     #     for movie in friend["watched"]:
#     #         if (movie not in user_data["watched"]) and (movie not in recommended_movies):
#     #             recommended_movies.append({"title": movie["title"], "host": movie["host"]})

#     # for friend in user_data["friends"]:
#     #     for movie in friend["watched"]:
#     #         if ({"title": movie["title"]} not in user_data["watched"]) and ({"title": movie["title"], "host": movie["host"]} not in recommended_movies):
#     #             recommended_movies.append({"title": movie["title"], "host": movie["host"]})
#     # user_subscriptions = user_data["subscriptions"]
    
#     # for friend in user_data["friends"]:
#     #     for movie in friend["watched"]:
#     #         if ({"title": movie["title"]} not in user_data["watched"]):
#     #             if movie["host"] in user_subscriptions:
#     #                 if ({"title": movie["title"], "host": movie["host"]} not in recommended_movies):
#     #                     recommended_movies.append({"title": movie["title"], "host": movie["host"]})

#     # Compare the movies that each friend has watched to the movies that user_data has watched
#     # If user_data hasn't already seen that movie, append it to the list, otherwise skip it
#     # Now, check the recommended_movies list for duplicates:
#     # If this movies is already in recommended_movies, skip it
#     # Now, check the list for hosts that the user_data doesn't have access to

#     # Look through the list of recommended_movies, it's a list of objects

#     # for each_movie in recommended_movies:
#     #     if each_movie["host"] not in user_subscriptions:
#     #         recommended_movies.remove(each_movie)

#     # If that condition matches, remove it from the list
#     # Finally, return the list
#     # print(recommended_movies)
#     # return recommended_movies


# # amandas_data = {
# # "subscriptions": ["Service A", "Service B"],
# # "watched": [],
# # "friends": [
# #     {
# #         "watched": [
# #             {
# #                 "title": "Title C",
# #                 "host": "Service C"
# #             }
# #         ]
# #     },
# #     {
# #         "watched": [
# #             {
# #                 "title": "Title D",
# #                 "host": "Service D"
# #             }
# #         ]
# #     }
# # ]
# # }

# # get_available_recs(amandas_data)


# sonyas_data = {
#     "watched": [
#         {
#             "title": "Title A",
#             "genre": "Intrigue"
#         },
#         {
#             "title": "Title B",
#             "genre": "Intrigue"
#         },
#         {
#             "title": "Title C",
#             "genre": "Fantasy"
#         }
#     ],
#     "friends": [
#         {
#             "watched": [
#                 {
#                     "title": "Title D",
#                     "genre": "Intrigue"
#                 }
#             ]
#         },
#         {
#             "watched": [
#                 {
#                     "title": "Title C",
#                     "genre": "Fantasy"
#                 },
#                 {
#                     "title": "Title E",
#                     "genre": "Intrigue"
#                 }
#             ]
#         }
#     ]
# }

# def get_most_watched_genre(user_data):
#     # Given a dictionary user_data
#     # Access the watched key, which is a list
#     # Loop through that watched list
#     # Append each genre to a genre dictionary
#     # Each genre will equal a key
#     # Set the count of each genre equal to the value of its corresponding key
#     # Return the name of the most-watched genre

#     genre_list = []
#     genre_dict = {}

#     if not user_data["watched"]:
#         return None

#     else:
#         for movie in user_data["watched"]:
#             genre_list.append(movie["genre"])

#         # Search through genre_list
#         # Count how many times each genre is listed
#         # Add it to a dictionary

#         for item in genre_list:
#             genre_dict[item] = 0

#         for item in genre_list:
#             if item in genre_dict.keys():
#                 genre_dict[item] += 1

#         most_watched = max(genre_dict, key=genre_dict.get)

#         return most_watched

# def get_new_rec_by_genre(user_data):
#     most_watched_genre = get_most_watched_genre(user_data)

#     recommended_by_genre = []
#     # [{title: title}, {host: host}]

#     # Create a list of recommended movies [{}]
#     # ------
#     # Look at the "watched" section for each friend
    
#     for friend in user_data["friends"]:
#         for movie in friend["watched"]:
#             if ({"title": movie["title"], "genre": movie["genre"]} not in user_data["watched"]):
#                 if movie["genre"] == most_watched_genre:
#                     if ({"title": movie["title"], "genre": movie["genre"]} not in recommended_by_genre):
#                         recommended_by_genre.append({"title": movie["title"], "genre": movie["genre"]})
    
#     print(recommended_by_genre)
#     return recommended_by_genre

# get_new_rec_by_genre(sonyas_data)

# def get_rec_from_favorites(user_data):
#     # If a title is in user_data favorites
#     # Return a list of dictionaries called recommendations
#     # For each friend's watched list, check whether the title in
#     # user_data watched list is present

#     recommendations = []

#     for friend in user_data["friends"]:
#         for movie in friend["watched"]:
#             for fav in user_data["favorites"]:
#                 if fav not in friend["watched"] and fav not in recommendations:
#                     recommendations.append({"title": fav["title"]})

#     print(recommendations)
#     return recommendations
def get_most_watched_genre(user_data):
    # Given a dictionary user_data
    # Access the watched key, which is a list
    # Loop through that watched list
    # Append each genre to a genre dictionary
    # Each genre will equal a key
    # Set the count of each genre equal to the value of its corresponding key
    # Return the name of the most-watched genre

    genre_list = []
    genre_dict = {}

    if not user_data["watched"]:
        return None

    else:
        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])

        # Search through genre_list
        # Count how many times each genre is listed
        # Add it to a dictionary

        # Add each genre as a new key in the dictionary with an initalized value of 0
        for item in genre_list:
            genre_dict[item] = 0
        # Go through each genre in genre_list, and count how many times it's in there
        # Add this count to the corresponding dictionary key in genre_dict
        for item in genre_list:
            if item in genre_dict.keys():
                genre_dict[item] += 1

        # Store the most_watched genre in a variable
        # Use the max function to pass two arguments
        # The first argument is the dictionary to check
        # The second argument accesses the key in genre_dict that has the highest value
        # The .get function reference accesses the value of a particular key
        most_watched = max(genre_dict, key=genre_dict.get)

        print(most_watched)
        return most_watched

janes_data = {
        "watched": [
            {
                "title": "Title A",
                "genre": "Fantasy"
            },
            {
                "title": "Title B",
                "genre": "Intrigue"
            },
            {
                "title": "Title C",
                "genre": "Intrigue"
            },
            {
                "title": "Title D",
                "genre": "Fantasy"
            },
            {
                "title": "Title E",
                "genre": "Intrigue"
            },
        ]
    }

get_most_watched_genre(janes_data)