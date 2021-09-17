def create_movie(title, genre, rating):
    if not title:
        return None
    if not genre:
        return None
    if not rating:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating        
    }
    return movie
    
def add_to_watched(user_data, movie):
    if not movie:
        return None
    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if not movie:
        return None
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    print("a")
    for i in range(len(user_data["watchlist"])):
        if title in user_data["watchlist"][i]["title"]:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])

    return user_data

def get_watched_avg_rating(user_data):
    total = 0
    for each in range(len(user_data["watched"])):
        total += user_data["watched"][each]["rating"]
    if user_data["watched"] == []:
        return 0
    avg = (total / (len(user_data["watched"])))
    print (avg)
    return avg

def get_most_watched_genre(user_data):
    counter_dict = {}
    for movie_dict in user_data["watched"]:
        if user_data["watched"] == []:
            break
        if counter_dict.get(movie_dict["genre"]):
            counter_dict[movie_dict["genre"]] += 1
        else:
            counter_dict[movie_dict["genre"]] = 1
    if not counter_dict:
        return None
    try:
        most_watched_value = max(counter_dict, key=lambda x : x[1])
    except ValueError:
        return None
    most_watched_genre = []
    return most_watched_value

def get_unique_watched(user_data):
    seen = []
    show_friends = []
    for i in range(len(user_data["friends"])):
        seen += user_data["friends"][i]["watched"]
    for i in range(len(user_data["watched"])):
        if user_data["watched"][i] not in seen:
            show_friends.append(user_data["watched"][i])

    if len(show_friends) == 0:
        return []
    return show_friends

def get_friends_unique_watched(user_data):
    seen = []
    friends_show = []
    for i in range(len(user_data["friends"])):
        seen += user_data["friends"][i]["watched"]
    no_repeats  = []
    for i in friends_show:
        if i not in no_repeats:
            no_repeats.append(i)
    friends_show = no_repeats
    for each in seen:
        if each not in user_data["watched"]:
            friends_show.append(each)

    if len(friends_show) == 0:
        return []
    no_repeats = []
    for i in friends_show:
        if i not in no_repeats:
            no_repeats.append(i)
    friends_show = no_repeats
    return friends_show

def get_available_recs(user_data):
    seen = []
    rec_list = []
    for i in range(len(user_data["friends"])):
        seen += user_data["friends"][i]["watched"]
    user_seen = []
    for element in user_data["watched"]:
        user_seen.append(element["title"])
    for each in seen:
        if each["title"] not in user_seen:
            rec_list.append(each)
    print (rec_list)

    subbed_only= []
    for dict in rec_list:
        if dict["host"] in user_data["subscriptions"]:
            subbed_only.append(dict)
    rec_list = subbed_only
    if len(rec_list) == 0:
        return []
    no_repeats = []
    for i in rec_list:
        if i not in no_repeats:
            no_repeats.append(i)
    rec_list = no_repeats
    return rec_list

def get_new_rec_by_genre(user_data):
    genre_counter = {}
    rec_list = []
    if user_data["watched"] == []:
        return []
    for list in user_data["watched"]:
        if list["genre"] not in genre_counter.keys():
            genre_counter[list["genre"]] = 1
        else:
            genre_counter[list["genre"]] += 1
    most_genred = max(genre_counter, key = lambda x : x[1])
    for list in user_data["friends"]:
        for sublist in list["watched"]:
            if sublist["genre"] in most_genred:
                
                rec_list.append(sublist)
        no_repeats = []
        for i in rec_list:
            if i not in no_repeats:
                no_repeats.append(i)
        rec_list = no_repeats

    return rec_list
    
def get_rec_from_favorites(user_data):
    seen = []
    show_friends = []
    for i in range(len(user_data["friends"])):
        seen += user_data["friends"][i]["watched"]
    for i in range(len(user_data["watched"])):
        if user_data["watched"][i] not in seen:
            show_friends.append(user_data["watched"][i])

    if len(show_friends) == 0:
        return []
    fav_rec = []
    for movie in user_data["favorites"]:
        if movie in show_friends:
            fav_rec.append(movie)
        
    return fav_rec
