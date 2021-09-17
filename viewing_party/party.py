#Wave_One part 1 
def create_movie (title, genre, rating):
    
    if title and genre and rating:
        movie_dict = {
        "title": title, 
        "genre": genre, 
        "rating": rating }
        return movie_dict 
    else:
        return None

#Wave_One part 2 
def add_to_watched(user_data, movie): 
    user_data["watched"].append(movie)
    return user_data


#Wave_One part 3 

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data


#Wave_One part 4 

def watch_movie (user_data, title): 

    for movie in user_data["watchlist"]:
        if movie["title"] == title:

            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


#Wave_TWO Part 1 

def get_watched_avg_rating(user_data):

    
    watched_list = user_data["watched"] 
    sum = 0 
    average_rating = 0.0
    if len(watched_list) == 0 :
        return average_rating
    for movie in watched_list:

        sum += movie["rating"]
    
    average_rating = sum/len(watched_list)
    return  average_rating
    
#Wave_TWO Part 2 

def get_most_watched_genre(user_data):
    most_populare_genre =[]
    if len (user_data["watched"]) == 0:
        return None 
    for movie_genre in user_data["watched"]:
        
            if "genre" in movie_genre:
                most_populare_genre.append(movie_genre["genre"])
            most_common = max(most_populare_genre, key = most_populare_genre.count)
            print (most_common)

    return most_common

            
#Completed using a dict but wasn't my first choice
# def get_most_watched_genre(user_data):
#     most_popular_genre = {}
#     if len(user_data["watched"]) == 0:
#         return None
#     for movie_genre in user_data["watched"]:
#         if movie_genre ["genre"] in most_popular_genre:
#             most_popular_genre[movie_genre["genre"]] += 1

#         else:
#             most_popular_genre[movie_genre["genre"]] = 1

#     max_value_genre=max(most_popular_genre, key= most_popular_genre.get)
#     return max_value_genre

#     # https://www.programiz.com/python-programming/methods/built-in/max
        

#Wave_Three Part 1 

def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    movie_list = []
    user_movie_set = set()
    friend_movie_set = set()
    for movie in user_watched: 
        user_movie_set.add(movie["title"])
        print(user_movie_set)
    for friend in friends_watched:
        for friends_watched_list in friend.values():
                # print(friends_watched_list)
            for movie_title in friends_watched_list:
                    # print(movie_title)
                    friend_movie_set.add(movie_title["title"])

    potential_friends_watched_set = (user_movie_set) - (friend_movie_set) 
    final_movie_list = []
    for potential in potential_friends_watched_set:
        final_movie_list.append({"title":potential})
    return final_movie_list



    
    

#Wave 3 Part 2 

def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = user_data["friends"]
    movie_list = []
    user_movie_set = set()
    friend_movie_set = set()
    for movie in user_watched: 
        user_movie_set.add(movie["title"])
        print(user_movie_set)
    for friend in friends_watched:
        for friends_watched_list in friend.values():
                # print(friends_watched_list)
            for movie_title in friends_watched_list:
                    # print(movie_title)
                    friend_movie_set.add(movie_title["title"])
    
    friends_unique_movies = []
    friends_unique_movie_set = (friend_movie_set) - (user_movie_set)

    for movie in friends_unique_movie_set:
        friends_unique_movies.append({"title":movie})
    return friends_unique_movies


            
        



#Wave 4 Part1




def get_available_recs(user_data):
    users_subscription = user_data["subscriptions"]
    friends_unique_movies = get_friends_unique_watched(user_data) 
    users_friends = user_data["friends"]
    users_friends_watched_movie = user_data["friends"]
    
    
    friends_movie_list = []
    for watched_movies in users_friends:
    
        
        for movies in watched_movies["watched"]:
            friends_movie_list.append(movies)

    movie_subscription = []
    for movies_watched in friends_movie_list:
        if movies_watched["host"] in users_subscription and movies_watched not in movie_subscription:
            movie_subscription.append(movies_watched)
    print(movie_subscription)
    

    user_title =[]
    for watched_movie in user_data["watched"]:
        user_title.append(watched_movie["title"])


    recommendations =[]

    if not user_data["watched"]:
        return movie_subscription
    for movie in movie_subscription:
        if movie["title"] not in user_title:
            recommendations.append(movie)
    return recommendations




#Wave 5 Part 1


def get_new_rec_by_genre(user_data):


    recommend_by_genre_list = []
    favorite_genre = get_most_watched_genre(user_data)
    friends= user_data["friends"]
    for movie_watched in friends:
        for movie_dictionary in movie_watched["watched"]:
            if ((movie_dictionary["title"] not in user_data["watched"]) \
            and (movie_dictionary["genre"] == favorite_genre) \
            and (movie_dictionary not in recommend_by_genre_list)):
                recommend_by_genre_list.append(movie_dictionary)

    return recommend_by_genre_list


#wave 5 Part 2
def get_rec_from_favorites(user_data):
    

    movie_recommend = []
    friends_watched_set = set()

    for friends_watched_lists in user_data["friends"]:
        for movies_friends_watched_list in friends_watched_lists.values():
            for user_dict in movies_friends_watched_list:
                friends_watched_set.add(user_dict["title"])
    
    for movie in user_data["favorites"]:
        if movie["title"] not in friends_watched_set:
            movie_recommend.append(movie)
    
    return movie_recommend








    #             for friends in users_friends: # {'watched': [{'title': 'Title A', 'host': 'Service A'}, {'title': 'Title C', 'host': 'Service C'}]}
    #                 for friends in (friends["watched"]): #{'title': 'Title A', 'host': 'Service A'} --> friends_movies 
    #                             if movie["host"] and  movie["title"]:
    #                                         friends_movie_list.append(movie["watched"])
    # #                                             print(m)
    # # print(friends_movie_list)
    # return friends_movie_list
    




    # users_movie = user_data["watched"]
    # users_friends = user_data["friends"]
    # users_subscription = user_data["subscriptions"]
    # recommended_movie_list = []
    # friends_movies_list = []
    # friends_movies_list1 = []
    # final_recommendations = []




