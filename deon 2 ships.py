import requests
from pprint import pprint as pp
import pymongo

client = pymongo.MongoClient()
db = client['StarWars']

# fetches data about the starships from teh API
def get_from_api():
    responses = []
    response = requests.get('https://www.swapi.tech/api/starships/').json()
    responses += response['results']
    while response['next'] is not None:  # ensures that all data is collected
        response = requests.get(response['next']).json()  # collects the link to the next page
        responses += response['results']  # adds information about the starships to the responses list
    return responses


#pp(get_from_api())

def collect_ships_url():
    starships = []
    for i in get_from_api():
        starships.append(requests.get(i['url']).json()['result']['properties'])
    return starships

#pp(collect_ships_url())

# Change pilot urls from the starship list to pilot name
def change_to_name():
    starships_updated =[]
    for i in collect_ships_url():
        pilot_names = []
        for j in i['pilots']:
            pilot_names.append(requests.get(j).json()['result']['properties']['name'])
        # replace pilot the list with the list of character names
        i.update({'pilots': pilot_names})
        starships_updated.append(i)
    return starships_updated


#pp(change_to_name())


def insert_collection():
    #drop old collection, create new collection from starships and insert into mongodb
    db.drop_collection('starships')
    db.create_collection('starships')
    starships = change_to_name()
    for i in starships:
        db.starships.insert_one(i)

    return


insert_collection()
