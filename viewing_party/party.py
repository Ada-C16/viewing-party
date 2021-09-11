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
    
    # Confirm the movie watched was in 'watchlist'
    if movie_watched:
        # Append watched movie to 'watched' list
        user_data['watched'].append(movie_watched[0])

        # Remove watched movie from 'watchlist' by filtering
            # for titles that do not match 'movie_title'
        # QUESTION: Is there a better way to do this?
        movies_unwatched = list(filter(lambda movie: movie['title'] != movie_title, 
            user_data['watchlist']))

        # Refer user_data['watchlist'] to updated list of 'movies_unwatched'
        user_data['watchlist'] = movies_unwatched

        return user_data
    # If the movie watched was not in 'watchlist'
    else:
        return user_data

def get_watched_avg_rating(user_data):
    '''
    Calculates and returns average rating of films from 
    'watched' list. 
    '''
    # Confirm there is data in 'watched' list
    if user_data['watched']:
        # Instantiate variable to hold running total
        total = 0
        # Loop through each movie's 'rating' in 'watched' list
        for i in range(len(user_data['watched'])):
            total += user_data['watched'][i]['rating']
        
        # Calculate average dividing total by length
        average = total / (i + 1)
        
        return average
    # If there is no data in 'watched' list
    else:
        return 0

def get_most_watched_genre(user_data):
    '''
    Tabulates the genre most prevalent in a user's 'watch'
    list.
    '''
    # Confirm there is data in 'watched' list
    if user_data['watched']:
        # Create a dictionary to hold counts of genres
        genre_counts = {}

        # Loop through 'watched' list counting occurances of each genre
        for i in range(len(user_data['watched'])):
            # Place long key name in shorter variable
            current_key = user_data['watched'][i]['genre']
            # Use .get() method to count occurances, default value of 1
            genre_counts[current_key] = genre_counts.get(current_key, 0) + 1

        # Find key with highest numerical value
        most_watched_genre = max(genre_counts, key=genre_counts.get)
        

        return most_watched_genre
    # If there is no data in 'watched' list
    else:
        return None


def get_unique_watched(user_data):
    '''
    Determines which movies user has watched that listed friends
    have not watched. Returns a list of dictionaries, that
    represents a list of unique movies.
    '''
    # Instantiate empty list to store returning movie data
    unique_movies = []

    # Create a set to store movie titles user has watched, add titles
    users_movies = set()
    for watched_movie in user_data['watched']:
        users_movies.add(watched_movie['title'])
    
    # Create a set to store movie titles friends have watched
    friends_movies = set()
    for friend_data in user_data['friends']:
        for watched_movie in friend_data['watched']:
            friends_movies.add(watched_movie['title'])
    
    # Compare watched titles of user and friends, isolating titles unique
    # to user in a set
    movies_unique_to_user = users_movies.difference(friends_movies)

    # For unique movie titles, create a dict and append to return list
    for title in movies_unique_to_user:
        format_dict = {}
        format_dict['title'] = title
        unique_movies.append(format_dict)

    # Return list of movie dictionaries
    return unique_movies

def get_friends_unique_watched(user_data):
    '''
    Determines which movies friends have watched that user
    has not watched. Returns a list of dictionaries, that
    represents a list of unique movies.
    '''
    # Instantiate empty list to store returning movie data 
    unique_movies = []

    # Create a set to store movie titles user has watched, add titles
    # QUESTION: Is is better practice to account for empty lists
    #  so this for loop doesn't run?
    users_movies = set()
    for watched_movie in user_data['watched']:
        users_movies.add(watched_movie['title'])

    # Create a set to store movie titles friends have watched, add titles
    friends_movies = set()
    for friend_data in user_data['friends']:
        for watched_movie in friend_data['watched']:
            friends_movies.add(watched_movie['title'])
    
    # Compare watched titles of user and friends, isolating titles unique
    # to friends in a set
    movies_unique_to_friends = friends_movies.difference(users_movies)

    # For unique movie titles, create a dict and append to return list
    for movie in movies_unique_to_friends:
        format_dict = {}
        format_dict['title'] = movie
        unique_movies.append(format_dict)

    # Return list of movie dictionaries
    return unique_movies

def get_available_recs(user_data):
    '''
    Returns a list of recommended movies.
    '''
    # Instantiate a return list to store recommendation dictionaries
    recommendations = []

    # Create variable to refer to list of user's subscriptions
    user_subscriptions = user_data['subscriptions']
    
    # Utilize get_friends_unique_watched function to filter for 
    #  friend-recommended movie titles
    friend_recommendations = get_friends_unique_watched(user_data)

    # Isolate friend-recommended movie titles from friend_recommendations
    #  in a list
    friends_movies = []
    for movie in friend_recommendations:
        friends_movies.append(movie['title'])
    
    # Identify friend-recommended movies that user has subscription to view
    for friend_data in user_data['friends']:
        for watched_movie_data in friend_data['watched']:
            # Check that user is subscribed to 'host' and
            #  'title' is recommended
            if watched_movie_data['host'] in user_subscriptions \
                and watched_movie_data['title'] in friends_movies:
                # If movie is not already recommended, addpend to recs
                if watched_movie_data not in recommendations:
                    recommendations.append(watched_movie_data)

    # Return recommendations
    return recommendations

def get_new_rec_by_genre(user_data):
    '''
    Returns a unique list of recommended movies based on movies
    friends have watched that match user's most frequently watched
    genre. 
    '''
    # Instantiate an empty list to hold recommendations
    recommendations = []

    # Determine user's most frequent genre using get_most_watched_genre()
    most_freq_genre = get_most_watched_genre(user_data)

    # Isolate friend-recommended movie titles with get_friends_unique_watched()
    friends_movie_recs = get_friends_unique_watched(user_data)

    # Determine which friend-recommmended titles match user's most freq genre
    # Loop through each friend profile
    for friend_data in user_data['friends']:
        # Loop through watched movies in individual friend profile
        for movie_data in friend_data['watched']:
            # Find titles that are in friend-recommended list
            #  and match user's most frequent genre
            for movie in friends_movie_recs:
                if movie_data['title'] in movie['title'] \
                    and movie_data['genre'] == most_freq_genre:
                    # If movie not already in rec list, add to list
                    if movie_data not in recommendations:
                        recommendations.append(movie_data)
                
    # Return recommendation list
    return recommendations