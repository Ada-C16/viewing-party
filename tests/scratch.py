def watch_movie(user_data, title):
    # if title in watchlist 
    # Movie the movie object to watched
    lenght_to_iterate = len(user_data["watchlist"])
    watchlist = [elem for elem in user_data["watchlist"]]
    for item in range(lenght_to_iterate):
        if title in watchlist[item]['title']:
            del user_data['watchlist'][item]
            user_data["watched"] +=[watchlist[item]]
    return user_data        


    
    

title = "Title A"
movie_to_watch = {
        "title": "Title A",
        "genre": "Fantasy",
        "rating": 4.8
    }
user_data =  {
        "watchlist": [
            {
                "title": "Title B",
                "genre": "Action",
                "rating": 2.0
            },
            movie_to_watch
        ],
        "watched": [
            {
                "title": "Title C",
                "genre": "Intrigue",
                "rating": 3.9
            }
        ]
    }
    

(watch_movie(user_data, title))