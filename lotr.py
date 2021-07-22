import config
import random
import json
from api_config import LotrAPI

auth_string = 'Bearer ' + config.LOTR_ACCESS_TOKEN

headers = {
    'Accept': 'application.json',
    'Authorization': auth_string,
}

lotr_url = "https://the-one-api.dev/v2"


api_request = LotrAPI(lotr_url, headers)
character_data = api_request.get_data('character')

def create_message(formatted_character):
    name = formatted_character['name']
    height = formatted_character['height']
    race = formatted_character['race']
    gender = formatted_character['gender']
    birth = formatted_character['birth']
    death = formatted_character['death']
    realm = formatted_character['realm']
    spouse = formatted_character['spouse']
    wiki = formatted_character['wikiUrl']
    hair = formatted_character['hair']
    if gender == 'Male':
        pronoun = 'His'
    elif gender == 'Female':
        pronoun = 'Her'
    else:
        pronoun = 'Their'
    if spouse == 'Unknown':
        spouse = 'They are unmarried'
    else:
        spouse = 'They are married to ' + spouse

    message = f'{name} is a {gender} {race} from {realm}. {pronoun} size is {height} and {pronoun} hair is {hair}. {pronoun} birth year is {birth}, and their death year is {death}.  {spouse}. READ MORE: {wiki}'
    add_to_file(message)
    return message

def add_to_file(message):
    with open('character_desc.txt', 'a') as outfile:
        json.dump(message, outfile)
        outfile.write('\n \n')

def create_character(character_data):
    formatted_character = {}
    try:
        for key, value in character_data.items():
            if value == '' or value == 'NaN':
                value = 'UNKNOWN ' + key.upper()
            formatted_character[key] = value
    except KeyError:
        pass
    return formatted_character
main_characters = []

for character in character_data:
    try:
        if character['wikiUrl']:
            main_characters.append(character)
    except KeyError:
        continue

random_character = character_data[random.randrange(0, len(main_characters))]

formatted_char = create_character(random_character)

message_to_send = create_message(formatted_char)
