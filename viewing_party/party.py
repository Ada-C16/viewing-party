def create_movie(title,genre,rating):
    mydict = {"title":title, "genre":genre,"rating":rating}
    for value in mydict.values():
        if value == None:
            return None            
    return mydict

def add_to_watched(user_data, movie):
    for key in user_data:       
        user_data[key].append(movie)
    return user_data 

def add_to_watchlist(user_data, movie):
    for key in user_data:   
        user_data[key].append(movie)
    return user_data 
    

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:   
        if movie['title'] == title:   
            user_data['watched'].append(movie)   
            user_data['watchlist'].remove(movie)
    return user_data


def get_watched_avg_rating(janes_data):
    count = 0
    total = 0
    if janes_data["watched"] == []:
        return 0
    for item in janes_data["watched"]:
        total += item["rating"]
        count += 1
    average_rating = total/count
    return  average_rating 
 

def get_most_watched_genre(janes_data):
    frequencey_genre = {}
    max_value = 0
    
    for item in janes_data["watched"]:
        temp = item["genre"]
        if temp in frequencey_genre:
            frequencey_genre[temp] +=1
        else:
            frequencey_genre[temp]= 1

    for value in frequencey_genre.values():
        if max_value < value:
            max_value = value
        
    for key in frequencey_genre:
        if frequencey_genre[key] == max_value:
            return key


def get_unique_watched(amandas_data):
    unique_watched = []
    amandas_watched = amandas_data["watched"]
    amandas_friends_watched =amandas_data["friends"][0]["watched"]
    for item in amandas_data["friends"][1]["watched"]:
        if item not in amandas_friends_watched:
            amandas_friends_watched.append(item)
    
    for item in amandas_watched:
        if item not in amandas_friends_watched:
            unique_watched.append(item)

    return unique_watched
    
def get_friends_unique_watched(amandas_data):
    unique_watched = []
    amandas_watched = amandas_data["watched"]
    amandas_friends_watched =amandas_data["friends"][0]["watched"]
    for item in amandas_data["friends"][1]["watched"]:
        if item not in amandas_friends_watched:
            amandas_friends_watched.append(item)
    
    for item in amandas_friends_watched:
        if item not in amandas_watched:
            unique_watched.append(item)

    return unique_watched


def get_available_recs(amandas_data):
    friends_unique_movie = []
    temp_unssen_movie_amanda= []
    rec_movie = []
    unseen_amanda_movie_title = []
    
    # find the unique movies watched by friends if the host is found in the Amanda subscriptions. 
    for item in amandas_data["friends"][0]["watched"]:
        if item["host"] in amandas_data["subscriptions"] :
            friends_unique_movie.append(item)
            
    for item in amandas_data["friends"][1]["watched"]:
        if item["host"] in amandas_data["subscriptions"]  and item not in friends_unique_movie:
            friends_unique_movie.append(item)
    # find the unique movie title watchd by friends with out the host       
    new_friends_unique_movie_title = [{k:v for k,v in item.items() if k != "host"} for item in friends_unique_movie ]
    
    
    # find the movie title unseen by Amanda as a dictionary and append to a list
    for item in new_friends_unique_movie_title:      
        if item not in amandas_data["watched"]:
            temp_unssen_movie_amanda.append(item)
    
    # find the movie unseen by amanda and add to a list
    for item in temp_unssen_movie_amanda:
        for value in item.values():
            unseen_amanda_movie_title.append(value)
    
    # recommend movie title with the host for Amanda and put in a list
    for item in friends_unique_movie:
        if item["title"] in unseen_amanda_movie_title:
            rec_movie.append(item)

    return rec_movie

def get_new_rec_by_genre(sonyas_data):
    rec_unique_movie = []
    if sonyas_data["watched"] == [] or (sonyas_data["friends"][0]["watched"]
                and sonyas_data["friends"][1]["watched"]) == []:
        return []

    for item in sonyas_data["friends"][0]["watched"]:
        if item not in sonyas_data["watched"] :
            rec_unique_movie.append(item)
            
    for item in sonyas_data["friends"][1]["watched"]:
        if item not in sonyas_data["watched"] and item not in rec_unique_movie:
            rec_unique_movie.append(item)
            
    return rec_unique_movie    
def get_rec_from_favorites(sonyas_data):
    rec_unique_movie_from_favorites = []
    for item in sonyas_data["favorites"]:
        Friend_movie_first =sonyas_data["friends"][0]["watched"]
        Friend_movie_second = sonyas_data["friends"][1]["watched"]
        if item not in Friend_movie_first and item not in Friend_movie_second :
            rec_unique_movie_from_favorites.append(item)
    return rec_unique_movie_from_favorites