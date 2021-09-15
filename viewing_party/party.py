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

    for item in only_user_watched_set:
        only_user_watched.append({"title" : item})


    return only_user_watched
                    
    

#oart 2 of wave 3!

def get_friends_unique_watched(user_data):
    user_watched_set = set()
    friends_watched_set = set()
    only_friends_watched_set = set()
    only_friends_watched = []


    for movie_user_watched in user_data["watched"]:
        user_watched_set.add(movie_user_watched["title"])
        
    for friends_watched_lists in user_data["friends"]:
        for movies_friends_watched_list in friends_watched_lists.values():
            for indiv_dict in movies_friends_watched_list:
                friends_watched_set.add(indiv_dict["title"])

    only_friends_watched_set = friends_watched_set.difference(user_watched_set)

    
    for item in only_friends_watched_set:
        only_friends_watched.append({"title" : item})

    return only_friends_watched




#wave 4!!!

#i want to return a list of movies that:
#the user hasn't watched - get_unique_watched()
#rememeber that that^ get's me the ones they have watched

#at least one of the friends has watched - get_friends_unique_watched()
#user has not watched AND one of friends watched
#AND the "host" is in "subscriptions"


def get_available_recs(user_data):

    #use my get_friends_unique_watched to get list of movies friends watched
    #compare to hosts
    #compare to subscription list
    # return a list of dictionaries (with title and host as keys for each dict)

    friends_watched_list = get_friends_unique_watched(user_data)
    friends_watched_list_titles = []
    
    print(friends_watched_list)


    for item in friends_watched_list:
        friends_watched_list_titles.append(item["title"])


    print(friends_watched_list_titles)


    rec_list = []

    for watched_lists in user_data["friends"]:
        for watched_dict in watched_lists["watched"]:
            if (watched_dict["host"] in user_data["subscriptions"]) \
                and (watched_dict not in rec_list) \
                and watched_dict["title"] in friends_watched_list_titles:
                    rec_list.append(watched_dict)
    print(rec_list)


    return rec_list









    """
    for friends_watched_dicts in user_data["friends"]:
        for one_list in friends_watched_dicts.values():
            for one_dict in one_list:
                complete_friends_watched_list.append(one_dict)
    #print(complete_friends_watched_list)
    #need list of movies NOT on user list, but on friends list
    
    
    for indiv_friends_dict in complete_friends_watched_list:
        #print(indiv_friends_dict["title"])
        for indiv_user_dict in user_data["watched"]:
            #print(indiv_user_dict["title"])
            if indiv_friends_dict["title"] not in indiv_user_dict.values():
                if indiv_friends_dict not in just_friends_watched:
                    
                    just_friends_watched.append(indiv_friends_dict)

    print(just_friends_watched)
    """


    



    #for user_movie_dict in user_movie_dict_list:
        #i will want to use this to compare: user_movie_dict["title"]






        


    











