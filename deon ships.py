import requests
import json
from pprint import pprint as pp
import os
import pymongo

client = pymongo.MongoClient()
db = client['StarWars']

#Retrieve starship api data page by pages json
pg1 = requests.get('https://swapi.dev/api/starships/').json()
pg2 = requests.get(pg1['next']).json()
pg3 = requests.get(pg2['next']).json()
pg4 = requests.get(pg3['next']).json()

# pprint(pg1)

#collect starship info into a list
def collect_results():
    starship_id = []
    for i in pg1['results']:
        starship_id.append(i)

    for j in pg2['results']:
        starship_id.append(j)

    for k in pg3['results']:
        starship_id.append(k)

    for l in pg4['results']:
        starship_id.append(l)
    return starship_id


#pp(collect_results())


# Collect all starship urls into a list
def collect_ship_urls():
    starship_urls =[]
    for i in collect_results():
        starship_urls.append(i['url'])
    return starship_urls


#pp(collect_ship_urls())


# Change pilot urls from the starship list to pilot name
def change_to_name():
    starships_updated =[]
    for i in collect_results():
        pilot_names = []
        for j in i['pilots']:
            pilot_names.append(requests.get(j).json()['name'])
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


