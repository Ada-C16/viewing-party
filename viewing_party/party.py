
#### WAVE 1
# user_data = {}

def create_movie(movie_title, genre, rating):  
  new_movie = {}
  
  if not movie_title or not genre or not rating:
    return None  
  else:
    new_movie["title"] = movie_title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
  return new_movie


def add_to_watched(user_data, movie):

  if not "watched" in user_data:
    user_data["watched"] = [movie]
  else: 
    user_data["watched"].append(movie)
  return user_data
  


def add_to_watchlist(user_data, movie):
  updated_dict = user_data
  
  if not "watchlist" in user_data:
    user_data["watchlist"] = [movie]
  else: 
    user_data["watchlist"].append(movie)
    
  return user_data


def watch_movie(user_data, title):
  
  movie_found = False
  index_to_be_removed = -1  # set to -1 bcs invalid, can't set it to other bcs those would be valid
  
  for index, temp_movie_dict in enumerate(user_data["watchlist"]):
    if temp_movie_dict["title"] == title: #found movie to be removed
      index_to_be_removed = index #the index of the movie
      movie_found = True
      user_data["watched"].append(temp_movie_dict)
    
  if movie_found:
    user_data["watchlist"].pop(index_to_be_removed)
    
  return user_data



    
# ##### WAVE 2

def get_watched_avg_rating(user_data):
  user_rating_total = 0.0
  average = 0.0
  watched_list = user_data["watched"]
  
  if watched_list != []:
    for movie_dict in watched_list:
      user_rating_total += movie_dict["rating"] 
    average = user_rating_total / len(watched_list)
  return average

      
def get_most_watched_genre(user_data):
  popular_genre_list = []
  count = 0
  watched_list = user_data["watched"]
  popular_genre = None
  
  
  if watched_list != []:
    for movie_dict in watched_list:
      popular_genre_list.append(movie_dict["genre"])
      
    for genre_name in popular_genre_list:
      
      if popular_genre_list.count(genre_name) > count:
        count = popular_genre_list.count(genre_name)
        popular_genre = genre_name
  
  return popular_genre


#### WAVE 3

# def get_unique_watched(user_data):
  
#   friends_list = user_data
#   user_movies_list = []
#   friends_movies_list = []
#   user_unique_movies = []
#   friends_unique_movies = {}
#   friends_movie_dict_list = user_data["friends"]


#   for friends_dict in friends_movie_dict_list:
#     for movie_watched_list in friends_dict["watched"]:
#       friends_movies_list.append(movie_watched["title"])

#   for movie_dict in user_data["watched"]:
#     if movie_dict["title"] not in friends_unique_movies:
#       user_unique_movies.append(movie_dict)
      
#   return user_unique_movies

        
def get_unique_watched(user_data):
    
    #Determine which movies the user has watched, but none of their friends have watched.
  
  friends_list = user_data
  user_movies_list = []
  friends_movies_list = []
  user_unique_movies = []
  friends_unique_movies = {}
  friends_movie_dict_list = user_data["friends"]


  for friends_dict in friends_movie_dict_list:
    for movie_watched_dict in friends_dict["watched"]:
        friends_movies_list.append(movie_watched_dict["title"])

  for movie_dict in user_data["watched"]:
      #if users movie is not in the friends list
    if movie_dict["title"] not in friends_movies_list:
      user_unique_movies.append(movie_dict)
      
  return user_unique_movies


def get_friends_unique_watched(user_data):
    
    #Determine which movies at least one of the user's friends have watched, but the user has not watched.
    
  friends_list = user_data
  user_movies_list = []
  friends_movies_list = []
  user_unique_movies = []
  friends_unique_movies = []
  the_friends_with_movie_dict_list = user_data["friends"]
  


#looping thr movie list to get to dictionary to append movie title
  for movie_dict in user_data["watched"]:
      user_movies_list.append(movie_dict["title"])

  for friends_dict in the_friends_with_movie_dict_list:
      for movie_watched_dict in friends_dict["watched"]:
          if movie_watched_dict["title"] not in user_movies_list:
              if movie_watched_dict not in friends_unique_movies:
                  friends_unique_movies.append(movie_watched_dict)
  
  return friends_unique_movies


