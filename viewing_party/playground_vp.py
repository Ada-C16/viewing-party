def get_rec_from_favorites(user_data):
    friend_watched_titles = create_a_list_of_only_friend_watched_titles(user_data)
    user_favorite_title = create_a_list_of_only_user_data_favorite_titles(user_data)
    user_watched_title = user_data["watched"]
    recommendations = []
    if len(user_favorite_title) == 0:
        return recommendations
    else:  
        for movie in user_watched_title:
            if movie["title"] in user_favorite_title:
                if movie["title"] not in friend_watched_titles:
                    recommendations.append(movie)
    return recommendations

def create_a_list_of_only_friend_watched_titles(user_data):
    friend_watched = merge_friend_watch_lists(user_data)
    friend_watched_list = []
    for movie in friend_watched:
        friend_watched_list.append(movie["title"])
    return friend_watched_list

def create_a_list_of_only_user_data_favorite_titles(user_data):
    user_watched = user_data["favorites"]
    user_watched_list = []
    for movie in user_watched:
        user_watched_list.append(movie["title"])
    return user_watched_list

def merge_friend_watch_lists(user_data):
    friend_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_watched:
                friend_watched.append(movie)
    return friend_watched

def test_get_rec_from_favorites_returns_expected_list_from_valid_input():
    # Arrange
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

    # Act
    recommendations = get_rec_from_favorites(sonyas_data)

    # Assert
    assert len(recommendations) == 1
    assert {"title": "Title A"} in recommendations
test_get_rec_from_favorites_returns_expected_list_from_valid_input()