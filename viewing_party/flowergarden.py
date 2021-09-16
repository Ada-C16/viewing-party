#Wave one
def create_movie(title, genre, rating):
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if title == None or genre == None or rating == None:
        return None
    else:
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
  for movie_data in user_data["watchlist"]:
    if movie_data ["title"] == title:
      user_data["watched"].append(movie_data)
      user_data["watchlist"].remove(movie_data)
  return user_data 

#Wave two
def get_watched_avg_rating(user_data):
    all_movie_ratings = []

    for each_rating in user_data["watched"]:
        all_movie_ratings.append(each_rating["rating"])

    if len(all_movie_ratings) == 0:
      return 0.0

    average_rating_of_all = sum(all_movie_ratings)/len(all_movie_ratings)
    return average_rating_of_all

def get_most_watched_genre(user_data):
  genre_map = {}

  for genre in user_data["watched"]:
    if genre["genre"] not in genre_map:
        genre_map[genre["genre"]] = 1 
    else:
        genre_map[genre["genre"]] += 1

  if len(user_data["watched"]) == 0:
    return None

  max_key = max(genre_map, key=genre_map.get)
  return max_key

#Wave Three
def get_unique_watched(user_data):
    # user_watched_list = {}
    # unique_data = []
  
    # x = 1
    # for friends_watched in user_data['friends']:
    #     for y in friends_watched['watched']:
    #         user_watched_list[y['title']] = y['title']
    user_watched_list = {y['title']: y['title'] for friends_watched in user_data['friends'] for y in friends_watched['watched']}
    
    # for r in user_data['watched']:
    #     for k, v in r.items():
    #         if v not in user_watched_list.keys():
    #             unique_data.append(r)
    unique_data = [r for r in user_data['watched'] for k, v in r.items() if v not in user_watched_list.keys()]
    return unique_data  


def get_friends_unique_watched(user_data):
    user_watched_list = {}
    unique_data = []
  
    x = 1
    for watched in user_data['watched']:
        user_watched_list[watched['title']] = watched['title']

    for x in user_data['friends']:
        for y in x['watched']:
            if y.values() in user_watched_list.keys():
               unique_data.append(y)   


    return unique_data 

def get_friends_unique_watched(user_data):
    user_watched_list = {}
    unique_data = []
  
    x = 1
    for watched in user_data['watched']:
        user_watched_list[watched['title']] = watched['title']

    for each_friend in user_data['friends']:
        if len(each_friend['watched']) > 0:
            for x in each_friend['watched']:
                for k, v in x.items():
                    if v not in user_watched_list.keys():
                        unique_data.append(v)
           
    set1 = set(unique_data)
    list1 = list(set1)
    final = []
    for x in list1:
        dict1 = {'title': x}
        final.append(dict1)

    return final  

#wave 4 
                      
def get_available_recs(user_data):
    user_dict_sub = {}
    user_dict_watched = {}
    recomendations = []

    #creating dictionaires for user data
    counter = 0
    for subscription in user_data['subscriptions']:
        user_dict_sub[counter] = subscription 
        counter += 1
    x = 0
    for watched in user_data['watched']:
        for k, v in watched.items():
            user_dict_watched[x] = v
            x += 1

    #getting recomendations
    for friend in user_data['friends']:
        for watch in friend['watched']:
            if watch['host'] in user_dict_sub.values() and watch['title'] not in user_dict_watched.values() and watch not in recomendations:
                recomendations.append(watch)
    return recomendations

#Wave five
def get_new_rec_by_genre(user_data):
    genre_map = {}
    if len(user_data['watched']) == 0:
        return []
    else:

        for genre in user_data["watched"]:
            if genre["genre"] not in genre_map:
                genre_map[genre["genre"]] = 1 
            else:
                genre_map[genre["genre"]] += 1

        max_key = max(genre_map, key=genre_map.get)
        
        users_watched_dict = {}
        for title in user_data['watched']:
            users_watched_dict[title['title']] = title['title']
        
        recomendations = []
        for friends_watched in user_data['friends']:
            for watch in friends_watched['watched']:
                if watch['title'] not in users_watched_dict and watch['genre'] == max_key and watch not in recomendations:
                    recomendations.append(watch)
        return recomendations

def get_rec_from_favorites(user_data):
    if len(user_data['favorites']) == 0:
        return []
    else:
        friend_watch_dict = {}
        
        for friend in user_data['friends']:
            for friend_watch in friend['watched']:
                friend_watch_dict[friend_watch['title']] = friend_watch['title']

        recomendations = []
        for fav in user_data['favorites']:
            if fav['title'] not in friend_watch_dict:
                recomendations.append(fav)

        return recomendations
