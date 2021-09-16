def create_movie(title, genre,rating):
    new_movie={}
    if isinstance(title,str):
        new_movie["title"]=title
    else:
        new_movie["title"]=None
    if isinstance(genre,str):
        new_movie["genre"]=genre
    else:
        new_movie["genre"]=None
    if type(rating)==int or float:
        new_movie["rating"]=rating
    else:
        new_movie["rating"]= None
    
    for key in new_movie: 
        if new_movie[key]==None:
            return None
    return new_movie
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************    
    
def add_to_watched(user_data, movie):
    watched=user_data["watched"]
    
    for key in user_data:
        if key=="watched":
            watched.append(movie)
            user_data["watched"]=watched
                
    return user_data
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************

def add_to_watchlist(user_data, movie):
    watchlist=user_data["watchlist"]
    
    for key in user_data:
        if key=="watchlist":
            watchlist.append(movie)
            user_data["watchlist"]=watchlist
                
    return user_data
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************       

def watch_movie(user_data,title):
    watched=user_data["watched"]
    watchlist=user_data["watchlist"]
    updated_watched=watched 
    updated_watchlist=watchlist
    movie_watch={}

    for item in watchlist:
        movie_watch.update(item)

    for movie_watch in user_data["watchlist"]:
        if movie_watch["title"]==title:
            updated_watchlist.remove(movie_watch)
            updated_watched.append(movie_watch)
            user_data["watchlist"]=updated_watchlist
            
            user_data["watched"]=updated_watched 
        else:
            updated_watchlist=watchlist
        
    return user_data

# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************

def get_watched_avg_rating(user_data):
    movie_ratings=[]
    movies_watched=user_data["watched"]
    avg_rating=0.0
    if len(movies_watched)!=0:
        for movie in movies_watched:
            movie_ratings.append(movie["rating"])

        avg_rating= sum(movie_ratings)/len(movie_ratings)
    
    return avg_rating 
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************

def get_most_watched_genre(user_data):
    genre_watched=[]
    movies_watched=user_data["watched"]
    most_watched={}
    
    if len(movies_watched)!=0:
        for movie in movies_watched:
            genre_watched.append(movie["genre"])
        for genre in genre_watched:
            if genre not in most_watched:
                most_watched[genre]=1
            else:
                most_watched[genre]+=1
        max_key = max(most_watched, key=most_watched.get)
        return max_key
    return None

# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************   

def get_unique_watched(user_data):
    user_watched=[]
    friends_watched=[]
    user_unique_watched=[]
    if len(user_data["watched"])>0:
        for movie in user_data["watched"]:
            if movie not in user_unique_watched:
                user_watched.append(movie)

        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie not in friends_watched:
                    friends_watched.append(movie)

        for movie in user_watched:
            if movie not in friends_watched:
                user_unique_watched.append(movie)

        return user_unique_watched
    return []
        
    # *_____________________________ with many lists =S  __________________________________* 
    # list_of_friends=user_data["friends"]
    # list_of_movies=[]
    # list_of_titles=[]
    # friends=[]
    # amigo_movie=[]
    # friends_watched=[]
    # for friend in list_of_friends:
    #     list_of_movies.append(friend["watched"])
    # for friend in list_of_friends:
    #     friends.append(friend)
    # for friend in list_of_movies:
    #     list_of_titles.append(friend)
    # for objeto in list_of_titles:
    #     for amigo in objeto:
    #         amigo_movie.append(amigo)
    # for amigo in amigo_movie:
    #     friends_watched.append(amigo["title"])
    # # print(friends) 
    # # print(list_of_friends) 
    # # print(list_of_titles)
    # # print(amigo_movie)
    # # print(friends_watched)
    # user_movies=user_data["watched"]
    # user_watched=[]
    # for movie in user_movies:
    #     user_watched.append(movie["title"])
 
    # user_set=set(user_watched)
    # friends_set=set(friends_watched)
    # result_set=user_set.difference(friends_set)
    
    # final_list=[]
    # for title in result_set:
    #     final_dict={}
    #     final_dict["title"]=title
    #     # print(title)
    #     # print(final_dict)
    #     final_list.append(final_dict)
    
    # return final_list

# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
    
def get_friends_unique_watched(user_data):
    list_of_friends=user_data["friends"]
    list_of_movies=[]
    list_of_titles=[]
    friends=[]
    amigo_movie=[]
    friends_watched=[]
    for friend in list_of_friends:
        list_of_movies.append(friend["watched"])
    for friend in list_of_friends:
        friends.append(friend)
    for friend in list_of_movies:
        list_of_titles.append(friend)
    for objeto in list_of_titles:
        for amigo in objeto:
            amigo_movie.append(amigo)
    for amigo in amigo_movie:
        friends_watched.append(amigo["title"])

    user_movies=user_data["watched"]
    user_watched=[]
    for movie in user_movies:
        user_watched.append(movie["title"])
 
    user_set=set(user_watched)
    friends_set=set(friends_watched)
    result_set=friends_set.difference(user_set)
    
    final_list=[]
    for title in result_set:
        final_dict={}
        final_dict["title"]=title
  
        final_list.append(final_dict)
    
    return final_list        

# *_____________________________ with many lists =S  __________________________________* 
    #     user_watched=[]
    # friends_watched=[]
    # friends_unique_watched=[]
    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if movie not in friends_watched:
    #             friends_watched.append(movie)
            
    # if len(user_data["watched"])>0:
    #     for movie in user_data["watched"]:
    #         if movie not in user_watched:
    #             user_watched.append(movie)
        
    #     # for friend in user_data["friends"]:
    #     #     for movie in friend["watched"]:
    #     #         if movie not in friends_watched:
    #     #             friends_watched.append(movie)  
    #     for movie in friends_watched:
    #         if movie not in user_watched:
    #             friends_unique_watched.append(movie)
    #             return friends_unique_watched
    # return friends_watched
    
        
        # return friends_unique_watched

# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************


def get_available_recs(user_data):
  
    recommendations=[]
    friends_unique_watched=[]
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
  
    # why it's not considering the user watched????
    for movie in friends_unique_watched:
        # if movie not in user_data["watched"]:
       
        if {"title":movie["title"]} not in user_data["watched"]:
            if movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
    return recommendations
   


# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************

def get_new_rec_by_genre(user_data):
    genre_recommended=[]
    friends_watched=[]
    user_watched_genre=[]
    
    for movie in user_data["watched"]:
        user_watched_genre.append(movie["genre"])
    if len(user_watched_genre)>0:   
        user_fav_genre=max(set(user_watched_genre), key = user_watched_genre.count)


        for friend in user_data["friends"]:
            for friends_movies_watched in friend["watched"]:
                if friends_movies_watched not in friends_watched:
                    friends_watched.append(friends_movies_watched)
        print(friends_watched)
        
        if user_data["watched"] not in friends_watched:
            for movie in friends_watched:
                if movie["genre"]== user_fav_genre:
                    genre_recommended.append(movie)
        return genre_recommended
    return []
   

# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************
# *************************************----------------------------*******************************************

def get_rec_from_favorites(user_data):
    fav_recommended=[]
    friends_watched=[]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
    for user_fav in user_data["favorites"]:
        if user_fav not in friends_watched:
            fav_recommended.append(user_fav)
    return fav_recommended
    

  
            


            

        
        


        






        
       


    






  


