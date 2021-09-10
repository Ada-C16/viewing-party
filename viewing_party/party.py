def create_movie(title, genre, rating):
    '''
    Creates a new movie profile in dictionary format.
    Returns movie dict if information is complete.
    Returns None if any empty fields.
    '''
    # Create dictonary for movie profile
    movie = {}
    
    # Add movie profile to dict if all data available
    if title and genre and rating:
        movie['title'] = title
        movie['genre'] = genre
        movie['rating'] = rating
    
        # Return movie
        return movie
    else:
        # If data missing, return None
        return None

def add_to_watched(user_data, movie):
    '''
    Adds a movie that a user has viewed to the user's data profile.
    Returns updated user_data dictionary.
    '''
    # Append watched-movie data to user's 'watched' list
    user_data['watched'].append(movie)
    
    # Return user data
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Adds a new movie to user's watchlist.
    Returns updated user_data dictionary.
    '''
    # Append movie to user's 'watchlist'
    user_data['watchlist'].append(movie)

    # Return user data
    return user_data

def watch_movie(user_data, movie_title):
    '''
    Moves movie from user's watchlist to watched-list after viewing.
    Returns updated user data.
    '''
    # Filter user's watchlist, a list of dicitionaries, for movie title.
    # Cast filter object as a list to retrieve filter's return value
    movie_watched = list(filter(lambda movie: movie['title'] == movie_title, 
        user_data['watchlist']))

    # movie_watched is formated as follows:
        # [{'title': 'Title B', 'genre': 'Action', 'rating': 2.0}]
    
    # If movie not in 'watched' list, return user data
    if movie_watched:

        # Append watched movie to 'watched' list
        user_data['watched'].append(movie_watched[0])

        # Remove watched movie from 'watchlist' by filtering
            # for titles that do not match 'movie_title'
        # QUESTION: Is there a better way to do this?
        movies_unwatched = list(filter(lambda movie: movie['title'] != movie_title, 
            user_data['watchlist']))

        # Refer 'watchlist' to updated list of 'movies_unwatched'
        user_data['watchlist'] = movies_unwatched

        return user_data
    
    else:
        return user_data