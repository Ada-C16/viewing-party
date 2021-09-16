def create_movie (movie_title, genre, rating):
    #This returns a dictionary with keys:
    #  - title
    #  - genre
    #  - rating
    if (not movie_title == None) and (not genre == None) and (not rating == None):
        movie_dict = {"title":movie_title, "genre":genre, "rating": rating}
        return movie_dict
    else:
        return None
        
def add_to_watched (user_data, movie):
    #user_data watched list gets updated with the movie info.
    user_data["watched"].append(movie)  
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    #move the movie from  watch_list to  watched in user_data
    
    for record in user_data["watchlist"]:
        if record["title"] == title:
            user_data["watched"].append(record)
            break

    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            del user_data["watchlist"][i]
            break        
    return user_data

def get_watched_avg_rating(user_data):
    #define a variable to hold the sum of ratings
    the_sum = 0
    #define a variable to get the count of ratings
    the_count = 0
    #add the ratings to the sum, and increment the counter
    try:
        for record in user_data["watched"]:
            the_sum += record["rating"]
            the_count += 1

        #figure out the average by dividing the sum by the count
        return the_sum/the_count
    except ZeroDivisionError:
        return 0

def get_most_watched_genre(user_data):
    genre_dict = {}
    if user_data["watched"] != []:
        #first, create a dict of the genres and how often they appear in the watched list
        for record in user_data["watched"]:
            mygenre = record["genre"]
            genre_dict[mygenre] = genre_dict.get(mygenre,0)+1


        #second, find which genre in that newly created dictionary has the greatest value
        most_popular_genre = ""
        most_popular_genre_count = 0
        for k,v in genre_dict.items():
            if v > most_popular_genre_count:
                most_popular_genre = k
        
        return most_popular_genre
    else:
        return None


def get_unique_watched(user_data):
    #Set up a variable to hold the unique titles
    unique_dict = []

    #Compare each title in watched to the friends watched
    for record in user_data["watched"]:
        watched_title = record["title"]
        watched_title_found = False
        #If I dont find the title in the friends lists append to new dictionary
        for friend in user_data["friends"]:
            for friend_watched_record in friend["watched"]:
                friend_watched_title = friend_watched_record["title"]
                if watched_title == friend_watched_title:
                    watched_title_found = True
        
        #I did not find it in the friends, so append it
        if watched_title_found == False:
            unique_dict.append(record)
    
    return unique_dict
    
def get_friends_unique_watched(user_data):
    #Set up a variable to hold the unique titles
    unique_dict = []
    friends_dict = []

    #Loop through all the friends watched data and create a single list of dictionaries
    #with those records 
    for friend in user_data["friends"]:
        for friend_watched_record in friend["watched"]:
            if friend_watched_record not in friends_dict:
                friends_dict.append(friend_watched_record)


    #Loop through the friends_dict  to compare to user_data_watched
    for friend_watched_record in friends_dict:
        if friend_watched_record not in user_data["watched"]:
            unique_dict.append(friend_watched_record)
    
    return unique_dict 

def get_available_recs(user_data):
    #Set up a variable to hold friends suscriptions
    friends_suscrip_dict = []
    recommendation_dict = []
    
    #Loop through friends watched data and create a single list of dictionaries with those records. (title and host as keys with their values)
    for friend in user_data["friends"]:
        for friend_watched_record in friend["watched"]:
            if friend_watched_record not in friends_suscrip_dict:
                friends_suscrip_dict.append(friend_watched_record)
    
    #Loop through the friends dictionary to recomend user_data suscriptions. 
    for friend_watched_record in friends_suscrip_dict:
        #does the user have the service from the friend recommendation?
        if friend_watched_record["host"] in user_data["subscriptions"]:
            #has the user not seen the movie?
            already_seen = False
            for record in user_data["watched"]:
                #already_seen = False
                if record["title"] == friend_watched_record["title"]:
                    already_seen = True
            if not already_seen:
                recommendation_dict.append(friend_watched_record)
                #user_data["watched"].append(friend_watched_record)

    return recommendation_dict  

def get_new_rec_by_genre(user_data):

    #Set up variables to hold friends or reference to friends_dict for comaprison
    friends_dict = []
    recommendation_list = []

    #If the user hasnt watch any movies return an empty list.
    if len(user_data["watched"]) == 0:
        return []

    #Loop through friends watched data and create a single list of dicitionaries with those records 
    for friend in user_data["friends"]:
        for friend_watched_record in friend["watched"]:
            if friend_watched_record not in friends_dict:
                friends_dict.append(friend_watched_record)    
    
    #Loop through the friends dictionary to recomend user_data titles 
    for friend_watched_record in friends_dict:
        already_seen = False
        for user_data_watched_record in user_data["watched"]:
            if friend_watched_record["title"]in user_data_watched_record["title"]:
                already_seen = True

        if not already_seen:
            recommendation_list.append(friend_watched_record)
    
    return recommendation_list  

def get_rec_from_favorites(user_data):
    friends_dict= []
    recommendations = [] 

    if len(user_data["favorites"]) == 0:
        return []

    #Loop through favorites watched data 
    for friend in user_data["friends"]:
        for friend_watched_record in friend["watched"]:
            if friend_watched_record not in friends_dict:
                friends_dict.append(friend_watched_record) 

    #Loop through user_data_watched_favorites
    for favorite in user_data["favorites"]:
        if favorite not in friends_dict:
            recommendations.append(favorite)  

    return recommendations
        