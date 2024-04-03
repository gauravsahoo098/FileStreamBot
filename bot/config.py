from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 27287371))
    API_HASH = env.get("TELEGRAM_API_HASH", "d85872e77a1dedc1829ff27727f5d393")
    OWNER_ID = int(env.get("OWNER_ID", 7080468611))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "7080468611").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "sahoovpsbot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6838132221:AAHcyCK9Qej7lN7bGpuSMlRvmXUiaZLTO9k")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002079351549))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://uclaadhar.cloud")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "uclaadhar.cloud")
    PORT = int(env.get("PORT", 80))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
