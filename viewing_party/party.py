
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



### WAVE 5 ###

def get_new_rec_by_genre(user_data):
    
  #most watched function has genre, return genre most watched
  #from find the movies in the users watched that match this genre and add to list if USER has not watched, one FRIEND has watch
  
  user_fave_genre = get_most_watched_genre(user_data)
  friends_watched_list = get_friends_unique_watched(user_data)
  new_rec_list = []
  
  
  if len(friends_watched_list) == 0:
    return new_rec_list
  
  for movie_dict in friends_watched_list:
    # the following is comparing two strings
    if user_fave_genre == movie_dict["genre"]:
      new_rec_list.append(movie_dict)
  
  return new_rec_list



  
def get_rec_from_favorites(user_data):
  # from users favorite movies, return list of movie dictionaries that none of user's friends have watched
  
  recommended_movies_list = []
  favorites_list = user_data["favorites"]
  friends_not_watched_list = get_unique_watched(user_data)
  
  for movie_dict in favorites_list:
    if movie_dict in friends_not_watched_list:
      recommended_movies_list.append(movie_dict)
  
  return recommended_movies_list

