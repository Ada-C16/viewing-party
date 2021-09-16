amandas_data = {
    "subscriptions": ["Service A", "Service B"],
    "watched": [],
    "friends": [
        {
            "watched": [
                {
                    "title": "Title A",
                    "host": "Service A"
                },
                {
                    "title": "Title C",
                    "host": "Service C"
                }
            ]
        },
        {
            "watched": [
                {
                    "title": "Title A",
                    "host": "Service A"
                },
                {
                    "title": "Title B",
                    "host": "Service B"
                },
                {
                    "title": "Title D",
                    "host": "Service D"
                }
            ]
        }
    ]
}

def get_available_recs(user_data):
    # Create an empty list of recommended movies
    friends_movies = []
    recommended_movies = []

    # Using a for loop, access each movie dictionary that each friend has seen
    # Use a print statement to confirm that we've accessed the right thing

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)
            # print(recommended_movies)

    # print("Friends' watched movies:")
    # print(friends_movies)

    for movie in friends_movies:
        if movie not in user_data["watched"] and movie not in recommended_movies:
            recommended_movies.append(movie)
            # print(movie)

    # Look inside of the subscriptions key of user_data
    # Loop through each movie to check that the movie's host matches an item in user_subscriptions

    print(recommended_movies)

    # print("Recommended movies that user has not already watched:")
    # print(recommended_movies)

get_available_recs(amandas_data)