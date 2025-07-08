import os
from configparser import ConfigParser
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def readConfig(section, key):
    config = ConfigParser()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(BASE_DIR, "..", "ConfigurationData", "conf.ini")

    if not os.path.exists(CONFIG_PATH):
        logger.error(f"Configuration file not found at: {CONFIG_PATH}")
        raise FileNotFoundError(f"Configuration file not found at: {CONFIG_PATH}")

    config.read(CONFIG_PATH)

    if not config.has_section(section):
        logger.error(f"Section '{section}' not found in config file")
        raise ValueError(f"Section '{section}' not found in config file")
    if not config.has_option(section, key):
        logger.error(f"Key '{key}' not found in section '{section}'")
        raise ValueError(f"Key '{key}' not found in section '{section}'")

    value = config.get(section, key)
    logger.info(f"Read config: [{section}] {key} = {value}")
    return value