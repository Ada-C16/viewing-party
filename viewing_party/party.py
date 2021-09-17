
#Wave 1

def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        movie_dict = {
        "title" : movie_title,
        "genre" : genre,
        "rating" : rating}
        return movie_dict
    else:
        return None



def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if movie["title"] == title:
            title = movie
    if title in user_data["watchlist"]:
        user_data["watchlist"].remove(title)
        user_data["watched"].append(title)
            
    return user_data

# Wave 2

def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    sum=0
    count=0
    if watched == []:
        print(watched)
        return 0.0
    else:
        for movie in watched:
            sum+=movie["rating"]
            count+=1
        avg=sum/count
        return avg


def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    if watched == []:
        return None
    else:
        genre_dict={}
        for movie in watched:
            if movie["genre"] not in genre_dict:
                genre_dict[movie["genre"]] = 1
            if movie["genre"] in genre_dict:
                genre_dict[movie["genre"]] += 1
        most_watched_genre = max(genre_dict, key=genre_dict.get)

        return most_watched_genre

#Wave 3

def get_unique_watched(user_data):
    user_watched=set()
    friends_watched=set()
    for movie in user_data["watched"]:
        user_watched.add(movie["title"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.add(movie["title"])
    unique_watched=user_watched.difference(friends_watched)

    result_list=[]

    for movie in unique_watched:
        for user_watched_movie in user_data["watched"]:
            if movie in user_watched_movie["title"]:
                result_list.append(user_watched_movie)

    return result_list


def get_friends_unique_watched(user_data):
    user_watched=set()
    friends_watched=set()
    for movie in user_data["watched"]:
        user_watched.add(movie["title"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.add(movie["title"])
    unique_watched=friends_watched.difference(user_watched)

    temp_list=[]
    result_list=[]

    for movie in unique_watched:
        for friend in user_data["friends"]:
            for friend_watched_movie in friend["watched"]:
                if movie in friend_watched_movie["title"]:
                    temp_list.append(friend_watched_movie)
    
    for i in range(0, len(temp_list)):
        if temp_list[i] not in temp_list[i+1:]:
            result_list.append(temp_list[i])
            
    return result_list


##Wave 4

def get_available_recs(user_data):
    unique_watched=get_friends_unique_watched(user_data)
    movie_rec=[]

    for unique_movie in unique_watched:
        if unique_movie["host"] in user_data["subscriptions"]:
            movie_rec.append(unique_movie)
    return movie_rec

##Wave 5

def get_new_rec_by_genre(user_data):
    genre=get_most_watched_genre(user_data)

    unique_watched=get_friends_unique_watched(user_data)
    rec_list=[]

    for unique_movie in unique_watched:
        if unique_movie["genre"] == genre:
            rec_list.append(unique_movie)    
    return rec_list


def get_rec_from_favorites(user_data):
    unique_watched=get_unique_watched(user_data)

    rec_list=[]

    for favorite in user_data["favorites"]:
        if favorite in unique_watched:
            rec_list.append(favorite)

    return rec_list