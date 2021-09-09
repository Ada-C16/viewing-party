def create_movie(title, genre, rating):        
    if title and genre and rating:
        movie_dict ={}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    elif not title or genre or rating:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return(user_data)

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return(user_data)

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    if len(user_data["watched"]) > 0:
        sum_of_ratings = 0.0
        for movie in user_data["watched"]:
            sum_of_ratings += movie["rating"]
        avg_rating = sum_of_ratings / len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    most_watched_genre = None
    most_watched_genre_stat_dict = {}

    #iterate thru the list of watched movies and add value (num of watched) key (genre of movie) pair to most_watched_genre_stat_dict
    for movie_dict in user_data["watched"]:  
        if movie_dict["genre"] in  most_watched_genre_stat_dict:
            most_watched_genre_stat_dict[movie_dict["genre"]] += 1
        else:
            most_watched_genre_stat_dict[movie_dict["genre"]] = 1

    #determine the most watched genre
    if len(user_data["watched"]):
        most_watched_genre = max(most_watched_genre_stat_dict, key=most_watched_genre_stat_dict.get)

    return most_watched_genre


vange_data = {
    "watched": [
        {
        "title": "spongebob",
        "genre": "animation"
        },
        {
        "title": "little mermaid",
        "genre": "animation"
        },
        {
        "title": "ever after",
        "genre": "drama"
        },
        {
        "title": "jaws",
        "genre": "drama"
        },
        {
        "title": "the hours",
        "genre": "drama"
        }
    ]
}

get_most_watched_genre(vange_data)


#print(create_movie("green mile", "action", None))
#create_movie("green mile", "action", None)

#movie1 = create_movie("Title A", "Horror", 3.5)
#movie2 = create_movie("CATS", "Musical", 100)

#add_to_watched(vange_data, movie1)
#add_to_watched(vange_data, movie2)

#add_to_watchlist(vange_data, movie1)
#add_to_watchlist(vange_data, movie2)

#watch_movie(vange_data, "Title A")

#pytest tests/test_wave_02.py