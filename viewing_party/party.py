
def create_movie(title,genre,rating):
    
    # if a title, genre, and rating are provided, create a dictionary of a movie and its relevant data
    if title and genre and rating:
        movie_dictionary = {}

        # assign keys to the corresponding data
        movie_dictionary["title"] = title
        movie_dictionary["genre"] = genre
        movie_dictionary["rating"] = rating
        
        # return the dictionary of the movie and its relevant data
        return movie_dictionary

def add_to_watched(user_data, movie):

    # add the dictionary of a movie and its relevant data to a user's list of watched movies
    user_data["watched"].append(movie)
    
    # return the user's data with an updated list of watched movies
    return user_data

def add_to_watchlist(user_data, movie):
    
    # add the dictionary of a movie and its relevant data to a user's watchlist
    user_data["watchlist"].append(movie)

    # return the user's data with an updated watchlist
    return user_data

def watch_movie(user_data, title):

    watchlist = user_data["watchlist"]
    watched_movies = user_data["watched"]

    # loop over the user's watchlist
    for movie in watchlist:
        movie_title = movie["title"]

        # if the title that was passed in as an argument is on the watchlist,
        #  remove the movie from the watchlist
        #  add the movie to the watched movies list
        if title == movie_title:
            watchlist.remove(movie)
            watched_movies.append(movie)

    
    # return the user's data with an updated watchlist and watched movies list
    return user_data

def get_watched_avg_rating(user_data):
    sum_of_ratings = 0.0
    number_of_movies_watched = 0.0
    
    # the average rating of an empty watched list is 0.0
    if not user_data["watched"]:
        return 0.0

    # loop over user's list of watched movies
    for movie in user_data["watched"]:
        # add a count to the total number of movies watched
        number_of_movies_watched += 1
        # add the movie's rating to the overall sum of movie ratings
        sum_of_ratings += movie["rating"]

    # get the average rating by diving sum of ratings by the number of movies
    average_rating = sum_of_ratings / number_of_movies_watched
    
    # return the average rating of the user's watched movies
    return average_rating

def get_most_watched_genre(user_data):

    watched_movies = user_data["watched"]
    genres_with_watch_counts = {}

    # if there are movies in the user's watched movies list,
    #  loop over the watched movies list
    if watched_movies:
        for movie in watched_movies:
            # if a genre is not already listed in the dictionary of genres and their watch counts,
            #  add the genre key and assign 0 to the watch count value
            if not movie["genre"] in genres_with_watch_counts.keys():
                genres_with_watch_counts[movie["genre"]] = 0
            # update the genre's watch count by one        
            genres_with_watch_counts[movie["genre"]] += 1

        # get the genre with the most watch counts
        highest_watch_count = max(genres_with_watch_counts.values())
        
        # loop over the dictionary of genres and their watch counts
        for genre in genres_with_watch_counts:
            # if a genre's watch count is the same as the highest watch count,
            #  return the genre with the highest watch counts
            if genres_with_watch_counts[genre] == highest_watch_count:
                return genre

def get_users_watched_movies(user_data):

    users_watched_movies = set()
    watched_movie_details = user_data["watched"]
    
    # loop over the user's list of watched movies
    for movie in watched_movie_details:
        movie_title = movie["title"]
        # add the movie title to a set of watched movies
        users_watched_movies.add(movie_title)

    # return set of user's watched movies 
    return users_watched_movies

def get_friends_watched_movies(user_data):

    movies_watched_all_friends = set()
    friends_list = user_data["friends"]

    # loop over a list of the user's friends
    for friend in friends_list:
        friends_movies = friend["watched"]
        # loop over each movie in the friend's watched movie list
        for movie in friends_movies:
            movie_title = movie["title"]
            # add the movie title to a set of all the movies watched by the user's friends
            movies_watched_all_friends.add(movie_title)

    # return set of the movies watched by user's friends
    return movies_watched_all_friends

def get_unique_watched(user_data):

    # get a list of the user's watched movies
    users_movies = get_users_watched_movies(user_data)
    # get a list of the user's friend's watched movies
    friends_movies = get_friends_watched_movies(user_data)

    # get the difference between the user's movies and the user's friend's movies
    unique_movies = users_movies.difference(friends_movies)
    
    users_unique_movies = []
    
    # loop over the list of movies only the user has watched
    for movie in unique_movies:
        movie_title = {"title":movie}
        # add the movie title to the list of unique movies
        users_unique_movies.append(movie_title)

    # return the list of movies only the user has watched
    return users_unique_movies

