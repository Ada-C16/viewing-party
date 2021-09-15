#WAVE 1

#function 1
def create_movie(title, genre, rating):
    if (type(title) != str) or (type(genre) != str) or (type(rating) != float):
        return None
    
    movies_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    
    return movies_dict
#function 2

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

#add the movie to the "watched" list inside of user_data adn then return the user_data


#function 3
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

#function 4 
def watch_movie(user_data, title):
    for i in user_data:
        if i in user_data["watchlist"]:
            user_data["watchlist"].pop(i)
            user_data["watched"].append(i)
            return user_data
        else: 
            return user_data


   

#WAVE 2 
#AVERAGE =  sum of a set of numbers divided by the number of figures in the data set
#HERE WE ARE ITERATING OVER THE DATA SET 
# def get_watched_avg_rating(user_data):
#     sum = 0
#     user_data_dict = {watched: [{movies}]}
#         for movies in user_data_dict:
#             sum += movie / 
#  for i in title:
#         if i in user_data["watchlist"]:
#             user_data.pop("value")
#             user_data["watched"][value] = user_data("value") 
#             return user_data
#     else: 
#         return user_data