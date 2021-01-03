import os

config = {
    "TELEGRAM_API_KEY": os.environ['TELEGRAM_API_KEY'],
    "RAP_GENERATOR_URL": os.environ['RAP_GENERATOR_URL'],
    "RAP_GENERATOR_LENGTH_MULTIPLIER": int(os.getenv('RAP_GENERATOR_LENGTH_MULTIPLIER', '9')),  # The bigger it is, the
    # bigger length of generated rap will be
    "TTS_URL": os.environ['TTS_URL'],
}
