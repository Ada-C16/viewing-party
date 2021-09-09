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
    '''
    # Append watched-movie data to user_data's watched list
    user_data['watched'].append(movie)
    
    # Return user profile
    return user_data