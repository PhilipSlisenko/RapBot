import io
import os
import random

from pydub import AudioSegment


def mix_song(speech: bytes) -> bytes:
    minus = AudioSegment.from_ogg(get_minus_path('./minuses'))
    with io.BytesIO(speech) as s:
        speech = AudioSegment.from_ogg(s) + 2  # Make voice 2 db louder
    mix = minus.overlay(speech)[:min(len(speech), len(minus))]
    with io.BytesIO() as f:
        mix.export(f, format='ogg')
        f.seek(0)
        mix_bytes = f.read()
    return mix_bytes


def get_minus_path(all_minuses_root: str = './minuses') -> str:
    all_minuses_paths = [file_ for file_ in os.listdir(all_minuses_root) if file_.endswith('.ogg')]
    return random.choice(all_minuses_paths)
