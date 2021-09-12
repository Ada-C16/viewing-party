def create_movie(title, genre, rating):
    dictionary_template = {}
    if title and genre and rating:
        dictionary_template["title"] = title
        dictionary_template["genre"] = genre
        dictionary_template["rating"] = rating
        return dictionary_template
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    index = 0
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            watched_movie = user_data["watchlist"].pop(index)
            user_data["watched"].append(watched_movie)
        index += 1
    return user_data

def get_watched_avg_rating(user_data):
    num_of_movies = 0
    sum_of_movie_ratings = 0.0
    average_rating = 0
    if not user_data["watched"]:
        return average_rating
    else:
        for movie in user_data["watched"]:
            sum_of_movie_ratings += movie["rating"]
            num_of_movies += 1
    average_rating = sum_of_movie_ratings/num_of_movies
    return average_rating

def get_most_watched_genre():
    
user_data = {
    "watchlist": [{
  "title": "Title A",
  "genre": "Horror",
  "rating": 3.5
},
{
  "title": "Title B",
  "genre": "Horror",
  "rating": 3.5
}], 
  "watched": [{
  "title": "Title A",
  "genre": "Horror",
  "rating": 3.5
},
{
  "title": "Title B",
  "genre": "Horror",
  "rating": 3.5
}]
}