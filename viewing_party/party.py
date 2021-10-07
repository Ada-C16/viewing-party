def create_movie(title,genre,rating):
    if not title or not genre or not rating:
        return None
    mydict = {"title":title, "genre":genre,"rating":rating}          
    return mydict

def add_to_watched(user_data, movie):
    for key in user_data:       
        user_data[key].append(movie)
    return user_data 

def add_to_watchlist(user_data, movie):
    return add_to_watched(user_data, movie)
    # for key in user_data:   
    #     user_data[key].append(movie)
    # return user_data 
    

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:   
        if movie['title'] == title:   
            user_data['watched'].append(movie)   
            user_data['watchlist'].remove(movie)
    return user_data


def get_watched_avg_rating(janes_data):
    
    total = 0
    if janes_data["watched"] == []:
        return 0.0
    for item in janes_data["watched"]:
        total += item["rating"]
        
    average_rating = total/len(janes_data["watched"])
    return  average_rating 
 

def get_most_watched_genre(janes_data):
    frequencey_genre = {}
    for item in janes_data["watched"]:
        temp = item["genre"]
        if temp in frequencey_genre:
            frequencey_genre[temp] += 1
        else:
            frequencey_genre[temp] = 1
    if frequencey_genre != {}:
        max_value = max(frequencey_genre.values())
    for key,value in frequencey_genre.items():
        if  value == max_value :
            return key
        
def friends_unique_movie(user_data):
    friends_watched =user_data["friends"] 
    friends_unique_watched = []
    for item in friends_watched:
        for watched_movie in item["watched"]:
            if watched_movie not in friends_unique_watched:
                friends_unique_watched.append(watched_movie)
    return friends_unique_watched  


def get_unique_watched(user_data):
    user_unique_watched = []
    amandas_watched = user_data["watched"]
    for item in amandas_watched:
        if item not in friends_unique_movie(user_data):
            user_unique_watched.append(item)

    return user_unique_watched
    
def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    user_watched = user_data["watched"]
    for item in friends_unique_movie(user_data):
        if item not in user_watched:
            friends_unique_watched.append(item)

    return friends_unique_watched


def get_available_recs(user_data):
    
    # find the unique movies watched by friends if the host is found in the Amanda subscriptions. 
    friends_unique_movie_by_host = [item for item in friends_unique_movie(user_data) if item["host"] in user_data["subscriptions"]]
    
    # find the unique movie title watchd by friends with out the host       
    friends_unique_movie_title_without_host = [{k:v for k,v in item.items() if k != "host"} for item in friends_unique_movie_by_host ]
    
    # find the movie unseen by amanda and add to a list
    unseen_amanda_movie_title = [item["title"] for item in friends_unique_movie_title_without_host if item not in user_data["watched"]]
            
    # recommend movie title with the host for Amanda and put in a list
    rec_movie = [item for item in friends_unique_movie_by_host if item["title"] in unseen_amanda_movie_title]
    return rec_movie


def get_new_rec_by_genre(user_data):
    if user_data["watched"] == [] or friends_unique_movie(user_data) == []:
        return []
    rec_unique_movie_by_genre = [item for item in get_friends_unique_watched(user_data) 
                        if item["genre"] == get_most_watched_genre(user_data)]        
    return rec_unique_movie_by_genre  

def get_rec_from_favorites(user_data):
    rec_unique_movie_from_favorites = [item for item in user_data["favorites"] 
    if item not in friends_unique_movie(user_data)]
    return rec_unique_movie_from_favorites
    