
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