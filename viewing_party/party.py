#WAVE_01
def create_movie(movie_title, genre, rating):
    new_movie = {}
    if movie_title and genre and rating != None:
        new_movie["title"]= movie_title   
        new_movie["genre"]= genre
        new_movie["rating"]= rating
        return(new_movie)
    else:
        return None

def add_to_watched(user_data, movie):
    if user_data["watched"] == []:
        movies_list = [movie]
        user_data["watched"] = movies_list

    else:
        movies_list = user_data["watched"]
        movies_list.append(movie)
        user_data["watched"]= movies_list

    updated_data = user_data
    return updated_data

def add_to_watchlist(user_data, movie):
    if user_data["watchlist"] == []:
        movies_list = [movie]
        user_data["watchlist"] = movies_list

    else:
        movies_list = user_data["watchlist"]
        movies_list.append(movie)
        user_data["watchlist"]= movies_list

    updated_data = user_data
    return updated_data

def watch_movie(user_data, title):
    watch_list = user_data['watchlist']
    viewed_list = user_data['watched']
    for movie in user_data["watchlist"]: 
        if movie["title"] == title:
            unwatched = movie["title"]
            if unwatched == title:
                watch_list.remove(movie)
                viewed_list.append(movie)
                updated_data = {"watchlist": watch_list, "watched": viewed_list}
                return updated_data
    else:
        return user_data

#WAVE_02

def get_watched_avg_rating (user_data):
    avg_rating = 0.0
    ratings = []
    viewed_list = user_data['watched']
    if user_data["watched"] != []:
        for movie in user_data["watched"]: 
            avg_rating += movie["rating"]
            ratings.append(movie["rating"])
        return avg_rating/len(ratings)
    else:
        return avg_rating

def get_most_watched_genre (user_data):
    user_genres = []
    watched_list = user_data["watched"]
    max_count = {}
    if user_data["watched"] != []:
        for movie in watched_list:
            genre_type = movie["genre"]
            user_genres.append(genre_type)
        genre_set = set(user_genres)
        for genre in genre_set:
            counter = 0
            temp_count = {}
            for user_genre in user_genres:
                if user_genre == genre:
                    counter += 1
                temp_count[genre] = counter
            max_count.update(temp_count)
        descending_value = (sorted(max_count, key=max_count.get, reverse=True))
        return descending_value[0]
    else:
        return None


#WAVE 03
def get_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    user_titles_list = []
    if user_data["watched"] != []: 
        for movie in user_watched_list:
            user_movie_title = movie["title"]
            user_titles_list.append(user_movie_title)

        friends_watched_list = user_data["friends"]
        friends_titles_list = []
        for friend in friends_watched_list:
            friend_list = friend["watched"]
            for movie in friend_list:
                watched_movie = movie["title"]
                friends_titles_list.append(watched_movie)

        user_titles_set = set(user_titles_list)
        friends_titles_set = set(friends_titles_list)
        unique_movie = list(user_titles_set - friends_titles_set)


#NEED TO CONINTUE TO WORK ON THIS!!!
        unique_movie_dict1 = {"title": unique_movie[0]}
        unique_movie_dict2 = {"title": unique_movie[1]}
        amandas_unique_movies = [unique_movie_dict1, unique_movie_dict2]
    else:
        amandas_unique_movies = []
    print(amandas_unique_movies)