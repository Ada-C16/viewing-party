def get_available_recs(user_data):
#   loop through dic and find movies that friends have watched and Amanda did not!!
#   The movies need to be supportted by the user's subscription - 
#   if 'host' not in user subscription do not recommend movie
#   return a dictionary eg:. {"title": "Title A", "host": "Service A"}








amandas_data = {
        "subscriptions": ["Service A", "Service B"],
        "watched": [{ "title": "Title A" }],
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

get_friends_unique_watched(amandas_data)