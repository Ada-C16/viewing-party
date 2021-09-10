

def create_movie(movie_title, genre, rating):
    #if any  value == None return None
    if  genre== None  or  movie_title == None or  rating ==None:
        return None
    else:
        new_movie={
        "title": movie_title,
        "genre": genre,
        "rating": rating}
        return new_movie







def watch_movie(data_dict, title):
    pass


def add_to_watchlist(user_data, movie):
    pass



def add_to_watched(user_data, movie):
    pass
def get_watched_avg_rating(data_dic):
    pass

def get_most_watched_genre(data_dict):
    pass

def get_unique_watched(data_dic):
    pass

def get_friends_unique_watched(data_dict):
    pass

def get_available_recs(data_dict):
    pass

def get_new_rec_by_genre(data):
    pass

def get_rec_from_favorites(data):
    pass