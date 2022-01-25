import requests
from pprint import pprint as pp
import pymongo
import os
import json

client = pymongo.MongoClient()
db = client['StarWars']

# fetches data about the starships from teh API


def get_from_api():
    responses = []
    response = requests.get('https://swapi.dev/api/starships/').json()
    responses += response['results']
    while response['next'] is not None:  # ensures that all data is collected
        response = requests.get(response['next']).json()  # collects the link to the next page
        responses += response['results']  # adds information about the starships to the responses list
    return responses


#pp(get_from_api())


def collect_ships_url():
    starships = []
    for i in get_from_api():
        starships.append(requests.get(i['url']).json())
    return starships


# pp(collect_ships_url())


# Change pilot urls from the starship list to pilot name
def change_to_name():
    starships_updated =[]
    for i in collect_ships_url():
        pilot_names = []
        for j in i['pilots']:
            pilot_names.append(requests.get(j).json()['name'])
        # replace pilot the list with the list of character names
        i.update({'pilots': pilot_names})
        starships_updated.append(i)
    return starships_updated


# pp(change_to_name())


sw_starships = db['starships']
sw_characters = db['characters']

# Create directory in locally/repository manually
for i in change_to_name():
    with open(os.path.join('starships', i['name'] + '.json'), 'w') as f:
        f.write(json.dumps(i))

# Upload starship collection to mongoDB
def upload_collection():
    for i in os.listdir('starships'):
        with open(os.path.join('starships', i), 'r') as f:
            sw_starships.insert_one(json.load(f))


# Change pilot name in starship collection to character id
def pilot_id():
    for i in sw_starships.find():
        pilots = []
        for j in i['pilots']:
            unique_character_id = sw_characters.find_one({'name': j})['_id']
            match_id = {'_id': unique_character_id}
            pilots.append(match_id)
        sw_starships.update_one({'name': i['name']}, {'$set': {'pilots': pilots}})

upload_collection()
pp(pilot_id())