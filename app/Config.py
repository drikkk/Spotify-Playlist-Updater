import os

from configparser import ConfigParser
from configparser import NoOptionError
from configparser import ParsingError
from app.CustomLogger import CustomLogger

log = CustomLogger(__name__)


class Config:
    CONFIG_NAME = "config.ini"
    config = ConfigParser()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_dir, "..", CONFIG_NAME)

    try:
        with open(config_file_path, 'r') as file:
            config.read_file(file)
    except FileNotFoundError:
        log.error(f"Could not find {CONFIG_NAME} from root directory.")
        raise FileNotFoundError
    except ParsingError:
        log.error(f"Failed to parse {CONFIG_NAME}")
        raise ParsingError

    try:
        refresher_token = config.get('API', 'refresher_token')
        client = config.get('API', 'client')
        secret = config.get('API', 'secret')
    except NoOptionError:
        log.error(f"Could not read {CONFIG_NAME} values.")
        raise NoOptionError

    missing_config_keys = []
    if refresher_token == '':
        missing_config_keys.append('refresher_token')
    if client == '':
        missing_config_keys.append('client')
    if secret == '':
        missing_config_keys.append('secret')

    if missing_config_keys:
        for key in missing_config_keys:
            log.error(f"Empty value for [{key}] in {CONFIG_NAME} file.")
        raise ValueError
