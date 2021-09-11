

def create_movie(movie_title, genre, rating):
    #initialize variables
    movie_dict = {}

    #check if movie title, genre and rating are correct
    #var types and returns movie_dict or None
    if type(movie_title) == str and type(genre) == str and type(rating) == float:
        movie_dict['title'] = movie_title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
    else:
        return None
    return movie_dict


movie = {
    "title": "Title A",
    "genre": "Horror",
    "rating": 3.5
}
user_data = {
    "watched": []
}

#add movie to user_data dictionary and returns user data
def add_to_watched(user_data, movie):
    #add user data to watched dictionary
    #user_data["watched"]
    return user_data['watched']

print(add_to_watched(user_data, movie))