#wave 4

def get_available_recs(user_data):
    
    host_list = []
    
    recommendation_list = []
    
    subscription_list = user_data["subscriptions"]
    
    user_not_watched_list = get_friends_unique_watched(user_data)
    
    for movie_dict in user_not_watched_list:
        if movie_dict["host"] in subscription_list:
            recommendation_list.append(movie_dict)
    
    return recommendation_list



  
#################################################

# amandas_data = {
# "watched": [
# {
# "title": "Title A"
# },
# {
# "title": "Title B"
# },
# {
# "title": "Title C"
# },
# {
# "title": "Title D"
# },
# {
# "title": "Title E"
# },
# ],
# "friends": [
# {
# "watched": [
# {
# "title": "Title A"
# },
# {
# "title": "Title C"
# }
# ]
# },
# {
# "watched": [
# {
# "title": "Title A"
# },
# {
# "title": "Title D"
# },
# {
# "title": "Title F"
# }
# ]
# }
# ]
# }

# Act
amandas_unique_movies = get_unique_watched(amandas_data)

print(amandas_unique_movies)




# janes_data = {
#     "watched": [
#         {
#             "title": "Title A",
#             "genre": "Fantasy"
#         },
#         {
#             "title": "Title B",
#             "genre": "Intrigue"
#         },
#         {
#             "title": "Title C",
#             "genre": "Intrigue"
#         },
#         {
#             "title": "Title D",
#             "genre": "Fantasy"
#         },
#         {
#             "title": "Title E",
#             "genre": "Intrigue"
#         },
#     ]
# }

# # Act
# popular_genre = get_most_watched_genre(janes_data)
# print(popular_genre)


#     # Watched Adding
# movie1 = create_movie("Title 1","Horror",3.5)
# movie2 = create_movie("Title 2","Horror",3.5)
# user_data = add_to_watched(user_data, movie1)
# user_data = add_to_watched(user_data, movie2)
# #Watchlist adding
# movie3 = create_movie("Title B","Horror",3.5)
# movie4 = create_movie("Title C","Comedy",6.0)
# user_data = add_to_watchlist(user_data, movie3)
# user_data = add_to_watchlist(user_data, movie4)
# #removing from watchlist and adding to Watched
# #expect Title b to be removed watchlist and added to watched
# user_data = watch_movie(user_data, "Title B")
# user_data = watch_movie(user_data, "Title Z")
# print()
# # movie = create_movie(movie_title, genre, rating)
# user_data = {"watchlist": [{"title": "Babe",
# "genre": "comedy", "rating": 1},{"title": "Startrek","genre":"scifi","rating": 1},{"title":"Cheers","genre": "drama","rating": 1} ], "watched": [{"title": "Starwars", "genre": "scifi","rating": 5}, {"title":"Matrix","genre": "scifi","rating": 3},{"title" : "Billboard","genre":"drama","rating": 1}]}
# user_data = {"watchlist": [{"title": "Babe",
# "genre": "comedy", "rating": 1},{"title": "Startrek","genre":"scifi","rating": 1},{"title":"Cheers","genre": "drama","rating": 1} ], "watched": [{"title": "Starwars", "genre": "scifi","rating": 5}, {"title":"Matrix","genre": "scifi","rating": 3},{"title" : "Billboard","genre":"drama","rating": 1}], "friends": [
#             {
#                 "watched": [
#                     {
#                         "title": "argosy"
#                     },
#                     {
#                         "title": "startrek"
#                     }
#                 ]
#             },
#             {
#                 "watched": [
#                     {
#                         "title": "Babe"
#                     },
#                     {
#                         "title": "Cheers"
#                     },
#                     {
#                         "title": "starwars"
#                     }
#                 ]
#             }
#         ]}