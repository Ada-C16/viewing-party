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

vange_data = {
    "watched": [],
    "watchlist": [{"title": "bring it on", "genre": "comedy", "rating": 10}]
}

#movie1 = create_movie("Title A", "Horror", 3.5)
#movie2 = create_movie("CATS", "Musical", 100)

#add_to_watched(vange_data, movie1)
#add_to_watched(vange_data, movie2)

#add_to_watchlist(vange_data, movie1)
#add_to_watched(vange_data, movie2)

#watch_movie(vange_data, "Title A")

#movie = create_movie("Title A", "Horror", 3.5)

#print(create_movie("green mile", "action", None))
#create_movie("green mile", "action", None)

#pytest tests/test_wave_01.py