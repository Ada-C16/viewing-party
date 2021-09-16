def create_movie(movie_title, genre, rating):
    """
    input: 3 strings which provide details about a movie
    output: a dictionary which stores details about the movie
    """

    # Create a dictionary where the keys are
    # title, genre, and rating of
    # the new dictionary - grab these values
    # from the arguments passed as parameters

    # if every argument that is passed is truthy
    # then run the code below, otherwise:
    # run different code

    if movie_title and genre and rating:
        movie = {}
        movie["title"] = movie_title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    """
    input: A dictionary of user_data and a particular movie
    output: Returns the dictionary of user_data, with the movie added to the "watched" key
    """
    # Given a movie dictionary, 
    # Return statement for this function should equal the dictionary of user_data
    # user_data is a parameter of data type dictionary
    # movie is also a parameter of data type dictionary

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    input: A dictionary of user_data and a particular movie
    output: Returns the user_data dictionary with the movie added to the "watchlist" key of user_data
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    input: A dictionary of user_data and a movie title
    output: The user_data dictionary with the movie dictionary removed from "watchlist"
    and added to the "watched" list
    """
    # Check whether movie_title was in watchlist
    # user_data[watchlist]
    # If it was, remove it from the watchlist
    # Append it to the add_to_watched list

    # Watchlist is a list with multiple dictionaries
    # Loop through each element in the watchlist list
    # Check whether the title key matches the movie_title given above

    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            watched_movie = movie
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(watched_movie)

    return user_data

def get_watched_avg_rating(user_data):
    """
    input: A dictionary of user_data
    output: The average rating of each movie in the user's watched list
    """

    # Access the watched key in user_data
    # That points to a list
    # Inside this list are dictionary elements
    # We need to loop through each dictionary element
    # in watched, access the rating keys
    # store them in a variable for calculation
    # calculate the average of each

    sum = 0
    avg_list = []

    # store each rating int into a new list

    if not user_data["watched"]:
        return 0.0

    else:
        for movie in user_data["watched"]:
            avg_list.append(movie["rating"])

        for num in avg_list:
            sum += num
        
        avg = sum / len(avg_list)
        
        return avg

def get_most_watched_genre(user_data):
    """
    input: A dictionary of user_data
    output: A string which represents which genre a user has watched the most
    """
    
    # Given a dictionary user_data
    # Access the watched key, which is a list
    # Loop through that watched list
    # Append each genre to a genre dictionary
    # Each genre will equal a key
    # Set the count of each genre equal to the value of its corresponding key
    # Return the name of the most-watched genre

    genre_list = []
    genre_dict = {}

    if not user_data["watched"]:
        return None

    else:
        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])

        # Search through genre_list
        # Count how many times each genre is listed
        # Add it to a dictionary

        # Add each genre as a new key in the dictionary with an initalized value of 0
        for item in genre_list:
            genre_dict[item] = 0
        # Go through each genre in genre_list, and count how many times it's in there
        # Add this count to the corresponding dictionary key in genre_dict
        for item in genre_list:
            if item in genre_dict.keys():
                genre_dict[item] += 1

        # Store the most_watched genre in a variable
        # Use the max function to pass two arguments
        # The first argument is the iterable (dictionary) to check
        # The second argument accesses the key in genre_dict that has the highest value
        # The .get function reference accesses the value of a particular key
        most_watched = max(genre_dict, key=genre_dict.get)

        print(most_watched)
        return most_watched

def get_unique_watched(user_data):
    """
    input: A dictionary of user_data
    output: A list of movies as dictionaries, which were watched by the user but not their friends
    """

    user_set = set()
    friend_set = set()

    # Collect all of the movie titles watched by original user_data
    # Access with user_data[0] <= loop through this list of dictionaries
    # Grab the values at each title key and put into a set_1
    for movie in user_data["watched"]:
        user_set.add(movie["title"])

    # this is a list - loop through this list of dictionaries
    # in the dictionaries, access ["watched"], which is another list of dictionaries
    # loop through the watched list to grab the ["title"] key and put that into a second set
    for friend_data in user_data["friends"]:
        for movie in friend_data["watched"]:
            friend_set.add(movie["title"])
    
    # Compare both sets, getting the difference between set_1 and set_2
    # Turn the resulting set into a list
    # Return that list back to the function
    unique_watched = list(user_set - friend_set)

    new_list = []
    # Create a dictionary for each title
    # append that dictionary to unique watched with the key "title"
    for movie in unique_watched:
        new_list.append({"title": movie})

    unique_watched = new_list
    

    return unique_watched

def get_friends_unique_watched(user_data):
    """
    input: A dictionary of user_data
    output: A list of movies that a user's friends have watched, but the user has not
    """

    user_set = set()
    friend_set = set()

    # Collect all of the movie titles watched by original user_data
    # Access with user_data[0] <= loop through this list of dictionaries
    # Grab the values at each title key and put into a set_1
    for movie in user_data["watched"]:
        user_set.add(movie["title"])
    # Then access the second element in user_data[1]
    for friend_data in user_data["friends"]:
        for movie in friend_data["watched"]:
            friend_set.add(movie["title"])
    # this is a list - loop through this list of dictionaries
    # in the dictionaries, access ["watched"], which is another list of dictionaries
    # loop through the watched list to grab the ["title"] key and put that into a second set
    friends_unique_watched = list(friend_set - user_set)

    new_list = []
    # Create a dictionary for each title
    # append that dictionary to unique watched with the key "title"
    for movie in friends_unique_watched:
        new_list.append({"title": movie})

    friends_unique_watched = new_list
    # Compare both sets, getting the difference between set_1 and set_2
    # Turn the resulting set into a list
    # Return that list back to the function

    return friends_unique_watched

def get_available_recs(user_data):
    """
    input: A dictionary of user_data
    output: A list of movies that the user has not watched and that match the subscription platforms
    the user uses
    """
    
    recommended_movies = []
    user_subscriptions = user_data["subscriptions"]

    for friend in user_data["friends"]: # For each friend
        for movie in friend["watched"]: # Loop through each movie the friend has watched
            if ({"title": movie["title"]} not in user_data["watched"]): # Check that the title has not been seen by the user
                if movie["host"] in user_subscriptions: # Check that the user is subscribed to the host
                    if movie not in recommended_movies: # Make sure you're not adding duplicate movies
                        recommended_movies.append(movie)
    
    return recommended_movies

def get_new_rec_by_genre(user_data):
    """
    input: A dictionary of user_data
    output: A list of movies that match the user's most-watched genre
    """

    most_watched_genre = get_most_watched_genre(user_data)

    recommended_by_genre = []
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in (user_data["watched"] and recommended_by_genre):
                if movie["genre"] == most_watched_genre:
                    recommended_by_genre.append(movie)
    
    return recommended_by_genre

def get_rec_from_favorites(user_data):
    """
    input: A dictionary of user_data
    output: A list of movies that the user recommends to their friends who have not already watched those movies
    """

    # Create a list of recommendations to return at the end of the function
    # Look through the list of user_data["favorites"] to collect a list of favorites
    # Store that information into a separate list called user_favorites
    # If a movie is not in friend["watched"] and not in recommendations, then add it to the list
    # Look inside of each friends "watched" list to create a friends_watched list
    # If a particular friend has /not/ watched the movie from favorites
    # Add it to the list

    recommendations = []
    user_favorites = user_data["favorites"]

    friends_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for favorite in user_favorites:
        if favorite not in friends_watched:
            recommendations.append(favorite)

    return recommendations