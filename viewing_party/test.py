# def get_most_watched_genre(user_data):
#     genre_type = {}
#     for item in user_data["watched"]:
#         if item["genre"] in genre_type:
#             genre_type[item["genre"]] += 1
#         else:
#             genre_type[item["genre"]] = 1
#     print(genre_type)
#     max_genre = []
#     for key, value in genre_type.items():
#         if value == max(genre_type, key = genre_type.get):
#             max_genre.append(key)
#     return max_genre
# user_data={
#         # "watchlist" = [{movie}, {movie}, {movie}]
#         "watched" :[{"genre":"action"}, {"genre":"love"}, {"genre":"comedy"},]
#     }    
#     # genre_type = {
#     #     "action":2
#     #     "love": 1
#     # }
# print(get_most_watched_genre(user_data))


# lst = [{"k1":[1,2]},{"k1": [3,4,5]}]
# a = [{"k1":[1,2]}, {"k1":[1,2, 3]}]
# for item in a:
#     if item in lst:
#         print("true")
#     else:
#         print("false")

# def add_to_watched(user_data, movie):
#     # user_data ={"watched": [{},{},]}
#     # user_data["watched"] = []
#     user_data["watched"].append(movie)
#     return user_data
# user_data = {
#     "watched": [{
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#     }]
# }
# movie = {
#     "title": "Title B",
#     "genre": "Adventure",
#     "rating": 2.0
# }
# update = add_to_watched(user_data, movie)
# print(len(update["watched"]))

# janes_data = {
#     "watched": [
#         {
#             "title": "Title A",
#             "genre": "Fantasy",
#             "rating": 4.8
#         },
#         {
#             "title": "Title B",
#             "genre": "Action",
#             "rating": 2.0
#         },
#         {
#             "title": "Title C",
#             "genre": "Intrigue",
#             "rating": 3.9
#         }
#     ]
# }

# def get_most_watched_genre(user_data):
#     genre_type = {}
#     for item in user_data["watched"]:
#         if item["genre"] in genre_type:
#             genre_type[item["genre"]] += 1
#         else:
#             genre_type[item["genre"]] = 1
#     return max(genre_type, key=genre_type.get)

# print(get_most_watched_genre(janes_data))
    


def get_friends_unique_watched(user_data):
    friends_watched_movie = []
    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched_movie.append(movie)
    user_watched_title = []
    for item in user_data["watched"]:
        user_watched_title.append(item["title"])
    friendswatched_usernot = []
    for item in tuple(friends_watched_movie):
        if not item["title"] in user_watched_title:
            friendswatched_usernot.append(item)
    return friendswatched_usernot

amandas_data = {
            "watched": [
                {
                    "title": "Title B"
                },
                {
                    "title": "Title C"
                }
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
                            "title": "Title E"
                        }
                    ]
                }
            ]
        }

print(get_friends_unique_watched(amandas_data))