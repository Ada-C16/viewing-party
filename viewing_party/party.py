from collections import Counter


# WAVE 1
def create_movie(movie_title, genre, rating):
    new_movie = None
    if movie_title and genre and rating:
        new_movie = {}
        new_movie["title"] = movie_title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
  for movie in user_data["watchlist"]:
    if movie["title"]==title:
      user_data["watched"].append(movie)
      user_data["watchlist"].remove(movie)
  
  return user_data



# WAVE 2
def get_watched_avg_rating(user_data):
    average = 0.0
    watched = user_data["watched"]
    count = 0
    while watched:
        for movie in watched:
            average += movie["rating"]
            count += 1
        average = average/count
        return average
    return average

def get_most_watched_genre(user_data):
    
    watched = user_data["watched"]
    genre_list = []
    while watched:
        for i in range(len(watched)):
            genre_list.append(watched[i]["genre"])

        word_counts = Counter(genre_list)
        popular_genre = word_counts.most_common(1)[0][0]

        return popular_genre
    return None
        


#WAVE 3
def get_unique_watched(user_data):
    watched = user_data["watched"]
    friends_watched = user_data["friends"]

    user_data_list = []
    friends_watched_list_pre = []
    friends_watched_list_final = []
   
    unique_movie_list = []
   
    for i in range(len(watched)):
        user_data_list.append(watched[i])
   
    for j in range(len(friends_watched)):
        friends_watched_list_pre.append((friends_watched[j]["watched"]))
   
    for k in range(len(friends_watched_list_pre)):
        friends_watched_list_final += friends_watched_list_pre[k]

    for movie in user_data_list:
        if not movie in friends_watched_list_final:
            unique_movie_list.append(movie)

    return unique_movie_list

def get_friends_unique_watched(user_data):
    watched = user_data["watched"]
    friends_watched = user_data["friends"]

    user_data_list = []
    friends_watched_list_pre = []
    friends_watched_list_final = []
   
    unique_movie_list_friends = []
   
    for i in range(len(watched)):
        user_data_list.append(watched[i])
   
    for j in range(len(friends_watched)):
        friends_watched_list_pre.append((friends_watched[j]["watched"]))
   
    for k in range(len(friends_watched_list_pre)):
        friends_watched_list_final += friends_watched_list_pre[k]

    friends_list_no_duplicates = []
    for i in friends_watched_list_final:
        if i not in friends_list_no_duplicates:
            friends_list_no_duplicates.append(i)
           
    for movie in friends_list_no_duplicates:
        if not movie in user_data_list:
            unique_movie_list_friends.append(movie)

    return unique_movie_list_friends



# WAVE 4
def get_available_recs(user_data):
    pre_recommendations = []
    
    final_recommendations = []
    friends_movies = user_data["friends"]
    friends_watched_list = []
    user_watched_movies = user_data["watched"]

    for friends_watched_dict in friends_movies:
        for key, value in friends_watched_dict.items():
            for movie in value:
                friends_watched_list.append(movie)

   
    for recommendation in friends_watched_list:
      for subscription in user_data["subscriptions"]:
        if recommendation["host"] == subscription:
          pre_recommendations.append(recommendation)

    for unique_movie in pre_recommendations:
      if unique_movie not in final_recommendations:
        final_recommendations.append(unique_movie)
    
    if user_watched_movies: 
      for movie in user_watched_movies:
        for recom in final_recommendations: 
          if movie["title"] in recom["title"]:
            final_recommendations = []       
          else:
            final_recommendations = []
            final_recommendations.append(recom)
   
    return final_recommendations



# WAVE 5
def get_new_rec_by_genre(user_data):
    most_frequent = get_most_watched_genre(user_data)
    #print(type(most_frequent))
    
    recommendations = []
    recommendations_final = []
    friends_movies = user_data["friends"]
    friends_watched_list = []
    user_watched_movies = user_data["watched"]

    for friends_watched_dict in friends_movies:
        for key, value in friends_watched_dict.items():
            for movie in value:
                friends_watched_list.append(movie)
    # print(friends_watched_list)
    if user_watched_movies:
      for friends_movie in friends_watched_list:
        for movie in user_watched_movies:
          if not friends_movie["title"] == movie["title"]:
            if friends_movie["genre"] == most_frequent:
              recommendations.append(friends_movie)
    for recommendation in recommendations:
      if recommendation not in recommendations_final:
        recommendations_final.append(recommendation)
    
    return recommendations_final

def get_rec_from_favorites(user_data):
    recommended = []
    friends_movies = user_data["friends"]
    friends_watched_list = []

    if not user_data['favorites']:
        return recommended
    else:
        for friends_watched_dict in friends_movies:
            for key, value in friends_watched_dict.items():
                for movie in value:
                    friends_watched_list.append(movie)
        for movie in user_data['favorites']:
          if movie not in friends_watched_list:
            recommended.append(movie)
    return recommended
    


