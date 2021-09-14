##Wave 1!!


def create_movie(title,genre,rating):
    
    if bool(title)==True and bool(genre)==True and bool(rating)==True:
        dict={"title":"Title A","genre":"Horror","rating":3.5}
        return dict
    else:
        return None

def add_to_watched(user_data,movie):
   
    #user_data={'watched':[{},{},{}]}
    #movie={"title": "Title A", "genre": "Horror", "rating": 3.5}
    watched=user_data['watched']
    watched.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #user_data=dictionary with a key `"watchlist"`, 
    #and a value which is a list of dictionaries representing the movies the user wants to watch
    #user_data={'watchlist':[{}{}{}]}
    watchlist=user_data['watchlist']
    watchlist.append(movie)
    return user_data
  
def watch_movie(user_data,title):
       #user_data={'watchlist':[{}{}{}], 'watched':[{}{}{}]}
    list=[]
    to_watch_movies=user_data['watchlist']
    for i in range(len(to_watch_movies)):
      to_watch_movie=to_watch_movies[i]['title']
      list.append(to_watch_movie)

    if title in list:
        #i have to remove and add the movie corresponding to this title
        movie_index=list.index(title)
        x=to_watch_movies.pop(movie_index)
        already_watched_movie=user_data['watched']
        already_watched_movie.append(x)
        return user_data
    else: 
        return user_data

## WAVE 2 !!!


def get_watched_avg_rating(user_data):
    #user_data={'watched'=[{},{},{}]}
    list_of_ratings=[]
    watchedlist=user_data['watched']
    for i in range(len(watchedlist)):
      rating=user_data['watched'][i]['rating']
      list_of_ratings.append(rating)
    if len(watchedlist)==0:
      avg_rating=0.0
    else:
      avg_rating=sum(list_of_ratings)/len(watchedlist)
    
    return avg_rating


def get_most_watched_genre(user_data):
    #user_data={'watched'=[{'genre'},{}]}
    list_of_genres=[]
    watchedlist=user_data['watched']
    for i in range(len(watchedlist)):
      genre=user_data['watched'][i]['genre']
      list_of_genres.append(genre)
    thisset=set(list_of_genres)
    count_list=[]
    genre_list=[]
    for i in range(len(thisset)):
      each_genre=list_of_genres[i]
      Count=list_of_genres.count(each_genre)
      genre_list.append(each_genre)
      count_list.append(Count) #i want this to reflect the actual genre not the number
    if len(watchedlist)==0:
      return None
    else:
      most_frequent=max(count_list)
      index_of_most_frequent=count_list.index(most_frequent)
      max_genre=genre_list[index_of_most_frequent]
      return max_genre

def get_unique_watched(user_data):
  #user_data={'watched':[{},{}],'friends':[{'watched':[{'title':,'genre':,'rating':},{}]},{}]

  user_watched=user_data['watched']
  #which will return a list of dictionaries of my films
  #i will then loop through to get all titles

  user_watched_titles=[]
  for i in range(len(user_watched)):
      user_watched_title=user_watched[i]
      user_watched_titles.append(user_watched_title)

  friends_watched_titles=[]
  friends_watched=user_data['friends']
  for j in range(len(friends_watched)):
    friend_ind_watched=friends_watched[j]['watched']
    for k in range(len(friend_ind_watched)):
      friends_watched_titles.append(friend_ind_watched[k])
  unique_watched=[]
  for title in user_watched_titles:
    if title not in friends_watched_titles:
      unique_watched.append(title)
  
  return unique_watched

def get_friends_unique_watched(user_data):
  
  user_watched=user_data['watched']
  #which will return a list of dictionaries of my films
  #i will then loop through to get all titles

  user_watched_titles=[]
  for i in range(len(user_watched)):
      user_watched_title=user_watched[i]
      user_watched_titles.append(user_watched_title)

  friends_watched_titles=[]
  friends_watched=user_data['friends']
  for j in range(len(friends_watched)):
    friend_ind_watched=friends_watched[j]['watched']
    for k in range(len(friend_ind_watched)):
      friends_watched_titles.append(friend_ind_watched[k])

  unique_watched=[]
  for title in friends_watched_titles:
    if title not in user_watched_titles:
      if title not in unique_watched:
        unique_watched.append(title)

  return unique_watched

def get_available_recs(user_data):

  recommended_movies=[]
  friends_movies=[]
  hosts=[]
  friends_final_list=[]
  watched_final_list=[]
  for i in range(len(user_data['friends'])):
    friends_watched=user_data['friends'][i]['watched']
    for j in range(len(friends_watched)):
        friends_watched_host=friends_watched[j]['host']
        hosts.append(friends_watched_host)
        friends_watched_title=friends_watched[j]['title']
        friends_movies.append(friends_watched_title)
        friends_final_list.append(friends_watched[j])
  for p in range(len(user_data['watched'])):
    watched=user_data['watched'][p]['title']
    watched_final_list.append(watched)

  for movie in friends_final_list:
   index=friends_final_list.index(movie)
   host=hosts[index]
   if host in user_data['subscriptions']: 
     if not movie['title'] in watched_final_list and not movie in recommended_movies:
        recommended_movies.append(movie)
  return recommended_movies

def get_new_rec_by_genre(user_data):
  recommended_movies=[]
  friends_movies=[]
  genres=[]
  friends_final_list=[]
  watched_final_list=[]
  for i in range(len(user_data['friends'])):
    friends_watched=user_data['friends'][i]['watched']
    for j in range(len(friends_watched)):
        friends_watched_genre=friends_watched[j]['genre']
        genres.append(friends_watched_genre)
        friends_watched_title=friends_watched[j]['title']
        friends_movies.append(friends_watched_title)
        #why do i need this next part? it's a list of all titles and hosts, basically movies that friends watched
        friends_final_list.append(friends_watched[j])
  for p in range(len(user_data['watched'])):
    watched=user_data['watched'][p]['title']
    watched_final_list.append(watched)
  for movie in friends_final_list:
   index=friends_final_list.index(movie)
   genre=genres[index]
   most_watched_genre=get_most_watched_genre(user_data)
   if genre==most_watched_genre:
    if not movie['title'] in watched_final_list and not movie in recommended_movies:
        recommended_movies.append(movie)
  return recommended_movies

def get_rec_from_favorites(user_data):
 recommended_list=[]
 unique_watched=get_unique_watched(user_data)

 for movie in unique_watched:
   if movie in user_data['favorites']:
     recommended_list.append(movie)
 return recommended_list