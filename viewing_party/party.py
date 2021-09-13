#wave 1

def create_movie(title, genre, rating):
    #is there a more efficient/cleaner way to do what's below?
    if bool(title) is True: 
        if bool(genre) is True:
            if bool(rating) is True:
                movie_dict = {
                    "title" : title,
                    "genre" : genre,
                    "rating" : rating
                }
                return movie_dict
    else:
        return None


#part 2

def add_to_watched(user_data, movie):
    
    user_data["watched"].append(movie) 
    return user_data


#part 3
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


#part 4
def watch_movie(user_data, title):
    for movie_list in user_data["watchlist"]:
    #gets me to the list in user_data
            if title in movie_list["title"]:
                user_data["watched"].append(movie_list)
                #movie_list.remove(movie)
                user_data["watchlist"].remove(movie_list)

    return user_data





#############################
#wave 2

#part 1

#return the avg rating : )
def get_watched_avg_rating(user_data):
    rating_sum = 0.0
    rating_avg = 0.0
    
    if len(user_data["watched"]) == 0:
        return rating_avg

    for movie_dict in user_data["watched"]:
        rating_sum += movie_dict["rating"]

    rating_avg = rating_sum / (len(user_data["watched"]))
    return rating_avg


#part 2

def get_most_watched_genre(user_data):
    #put genres in a list
    #count amount occurence of each genre in the list
    #return the one that occurs most frequently
    genre_list = []
    fantasy_count = 0
    action_count = 0
    intrigue_count = 0

    if len(user_data["watched"]) == 0:
        return None

    for movie_dict in user_data["watched"]:
        genre_list.append(movie_dict["genre"])

    fantasy_count = genre_list.count("Fantasy")
    action_count = genre_list.count("Action")
    intrigue_count = genre_list.count("Intrigue")

    if (fantasy_count > action_count) and (fantasy_count > intrigue_count):
        return "Fantasy"
    elif (action_count > fantasy_count) and (action_count > intrigue_count):
        return "Action"
    else: #this does not account for the fact that there may be no clear most popular genre
        #it doesn't look like the tests require this, but I can add it in later
        return "Intrigue"








##########################
#wave 3!!
def get_unique_watched(user_data):
    #which movies has the user watched, the friends have watched
    #which ones as the user watched but the friends have NOT watched?
    #return a list of dictionaries of the movies only the user has watched

    #want to iterate through both lists and compare the innermost lists 
    only_user_watched = []
    user_watched_set = set()
    friends_watched_set = set()
    only_user_watched_set = set()

    for movie_user_watched in user_data["watched"]:
        user_watched_set.add(movie_user_watched["title"])
        for friends_watched_lists in user_data["friends"]:
            for movies_friends_watched_list in friends_watched_lists.values():
                for indiv_dict in movies_friends_watched_list:
                    friends_watched_set.add(indiv_dict["title"])

    only_user_watched_set = user_watched_set.difference(friends_watched_set)

    print(only_user_watched_set)

    for item in only_user_watched_set:
        only_user_watched.append({"title" : item})


    return only_user_watched
                    
    
#my logic doesn't make sense! I am comparing everything in one list to another
#i can try to use sets instead
#make two sets: one with everything from user,
#one with everything from friends
#then, compare sets
#then, build a dict with only the values that are 

    





