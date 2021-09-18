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

def get_rec_from_favorites(user_data):
    #returns_empty_list_when_sonya_has_no_favorites
    #returns_expected_list_from_valid_input

    recommendations = []

    if user_data["favorites"] == []:
        return []

    for movie in user_data["watched"]:
        recommendations.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in recommendations:
                recommendations.remove(movie)
    
    print(recommendations)
    return recommendations

get_rec_from_favorites(sonyas_data)