# Wave 1
def create_movie(title, genre, rating):
    movie_dict = {}
        if title: 
            movie_dict['title'] = title
        elif genre:
            movie_dict['genre'] = genre
        elif rating:
            movie_dict['rating'] = rating
        else:
            return None
    return movie_dict

def add_to_watched(user_data, movie):
    # return user_data
    pass

def add_to_watchlist(user_data, movie):
    # return user_data
    pass

def watch_movie(user_data, title):
    # return user_data
    pass