def get_friends_unique_watched(user_data):

    # get a list of the user's watched movies
    users_movies = get_users_watched_movies(user_data)
    # get a list of the user's friend's watched movies
    friends_movies = get_friends_watched_movies(user_data)

    # get the difference between the user's friend's movies and the user's movies
    unique_movies = friends_movies.difference(users_movies)
    
    friends_unique_movies = []

    # loop over the list of unique movies the user's friends have watched
    for movie in unique_movies:
        movie_title = {"title": movie}
        # add the movie title to the list of unique movies
        friends_unique_movies.append(movie_title)

    # return the list of movies the user's friends have watched but the user has not
    return friends_unique_movies

def get_friends_unique_watched_with_details(user_data):

    # get a list of movie only theuser's friends have watched
    users_unwatched_movies = get_friends_unique_watched(user_data)
    friends_list = user_data["friends"]

    unwatched_movies_and_details = set()

    # loop over the list of movies only the user's friends have watched
    for unwatched_movie in users_unwatched_movies:
        unwatched_movie_title = unwatched_movie["title"]
        # loop over the list of the user's friends
        for friend in friends_list:
            friends_watched_list = friend["watched"]
            # loop over the list of that friend's watched movies
            for movie in friends_watched_list:
                friends_movie_title = movie["title"]
                # if a movie from user's unwatched movie list is in a friend's watched movies list
                #  add the movie title and details (such as host or genre) to a list of user's unwatched movies
                if unwatched_movie_title == friends_movie_title:
                    movie_details = tuple(movie.values())
                    unwatched_movies_and_details.add(movie_details)
    
    # return the list of movies that only the user's friends have watched including relevant details
    return unwatched_movies_and_details

def get_available_recs(user_data):
    
    # get a list of movies and their streaming services only the user's friends have watched
    unwatched_movies_and_hosts = get_friends_unique_watched_with_details(user_data)
    
    available_recommended_movies = []

    # loop over the user's list of unwatched movies and their streaming services 
    for title, host in unwatched_movies_and_hosts:
        # if the unwatched movie is hosted on a service that the user is subscribed to,
        #  append the movie and service details to the list of recommended movies
        if host in user_data["subscriptions"]:
            available_recommended_movies.append({"title": title, "host": host})

    # return the list of movies that are hosted by a service the user is subscribed to that they have not watched but their friends have
    return available_recommended_movies

def get_new_rec_by_genre(user_data):
    
    # get a list of movies and their genres that the user's friends have watched but the user has not
    unwatched_movies_and_genres = get_friends_unique_watched_with_details(user_data)
    
    # get the genre the user watches the most
    favorite_genre = get_most_watched_genre(user_data)

    recommended_movies_in_favorite_genre = []

    # loop over user's friend's list of unwatched movies and their genres 
    for movie in unwatched_movies_and_genres:
        genre = movie[1]
        # if the unwatched movie is the same genre as the user's favorite genre,
        #  append the movie and genre to the recommended movies list
        if genre == favorite_genre:
            recommended_movies_in_favorite_genre.append({"title": movie[0], "genre": genre})

    # return the list of movies that only the user has watched that are in the user's favorite genre
    return recommended_movies_in_favorite_genre

def get_rec_from_favorites(user_data):

    # get a list of movies only the user has watched
    friends_unwatched_movies = get_unique_watched(user_data)
    recommended_movies_from_favorites = []
    users_favorites = user_data["favorites"]

    # loop over each movie that the user's friends have not watched
    for unwatched_movie in friends_unwatched_movies:
        movie = unwatched_movie["title"]
        # loop over each movie that is a favorite of the user's
        for favorite in users_favorites:
            # if a movie that friends have not watched is a favorite of the user,
            #  add a dict with movie title to the recommended movies list
            if movie == favorite["title"]:
                recommended_movies_from_favorites.append({"title": movie})
    
    # return the list of the user's favorite movies that have not been watched by their friends
    return recommended_movies_from_favorites
