def create_movie(movie_title, genre, rating):

    if movie_title and genre and rating:
        return {"title" : movie_title, "genre" : genre, "rating" : rating}
    return None
   

def add_to_watched(user_data, movie):
  
    user_data["watched"].append(movie)
    return user_data
   
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(janes_data, Title_A):

    for each in janes_data["watchlist"]:

         if Title_A in each.values():
            janes_data["watched"].append(janes_data["watchlist"].pop())
         

    return janes_data
    

def get_watched_avg_rating(janes_data):
    
    sum_counter = 0.0
    for each in janes_data["watched"]:
           sum_counter += each["rating"]
    if len(janes_data["watched"]):

         return sum_counter/len(janes_data["watched"])
    else:
        return 0


def get_most_watched_genre(janes_data):
  genre_dict = {}
    
  for listi in janes_data["watched"]:
        for key, val in listi.items():           
            if key=="genre":               
                if val not in genre_dict:
                  genre_dict[val]=1         
                else:
                  genre_dict[val] +=1
    
  counter = 0
  genree = None
  for key, val in genre_dict.items():
    if val > counter:
      counter = val
      genree = key 
  return genree
    
def get_unique_watched(amandas_data):

    set_watched = set()
    set_friends = set()

    for each in amandas_data["watched"]:
        set_watched.add(each["title"])
  
    
    for each_friends in amandas_data["friends"]:
        inner_list_values = each_friends["watched"]  # this is dictionaries collected as a list as values of a key ("watched")
        for j in range(len(inner_list_values)):   
            set_friends.add(inner_list_values[j]["title"])

    unique_set  = set_watched - set_friends
    new_unique_list = list(unique_set)
    print(unique_set)
    return_list = []
    
    
    for j in range(len(new_unique_list)):
        unique_dictionaries = {}
        unique_dictionaries["title"] = new_unique_list[j]
        return_list.append(unique_dictionaries)

    return return_list

def get_friends_unique_watched(amandas_data):
    set_watched = set()
    set_friends = set()

    for each in amandas_data["watched"]:
        set_watched.add(each["title"])
 
    
    for each_friends in amandas_data["friends"]:
        inner_list_values = each_friends["watched"]  # this is dictionaries collected as a list as values of a key ("watched")
        for j in range(len(inner_list_values)):   
            set_friends.add(inner_list_values[j]["title"])

    unique_set  = set_friends - set_watched 
    new_unique_list = list(unique_set)
    
    return_list = []
    
    
    for j in range(len(new_unique_list)):
        unique_dictionaries = {}
        unique_dictionaries["title"] = new_unique_list[j]
        return_list.append(unique_dictionaries)

    return return_list


def get_available_recs(amandas_data):

    set_watched = set()
    set_friends = set()
    set_hosts = set()
    title_host_dict = {}
    movie_recommend = []

    for each in amandas_data["watched"]: # find out set of titles the user watched
        set_watched.add(each["title"])
  
    
    for each_friends in amandas_data["friends"]:
        inner_list_values = each_friends["watched"]  # this is dictionaries collected as a list as values of a key ("watched")
        for j in range(len(inner_list_values)):   
            set_friends.add(inner_list_values[j]["title"])
            title_host_dict[inner_list_values[j]["title"]] = inner_list_values[j]["host"]
            set_hosts.add(inner_list_values[j]["host"])

    list_subscriptions = amandas_data["subscriptions"]
   
    for each_set in set_friends:
        if  each_set not in set_watched and title_host_dict[each_set] in list_subscriptions:
            movie_recommend.append ({"title" : each_set, "host" : title_host_dict[each_set]})
   
    return movie_recommend




def get_new_rec_by_genre(sonyas_data):

    set_watched = set()
    set_friends = set()
    set_genre_sonyas = set()
    set_genre_friends = set()
    title_genre_dict = {}
    movie_recommend = []

    for each in sonyas_data["watched"]: # find out set of titles the user watched
        set_watched.add(each["title"])
        set_genre_sonyas.add(each["genre"])
   
    
    for each_friends in sonyas_data["friends"]:
        inner_list_values = each_friends["watched"]  # this is dictionaries collected as a list as values of a key ("watched")
        for j in range(len(inner_list_values)):   
            set_friends.add(inner_list_values[j]["title"])
            title_genre_dict[inner_list_values[j]["title"]] = inner_list_values[j]["genre"]
            set_genre_friends.add(inner_list_values[j]["genre"])

    
    for each_set in set_friends:
        if  each_set not in set_watched and title_genre_dict[each_set] in set_genre_sonyas:
            movie_recommend.append ({"title" : each_set, "genre" : title_genre_dict[each_set]})
    
   
    return movie_recommend

def get_rec_from_favorites(sonyas_data):
    set_watched = set()
    set_friends = set()
    set_favorites_sonyas = set()
    movie_recommend = []

    for each in sonyas_data["watched"]: # find out set of titles the user watched
        set_watched.add(each["title"])
    
    for fav in sonyas_data["favorites"]:   #find sets of favorites by the user
        set_favorites_sonyas.add(fav["title"])
   
    
    for each_friends in sonyas_data["friends"]:
        inner_list_values = each_friends["watched"]  # this is dictionaries collected as a list as values of a key ("watched")
        for j in range(len(inner_list_values)):   
            set_friends.add(inner_list_values[j]["title"])
            
            
    for each_set in set_favorites_sonyas:
        if each_set not in set_friends:
            movie_recommend.append({"title" : each_set})
    
   
    return movie_recommend
