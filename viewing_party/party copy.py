def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        new_movie = {"title": movie_title, "genre": genre, "rating": rating}
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].pop()
    return user_data

def get_watched_avg_rating(user_data):
    ratings_list = []
    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])
    if len(ratings_list) == 0:
        return 0
    else:
        avg_rating = sum(ratings_list)/len(ratings_list)
        return avg_rating

def get_most_watched_genre(user_data):
    # Create Frequency Table
    frequency_table = {}
    for movie in user_data["watched"]:
        if movie["genre"] in frequency_table:
            print(movie["genre"])
            frequency_table[str(movie["genre"])] += 1
        else:
            print(movie["genre"])
            frequency_table[str(movie["genre"])] = 1
    # Find Max Value
    current_high = -1  # TODO: Might need to return None if watched is empty
    max_genre = None  # TODO: Might need to change this to a list for ties
    for genre, frequency in frequency_table.items():
        if frequency > current_high:
            current_high = frequency
            max_genre = genre
    return(max_genre)

 # ************* WAVE 3 ******************   
 #  TODO: Consider creating a helper function for finding unique movies
 #  TODO: Look into list comprehension to make smoother
def get_unique_watched(user_data):
    # Step 1: Get combined friend's watched list
    combined_friends = set()
    for friend in user_data["friends"]:
        for friend_watched in friend["watched"]:
            combined_friends.add(friend_watched["title"])
    # Step 2: Get User's watched list
    watched_set = set()
    for movie_watched in user_data["watched"]:
        watched_set.add(movie_watched["title"])
    # Step 3: Find user's difference with Friend's
    unique_watched_set = watched_set.difference(combined_friends)
    # Ste 4: Convert to Dictionary
    unique_watched_list = []
    for item in unique_watched_set:
        title_dict = {"title": item}
        unique_watched_list.append(title_dict)
    return unique_watched_list

# def get_friends_unique_watched(user_data):
#     # Step 1: Get combined friend's watched list
#     combined_friends = set()
#     for friend in user_data["friends"]:
#         for friend_watched in friend["watched"]:
#             combined_friends.add(friend_watched["title"])
#     # Step 2: Get User's watched list
#     watched_set = set()
#     for movie_watched in user_data["watched"]:
#         watched_set.add(movie_watched["title"])
#     # Step 3: Find Friend's difference with Users's
#     unique_watched_set = combined_friends.difference(watched_set)
#     # Ste 4: Convert to Dictionary
#     unique_watched_list = []
#     for item in unique_watched_set:
#         title_dict = {"title": item}
#         unique_watched_list.append(title_dict)
#     return unique_watched_list

def get_friends_unique_watched(user_data):
    # Step 1: Get combined friend's watched list
    combined_friends_title_only = set() # originally set()
    combined_friends_list = []
    for friend in user_data["friends"]:
        for friend_watched in friend["watched"]:
            combined_friends_title_only.add(friend_watched["title"])
            combined_friends_list.append(friend_watched)
    # Step 2: Get User's watched list
    user_watched_set = set()
    for movie_watched in user_data["watched"]:
        user_watched_set.add(movie_watched["title"])
    # Step 3: Find Friend's difference with Users's
    unique_watched_set = combined_friends_title_only.difference(user_watched_set)
    # Step 4: Convert set to list of dictionaries & Find Source
    unique_watched_list = []
    for item in unique_watched_set:
        # Find Host since this was lost in the set
        # Try block to cover cases when Host is not provided in friend's dataset
        try:
            for movie in combined_friends_list:
                if movie["title"] == item:
                    host = movie["host"]
                    movie_dict = {"title": item, "host": host}
                    unique_watched_list.append(movie_dict)
                    break  # Breaking to avoid adding multiple times if duplicates in combined_friends_list
        except KeyError:
            movie_dict = {"title": item}
            unique_watched_list.append(movie_dict)
    return unique_watched_list


# ************* WAVE 4 ******************   
def get_available_recs(user_data):
    friends_unwatched_list = get_friends_unique_watched(user_data)
    available_services = user_data["subscriptions"]
    final_recommendations = []
    for movie in friends_unwatched_list:
        if movie["host"] in available_services:
            final_recommendations.append(movie)
    return final_recommendations

# ************* WAVE 5 *******************
def get_new_rec_by_genre(user_data):
    friends_unwatched_list = get_friends_unique_watched(user_data)
    frequent_genre = get_most_watched_genre(user_data)
    final_recommendations = []
    if friends_unwatched_list and user_data["watched"]: 
        for movie in friends_unwatched_list:
            if movie["genre"] == frequent_genre:
                final_recommendations.append(movie)
    return final_recommendations