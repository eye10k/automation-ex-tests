import os
from configparser import ConfigParser

def readConfig(section, key):
    config = ConfigParser()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directory where configReader.py is located
    CONFIG_PATH = os.path.join(BASE_DIR, "..", "ConfigurationData", "conf.ini")  # Navigate to conf.ini

    # Проверка существования файла
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Configuration file not found at: {CONFIG_PATH}")

    config.read(CONFIG_PATH)

    # Проверка существования секции и ключа
    if not config.has_section(section):
        raise ValueError(f"Section '{section}' not found in config file")
    if not config.has_option(section, key):
        raise ValueError(f"Key '{key}' not found in section '{section}'")

    return config.get(section, key)
