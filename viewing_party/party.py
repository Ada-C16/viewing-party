# Wave 1

def create_movie(title, genre, rating):
    create_movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if title and genre and rating:
      return create_movie_dict 
    else:
      return None

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    add_watchlist = user_data["watchlist"]
    add_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if title == movie['title']:
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
    return user_data


# Wave 2

def get_watched_avg_rating(user_data):
    pass
    if len(user_data['watched']) > 0:
      sum_rating = 0
      for movie in user_data['watched']:
        rating = movie['rating']
        sum_rating += rating 
      
      return sum_rating/len(user_data['watched'])
    else:
      return 0.0

def get_most_watched_genre(user_data):
    pass
    genres = []
    if len(user_data['watched']) > 0:
        for movie in user_data['watched']:
            for genre in movie['genre']:
                genre = movie['genre']
                genres.append(genre)
    
        most_common = max(genres, key = genres.count)
        return most_common
    elif len(user_data['watched']) == 0:
        return None 

# Wave 3

def get_unique_watched(user_data):
    user_list = []
    friends_list = []
    final_list = []
    for movies in user_data['friends']:
        for movie in movies['watched']:
            friends_list.append(movie)
    for movie in user_data['watched']:
        user_list.append(movie)
    for movie in user_list:
        if movie not in friends_list:
            final_list.append(movie)

    return final_list
def get_friends_unique_watched(user_data):
    user_list = []
    friends_list = []
    final_list = []
    
    for movies in user_data['friends']:
        for movie in movies['watched']:
            friends_list.append(movie)
    for movie in user_data['watched']:
        user_list.append(movie)
    for movie in friends_list:
        if movie not in user_list and movie not in final_list:
            final_list.append(movie)
    return final_list
    

#Wave 4


# def get_friends_movies(user_data):
#     titles = set()
#     friends = user_data['friends']
#     movies = []
#     for friend in friends:
#         for movie in friend['watched']:
#             if movie['title'] not in titles:
#                 movies.append(movie)
#                 titles.add(movie['title'])
#     return movies 

def get_available_recs(user_data):
    pass
    friends_watch_list = get_friends_unique_watched(user_data)
    recommended_movies = []

    if len(friends_watch_list) == 0:
        return []
    
    titles_of_movies_user_watched =set()
    for movie in user_data['watched']:
        titles_of_movies_user_watched.add(movie['title'])

    for movie in friends_watch_list:
        if movie['title'] not in titles_of_movies_user_watched:
            if movie['host'] in user_data['subscriptions']:
                recommended_movies.append(movie) 
    return recommended_movies

# Wave 5

def get_genres(user_data):
  genres = []
  for movie in user_data['watched']:
      genres.append(movie['genre'])
  return genres

def get_freq_genre(user_data):
  pass
  genres_list = get_genres(user_data)
  return max(set(genres_list), key = genres_list.count)

def get_new_rec_by_genre(user_data):
  pass
  rec_list = []

  if len(user_data['watched']) == 0:
      return rec_list
  for friends in user_data['friends']:
      for movies in friends['watched']:
        if movies['genre'] == get_freq_genre(user_data) and movies not in rec_list:
            rec_list.append(movies)
 
  return rec_list

def get_rec_from_favorites(user_data):
  pass
  rec_list = []
  friend_movies = []
  friends = user_data['friends']
  
  if len(user_data['favorites']) == 0:
    return rec_list
  
  for movies in friends:
    for movie in movies['watched']:
      friend_movie = movie 
      friend_movies.append(friend_movie)
      

  for user_movie in user_data['watched']:
    
    if user_movie not in friend_movies and user_movie in user_data['favorites']:
      rec_list.append(user_movie)
  
  return rec_list