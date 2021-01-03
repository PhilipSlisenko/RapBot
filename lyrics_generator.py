import random

import requests

from config import config


def generate_lyrics(prompt: str) -> str:
    base_url = config['RAP_GENERATOR_URL']
    seed = random.randint(0, 100)
    length = len(prompt.split()) * config['RAP_GENERATOR_LENGTH_MULTIPLIER']
    params = {
        'num_return_sequences': 1,
        'length': length,
        'seed': seed}
    req_url = base_url + prompt
    res = requests.get(req_url, params=params)
    return res.text
