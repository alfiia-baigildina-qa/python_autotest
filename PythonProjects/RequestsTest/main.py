import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e09af5e892b34b3c92cd36a5d8ee41e5'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN} 
{
    "name": "generate",
    "photo_id": -1
}
'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)''' 
update_data = {
    "pokemon_id": "124016",
    "name": "New Name",
    "photo_id": 2
}                   
'''update_response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = update_data) 
print(update_response.text)'''  
 
catch_data = {
    "pokemon_id": "124016"
}

catch_response = requests.post(f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_data)
print("Поймать покемона в покебол:", catch_response.json())