def test_get_available_recs_returns_appropriate_recommendations_for_valid_input():
    # Arrange
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

    # Act
    recommendations = get_available_recs(amandas_data)


def get_available_recs(user_data):

    recommendations = []

    user_subscriptions = user_data["subscriptions"]
    
    friend_recommendations = get_friends_unique_watched(user_data)

    friends_movies = []
    for movie in friend_recommendations:
        friends_movies.append(movie["title"])
    for friend_data in user_data["friends"]:
        for watched_movie_data in friend_data["watched"]:
            if watched_movie_data["host"] in user_subscriptions \
                and watched_movie_data["title"] in friends_movies:
                if watched_movie_data not in recommendations:
                    recommendations.append(watched_movie_data)
    return recommendations
    
    
