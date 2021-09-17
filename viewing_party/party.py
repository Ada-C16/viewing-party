import operator 
def create_movie(movie_title,genre,rating):
    movie_dict={
        "title": " ",
        "genre": " ",
        "rating":0.0
    }
    if movie_title and genre and rating:
        # for movie in movie_title:
        #     movie_dict["title"]=movie
        # for kind in genre:
        #     movie_dict["genre"]=kind
        # for score in rating:
        #     movie_dict["rating"]=score
        movie_dict["title"]=movie_title
        movie_dict["genre"]=genre
        movie_dict["rating"]=rating
        return movie_dict
    else:
        return None



def add_to_watched(user_data, movie):
    user_data["watched"] += [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"] += [movie]
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


def get_watched_avg_rating(user_data):
    ratings=[]
    average_rating=0
    if len(user_data["watched"]) == 0:
            average_rating=0.0
            return average_rating
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
        
    average_rating = sum(ratings) / len(ratings)
    return average_rating



def get_most_watched_genre(user_data):
    most_frequent_genre_list=[]
    most_common=None
    for movie in user_data["watched"]:
        
        most_frequent_genre_list.append(movie["genre"])
        most_common=max(most_frequent_genre_list, key=most_frequent_genre_list.count)
        print(most_frequent_genre_list)
    return most_common
    # frequency={}
    # max_count=0


    # for movie in user_data["watched"]:
    #     genre= movie["genre"]
    #     if( genre in frequency):
    #         frequency[genre]+= 1
    #     else:
    #         frequency[genre] = 1
    
    
    # popular_genre=[]
    # for genre,count in frequency.items():
    #     if count == 1:
    #         popular_genre.append(count)
    #         max_count=max(frequency.values())
    # print(max_count)
    # return max_count


    # print(popular_genre)
    # return popular_genre
    
    # for movie in user_data["watched"]["genre"]:
    #     frequency_list.append(user_data["watched"])
    #     # print(frequency_list)
    #     most_common=max(frequency_list, key = frequency_list.count)
    # print(frequency_list)
    # print(most_common)
    # return most_common
    



    # def get_unique_items(items):
#     unique_items = []

#     # N times
#     for item in user_data["watched"]:
#         count = 0
#         # N times
#         for other_item in items:
#             if item == other_item:
#                 count += 1
        
#         if count == 1:
#             unique_items.append(item)
    
#     return unique_items

#wave3
def get_unique_watched(user_data):
    unique_list=[]
    for movie in user_data["friends"]:
        unique_list.append(movie)
    print(unique_list)
    #     if user_data["watched"] not in movie:
    #         unique_list.append(movie)
    # print(unique_list)
    # return unique_list
