import numpy as np
import pandas as pd
import requests

NB_GAMES_SEASON = 1271

def request_game(game_nb,year):
    game_id = str(year) + '02' + game_nb
    response = requests.get('https://statsapi.web.nhl.com/api/v1/game/' + game_id + '/feed/live')
    response_json = response.json()

    return response_json


print(request_game('0001',2018))
