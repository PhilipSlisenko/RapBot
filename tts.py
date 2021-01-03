import requests

from config import config


def generate_speech_from_text(text: str) -> bytes:
    params = {'message': text, 'speed': 1.0, 'emotion': 'evil', 'voice': 'zahar'}
    url = config['TTS_URL']
    resp = requests.get(url, params=params)
    return resp.content
