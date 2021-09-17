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
    for movie in user_data["watchlist"]:
        if title == movie["title"]:     #Rebeca review this when you have time 
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data
        
#WAVE 2 
#AVERAGE =  sum of a set of numbers divided by the number of figures in the data set
#HERE WE ARE ITERATING OVER THE DATA SET 
#fuction 1 
def get_watched_avg_rating(user_data):
    total_watched = len(user_data["watched"])
    sum = 0
    if total_watched:
        for movie in user_data["watched"]:
            sum += movie["rating"]  #this calculates the sum of the ratings
            average_rating = sum / total_watched
        return average_rating
    else:
        return 0.0
    
#function 2 - Function that finds the mode of the genre category.
def get_most_watched_genre(user_data):
    genre_list = []
    freq = {}
    if user_data["watched"]:
        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])
        for elem in genre_list:
           freq[elem] = genre_list.count(elem)
        most_watched_genre = max(freq, key=freq.get)
        return most_watched_genre
    else:
        return None



