def create_movie(movie_title,genere,rating):
    mylist = ["movie_title","genere","rating"]
    mydict = {}
    for key in mylist:
        mydict[key] = eval(key)
        print(mydict)
        if eval(key) == 0:
            return None
        
        
        
    return mydict
  
def add_to_watched(user_data, movie):
    for key in user_data:
        
        user_data[key].append(movie)
    return user_data     
