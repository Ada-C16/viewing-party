# *****WAVE 1******

def create_movie(title, genre, rating):
	dictionary_template = {}
	if title and genre and rating:
		dictionary_template["title"] = title
		dictionary_template["genre"] = genre
		dictionary_template["rating"] = rating
		return dictionary_template
	else:
		return None

def add_to_watched(user_data, movie):
	user_data["watched"].append(movie)
	return user_data

def add_to_watchlist(user_data, movie):
	user_data["watchlist"].append(movie)
	return user_data

def watch_movie(user_data, title):
	index = 0
	for movie in user_data["watchlist"]:
		if movie["title"] == title:
			watched_movie = user_data["watchlist"].pop(index)
			user_data["watched"].append(watched_movie)
		index += 1
	return user_data

# ******WAVE 2********
def get_watched_avg_rating(user_data):
	num_of_movies = 0
	sum_of_movie_ratings = 0.0
	average_rating = 0
	if not user_data["watched"]:
		return average_rating
	else:
		for movie in user_data["watched"]:
			sum_of_movie_ratings += movie["rating"]
			num_of_movies += 1
	average_rating = sum_of_movie_ratings/num_of_movies
	return average_rating

def get_most_watched_genre(user_data):
	genre_dict = {}
	genre_list = []
	previous_highest_times_watched = 1
	if not user_data["watched"]:
		return None
	else:
		for movie in user_data["watched"]:
			if genre_dict.get(movie["genre"]):
				genre_dict[movie["genre"]] += 1
			else:
				genre_dict[movie["genre"]] = 1
		for genre, times_watched in genre_dict.items():
			if times_watched > previous_highest_times_watched:
				genre_list.clear()
				genre_list.append(genre)
				previous_highest_times_watched = times_watched
			elif times_watched == previous_highest_times_watched:
				genre_list.append(genre)
				previous_highest_times_watched = times_watched
		if len(genre_list) == 1:
			return genre_list[0]
		elif len(genre_list) > 1: # to account for more than 1 most popular genre
			multiple_highest_genre = ""
			for genre in genre_list:
				if multiple_highest_genre == "":
					multiple_highest_genre += f"{genre} "
				else: 
					multiple_highest_genre += f"& {genre} "
			return multiple_highest_genre


# ******WAVE 3********

def get_unique_watched(user_data):
  
	# create of 2 lists of dictionaries, one representing movies the user has watched and the other movies that all friends have watched 

	user_watched_list =[]
	friends_watched_list = []

	if not user_data["watched"]:
		return user_data["watched"]
	else:
		for movie in user_data["watched"]:
			user_watched_list.append(movie)

	i = 0
	while i < len(user_data["friends"]):
		for movie in user_data["friends"][i]["watched"]:
			friends_watched_list.append(movie)
		i += 1
	
	# convert friend_watched_list and user_watched_list to a list of strings, then to a set of strings, and then find the difference between the 2 sets

	user_watched_set = set()
	friends_watched_set = set()

	i = 0
	while i < len(user_watched_list):
		user_watched_set.add(str(user_watched_list[i]))
		i += 1

	j = 0
	while j < len(friends_watched_list):
		friends_watched_set.add(str(friends_watched_list[j]))
		j += 1

	user_only_watched_set = user_watched_set - friends_watched_set


	# converting difference set back to a list of dictionaries

	import ast
	user_only_watched_list = list(user_only_watched_set)
	user_only_watched_list_final = []

	k = 0
	while k < len(user_only_watched_set):
		convert_to_dict = ast.literal_eval(user_only_watched_list[k])
		user_only_watched_list_final.append(convert_to_dict)
		k += 1

	return user_only_watched_list_final


