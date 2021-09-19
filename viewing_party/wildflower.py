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

def get_available_recs(user_data):
    recomendations = []
    watches = [x['title'] for x in user_data['watched']]
    for friend in user_data['friends']:
        for watch in friend['watched']:
            if watch['host'] in user_data['subscriptions'] and watch['title'] not in watches and watch not in recomendations:
                recomendations.append(watch)

    return recomendations

print(get_available_recs(amandas_data))