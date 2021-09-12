def get_rec_from_favorites(user_data):
# return value from favorites that friends have not watched yet
# loop through friends movies title and store in list
# store favorites in a list
#create a variable  to store the result
    favorites = [item['title'] for item in user_data["favorites"]]
    friends_watched = []
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_watched.append(value['title']) 
    not_watched = set(favorites).difference(set(friends_watched))
    result= [{"title":item} for item in not_watched]
    return result


    


sonyas_data = {
        "watched": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            },
            {
                "title": "Title C"
            }
        ],
        "favorites": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            }
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title B"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title C"
                    },
                    {
                        "title": "Title D"
                    }
                ]
            }
        ]
    }
print(get_rec_from_favorites(sonyas_data))