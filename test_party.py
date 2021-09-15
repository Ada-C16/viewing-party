from viewing_party.party import *
user_data = {
        "subscriptions": ["Service A", "Service B"],
        "watched": [{"title": "Title A"}],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A",
                        "host": "Service A"
                    },
                    {
                        "title": "Title C",
                        "host": "Service C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A",
                        "host": "Service A"
                    },
                

    {
                        "title": "Title B",
                        "host": "Service B"
                    },
                    {
                        "title": "Title D",
                        "host": "Service D"
                    }
                ]
            }
        ]
    }
# def get_available_recs(user_data):
#     friend_just_watched = []
#     print("user data watched are :",user_data["watched"])
#     for friend in user_data["friends"]:
#         for friend_watched in friend["watched"]:
#             print(friend_watched)
#             if friend_watched not in user_data["watched"]:
#                 friend_just_watched.append(friend_watched)
#     return friend_just_watched
# print(get_available_recs(user_data))

print()


# def get_friends_unique_watched(user_data):
#     friend_watched_list = []
#     for friend in user_data["friends"]:
#         for friend_watched in friend["watched"]:
#             #print(f"friend watched is {friend_watched}")
#             #print("user watched movies are",user_data["watched"])
#             if friend_watched not in user_data["watched"] and\
#                 friend_watched not in friend_watched_list:
#                 friend_watched_list.append(friend_watched)
#                 #print(friend_watched_list)
#     return friend_watched_list

# print(get_friends_unique_watched(user_data))
# print("----------------------------------------------------------------------------------")


# def get_available_recs(user_data):
#     rec_movie = []
#     friend_watched_not_user = get_friends_unique_watched(user_data)
#     print("friends watched not user : ",friend_watched_not_user)
#     user_titles = []
#     for user_movie in user_data["watched"]:
#         user_titles.append(user_movie)
#         print("user titles are:",user_titles)
#     for movie in friend_watched_not_user:
#         # friend_movies.append(movie["title"])
#         # print("the title is : ",movie)
#         if movie["title"] not in user_titles :
#             if movie["host"] in user_data["subscriptions"]:
#             # and movie[] not in user_data["watched"]:
#                 rec_movie.append(movie)
#                 if user_data["watched"] in rec_movie:
#                     rec_movie.pop(user_data["watched"])
#     print("----------------------------------------------------------------------")
#     return rec_movie

# print(get_available_recs(user_data))