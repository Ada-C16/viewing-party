# 1. The first four tests are about a `create_movie()` function.

# In `party.py`, there should be a function named `create_movie`. This function should...

# - take three parameters: `title`, `genre`, `rating`
# - If those three attributes are truthy, then return a dictionary. This dictionary should...
#   - Have three key-value pairs, with specific keys
#   - The three keys should be `"title"`, `"genre"`, and `"rating"`
#   - The values of these key-value pairs should be appropriate values
# - If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`

def create_movie(title, genre, rating):
    """
    takes three parameters -title, genre and ratings. title and parameters
    expected to be strings, rating expected to be real number
    returns a dictionary movie with values as arguments passed in params
    if any param is missing function returns none
    """
    movie = None
    if title and genre and rating:
        movie = {}
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating

    return movie

