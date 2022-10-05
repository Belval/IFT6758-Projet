import numpy as np
import pandas as pd
import os
import requests
import json

NB_GAMES_SEASON = 1271

def request_game(game_nb,year):
    game_nb = str(game_nb).zfill(4)
    game_id = str(year) + '02' + game_nb
    json_path = 'data/' + game_id + '.json'

    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            response_json = json.load(f)

    else:
        response = requests.get('https://statsapi.web.nhl.com/api/v1/game/' + game_id + '/feed/live')
        response_json = response.json()

        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, 'w') as f:
            json.dump(response_json,f)

    return response_json

request_game(130,2018)
