def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating: 
        movie = {
            'title': movie_title,
            'genre': genre,
            'rating': rating
        }
        return movie
    return None

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    movie_to_watch = next(filter(lambda  movie: movie.get('title') == movie_title, user_data['watchlist']), None)
    if movie_to_watch: 
        user_data['watched'].append(movie_to_watch)
        user_data['watchlist'].remove(movie_to_watch)
    return user_data
