from viewing_party.party import get_new_rec_by_genre
# Arrange
# Arrange
sonyas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A",
                        "genre": "Intrigue"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title B",
                        "genre": "Fantasy"
                    },
                    {
                        "title": "Title C",
                        "genre": "Intrigue"
                    }
                ]
            }
        ]
    }

    # Act
recommendations = get_new_rec_by_genre(sonyas_data)

 
# Act
# recommendations = get_rec_from_favorites(sonyas_data)
# recommendations = get_available_recs(amandas_data)
print(recommendations)
 # Act
# amandas_unique_movies = get_unique_watched(amandas_data)
# print(amandas_unique_movies)
# friends_unique_movies = get_friends_unique_watched(amandas_data)
# print(friends_unique_movies)

# recommendations = get_available_recs(amandas_data)

# print(recommendations)