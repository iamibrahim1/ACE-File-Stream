# (c) adarsh-goel

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('25184668'))
    API_HASH = str(getenv('9de2fcd18b25deed06adf855fcd181ed'))
    BOT_TOKEN = str(getenv('6059388276:AAHoqxS5YQXAiDir1AlxZJR8f6zEHwJYIBQ'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'F2LxBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('-1001955345051'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(getenv('OWNER_ID', '5390385209'))
    NO_PORT = bool(getenv('NO_PORT', True))
    APP_NAME = lucierfiletolink
    OWNER_USERNAME = str(getenv('Lucifer6985'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('lucierfiletolink'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('mongodb+srv://Ibrahim:ibrahim@cluster0.onq4xpo.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
