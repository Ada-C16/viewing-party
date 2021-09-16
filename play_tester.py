from viewing_party.party import *

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
    '''
    Returns a list of recommended movies based on movies friends
    have watched and a platform that the user subscribes to. 
    '''
    # Instantiate a return list to store recommendation dictionaries
    recommendations = []

    # Create variable to refer to list of user's subscriptions
    user_subscriptions = user_data['subscriptions']
    
    # Identify friend-recommended movies that user has subscription to view
    for friend_data in user_data['friends']:
        for watched_movie_data in friend_data['watched']:
            # Check that user is subscribed to 'host' and
            #  'title' is recommended
            if watched_movie_data['host'] in user_subscriptions \
                and watched_movie_data['title'] not in user_data['watched']:

                # If movie is not already recommended, addpend to recs
                if watched_movie_data not in recommendations:
                    recommendations.append(watched_movie_data)

    # Return recommendations
    return recommendations


# Act
recommendations = get_available_recs(amandas_data)
print(recommendations)