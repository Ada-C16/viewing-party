def get_rec_from_favorites(user_data):
    favorites = [item['title'] for item in user_data["favorites"]]
    friends_list = []
    for item in user_data["friends"]:
        for  value  in item['watched']:
            friends_list.append(value['title']) 
    # create_friends_list(user_data,friends_list)   
    
    print(friends_list)    
    not_watched = set(favorites).difference(set(friends_list))
    result= [{"title":item} for item in not_watched]
    return result