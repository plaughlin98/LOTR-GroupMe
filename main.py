import math
import json
import random
from api_config import LotrAPI
from prettytable import PrettyTable

auth_string = 'Bearer ' + config.ACCESS_TOKEN

headers = {
    'Accept': 'application.json',
    'Authorization': auth_string,
}

lotr_url = "https://the-one-api.dev/v2"


api_request = LotrAPI(lotr_url, headers)
character_data = api_request('character')

main_characters = []



for character in character_data:
    if character['height'] != '' and character['height'] != 'NaN':
        main_characters.append(character)

random_character = character_data[random.randrange(0, len(main_characters))]

print(random_character)

for main_character in main_characters:
    name = main_character['name']
    race = main_character['race']
    gender = main_character['gender']
    spouse = main_character['spouse']

    table = add_table_row(table, name, race, gender, spouse)
    
print(table)
