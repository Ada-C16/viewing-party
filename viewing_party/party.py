
#### WAVE 1
user_data = {}

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
  ''' Takes in two dictionaries, adds the second dictionary as a value to the first dictionary and returns the first dictionary. '''
  
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



    
#### WAVE 2

def get_watched_avg_rating(user_data):
  user_rating_list = []
  average = 0.0

  for temp_movie_dict in user_data["watched"]:
    user_rating_list.append(temp_movie_dict["rating"])
  
  if user_rating_list == []:
    return average
  else:
    average = sum(user_rating_list) / len(user_rating_list)
    return average
  
get_watched_avg_rating(user_data)
    
    
def get_most_watched_genre:(user_data):
  popular_genre_list = []
  count = 0
  
  for temp_movie_dict in user_data["watched"]:
    user_rating_list.append(temp_movie_dict["genre"])
    
    for i in popular_genre_list:
        if popular_genre_list.count(i) > count:
            count = popular_genre_list.count(i)
    popular_genre = (popular_genre_list[count])


get_most_watched_genre:(user_data)

#### WAVE 3


# movies friends have watched but user has not, return list of dictionaries

def get_unique_watched(user_data):
    user_movies_list = []
    friends_movies_list = []
    
    for temp_movie_dict in user_data["watched"]:
        user_movies_list.append(temp_movie_dict["title"])
        
    for tempt_movie_dict in user_data["friends"]:
        for friend_dict in tempt_movie_dict["watched"]:
            # for title in friend_dict["title"]:
                friends_movies_list.append(friend_dict["title"])
        
        # for title in tempt_movie_dict:       
        #     friends_movies_list.append(tempt_movie_dict[title])
    # if not "friends" in user_data:
    #     user_data["friends"] = []
    print(user_movies_list)
    print(friends_movies_list)


get_unique_watched(user_data)
  
        
  

  
#watch_movie(user_data, title)
#################################################
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

# user_data3 = {"watchlist": [{"title": "Babe",
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