def get_friends_unique_watched(user_data):

	# create of 2 lists of dictionaries, one representing movies the user has watched and the other movies that all friends have watched 

	user_watched_list =[]
	friends_watched_list = []

	for movie in user_data["watched"]:
		user_watched_list.append(movie)

	i = 0
	while i < len(user_data["friends"]):
		for movie in user_data["friends"][i]["watched"]:
			friends_watched_list.append(movie)
		i += 1
	
	# convert friend_watched_list and user_watched_list to a list of strings, then to a set of strings, and then find the difference between the 2 sets

	user_watched_set = set()
	friends_watched_set = set()
	
	i = 0
	while i < len(user_watched_list):
		user_watched_set.add(str(user_watched_list[i]))
		i += 1

	j = 0
	while j < len(friends_watched_list):
		friends_watched_set.add(str(friends_watched_list[j]))
		j += 1

	friends_only_watched_set = friends_watched_set - user_watched_set  

	# converting difference set back to a list of dictionaries

	import ast
	friends_only_watched_list = list(friends_only_watched_set)
	friends_only_watched_list_final = []

	k = 0
	while k < len(friends_only_watched_set):
		convert_to_dict = ast.literal_eval(friends_only_watched_list[k])
		friends_only_watched_list_final.append(convert_to_dict)
		k += 1
	
	return friends_only_watched_list_final

# *****WAVE 4******

def get_available_recs(user_data):
	
	user_subcription_list = user_data["subscriptions"]
	user_watched_list = user_data["watched"]
	recommend_for_user_list = []

	friends_watched_list = [] 
	friends_watched_list_no_duplicates = []
	friends_watched_set = set()

	for friends_dict in user_data["friends"]:
		for friends_watched_dict in friends_dict["watched"]:
			friends_watched_list.append(friends_watched_dict)

	# remove duplicates from friends_watched_list by converting 
	# dictionaries to strings then converting outer list to a set

	for watched_dict in friends_watched_list:
		friends_watched_set.add(str(watched_dict))

	# converting friends_watched_set to a list of dictionaries

	import ast

	for string in friends_watched_set:
		convert_to_dict = ast.literal_eval(string)
		friends_watched_list_no_duplicates.append(convert_to_dict)


	for film_host_dict in friends_watched_list_no_duplicates:
		if user_watched_list == []:
			if film_host_dict["host"] in user_subcription_list:
				recommend_for_user_list.append(film_host_dict)
		else:
			for film_dict in user_watched_list:				
				if film_dict["title"] != film_host_dict["title"]:
					if film_host_dict["host"] in user_subcription_list:
						recommend_for_user_list.append(film_host_dict)
						
	# remove any films user has already seen from recommended movies list
	for movie in user_watched_list:
		for movie_host in recommend_for_user_list:
			if movie["title"] == movie_host["title"]:
				recommend_for_user_list.remove(movie_host)

	return recommend_for_user_list

# *****WAVE 5******

def get_new_rec_by_genre(user_data):

	user_watched_list = user_data["watched"]
	friends_watched_list = [] 
	friends_watched_list_no_duplicates = []
	user_watched_genres_list = []
	recommend_to_user = []
	
	if user_watched_list == []:
		return []

	# add movie dictionaries for all friends into one list
	for movie in user_data["friends"]:
		for friends_watched_dict in movie["watched"]:
			friends_watched_list.append(friends_watched_dict)

    # remove duplicates from friends_watched_list
	for movie_dict in friends_watched_list:
		if movie_dict not in friends_watched_list_no_duplicates:
			friends_watched_list_no_duplicates.append(movie_dict)

	# put all user watched movie genres into a list
	for movie in user_watched_list:
		user_watched_genres_list.append(movie["genre"])

	# determine the genre that appears the most in user_genres_list 
	from collections import Counter
 
	occurence_count = Counter(user_watched_genres_list)
	most_frequent_user_genre = occurence_count.most_common(1)[0][0]

	for movie in friends_watched_list_no_duplicates:
		if movie not in user_watched_list:
			if movie["genre"]==most_frequent_user_genre:
				recommend_to_user.append(movie)

	return recommend_to_user


def get_rec_from_favorites(user_data):
	user_favorites_list = user_data["favorites"]
	friends_watched_list = []
	recommended_movies = []

	for watched_movie in user_data["friends"]:
		for movie in watched_movie["watched"]:
			friends_watched_list.append(movie)

	for movie in user_favorites_list:
		if movie not in friends_watched_list:
			if movie not in recommended_movies:
				recommended_movies.append(movie)

	return recommended_movies


