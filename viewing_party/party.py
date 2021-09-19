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
      add_to_watched(user_data, movie_data)
      user_data["watchlist"].remove(movie_data)
  return user_data 

#Wave two
def get_watched_avg_rating(user_data):
    all_movie_ratings = [each_rating["rating"] for each_rating in user_data["watched"]]
    try:
        average_rating_of_all = sum(all_movie_ratings)/len(all_movie_ratings)
        return average_rating_of_all
    except ZeroDivisionError:
        return 0 

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
    user_watched_list = {y['title'] for friends_watched in user_data['friends'] for y in friends_watched['watched']}    
    unique_data = [r for r in user_data['watched'] if r['title'] not in user_watched_list]
    return unique_data

def get_friends_unique_watched(user_data):
    user_watched_list = []
    for friends_watched in user_data['friends']: 
        for y in friends_watched['watched']: 
            if y not in user_data['watched'] and y not in user_watched_list and y['title'] not in user_watched_list:
                user_watched_list.append(y)
    return user_watched_list 

#Wave 4                
def get_available_recs(user_data):
    recomendations = []
    watches = [x['title'] for x in user_data['watched']]
    for friend in user_data['friends']:
        for watch in friend['watched']:
            if watch['host'] in user_data['subscriptions'] and watch['title'] not in watches and watch not in recomendations:
                recomendations.append(watch)

    return recomendations

#Wave five
def get_new_rec_by_genre(user_data):
    max_key = get_most_watched_genre(user_data)
    users_watched_set = {title['title'] for title in user_data['watched']}
    recomendations = []

    for friends_watched in user_data['friends']:
        for watch in friends_watched['watched']:
            if watch['title'] not in users_watched_set and watch['genre'] == max_key and watch not in recomendations:
                recomendations.append(watch)
    return recomendations

def get_rec_from_favorites(user_data):
    friend_watch_set = {friend_watch['title'] for friend in user_data['friends'] for friend_watch in friend['watched']}
    recomendations = [fav for fav in user_data['favorites'] if fav['title'] not in friend_watch_set]
    return recomendations
