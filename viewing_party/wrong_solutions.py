    # def get_rec_from_favorites(user_data):
    # ---------------------------------------
    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if movie in user_favorites and movie not in friend["watched"]

    # for favorite in user_favorites:
    #     for friend in user_data["friends"]:
    #         for movie in friend["watched"]:
    #             if favorite == movie:
    #                 continue
    #             else:
    #                 recommendations.append(favorite)

        # for favorite in user_favorites:
    #     for friend in user_data["friends"]:
    #         print(friend["watched"])
    #         if favorite not in friend["watched"] and favorite not in recommendations:
    #             recommendations.append(favorite)

    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if {"title": movie["title"]}

    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         for fav in user_data["favorites"]:
    #             if fav not in friend["watched"] and fav not in recommendations:
    #                 recommendations.append({"title": fav["title"]})

    # ========= GET_AVAILABLE_RECS()
        # Figure out which movies each friend has watched
    # user_data["friends"] gives you a list of friend-dictionaries
    # Looping through 1 gives you a friend

    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if (movie not in user_data["watched"]) and (movie not in recommended_movies):
    #             recommended_movies.append({"title": movie["title"], "host": movie["host"]})

    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if ({"title": movie["title"]} not in user_data["watched"]) and ({"title": movie["title"], "host": movie["host"]} not in recommended_movies):
    #             recommended_movies.append({"title": movie["title"], "host": movie["host"]})

       # for each_movie in recommended_movies:
    #     if each_movie["host"] not in user_subscriptions:
    #         recommended_movies.remove(each_movie)

    # If that condition matches, remove it from the list
    # Finally, return the list

    # friends_movies = []
        # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         friends_movies.append(movie)

    # for movie in friends_movies:
    #     if movie not in user_data["watched"] and movie not in recommended_movies:
    #         if movie["host"] in user_subscriptions:
    #             recommended_movies.append(movie)