

def create_movie(movie_title, genre, rating):
    if  genre== None  or  movie_title == None or  rating ==None:
        return None
    else:
        new_movie={
        "title": movie_title,
        "genre": genre,
        "rating": rating}
        return new_movie


print(create_movie('a', "drama", 4))    