# import dotenv
# import os
# from pathlib import Path

# current_dir = Path(__file__).parent.absolute()


# env_file = os.getenv("SCWEET_ENV_FILE", current_dir.parent.joinpath(".env"))
# dotenv.load_dotenv(env_file, verbose=True)


# def load_env_variable(key, default_value=None, none_allowed=False):
#     v = os.getenv(key, default=default_value)
#     if v is None and not none_allowed:
#         raise RuntimeError(f"{key} returned {v} but this is not allowed!")
#     return v


# def get_email(env):
#     dotenv.load_dotenv(env, verbose=True)
#     return load_env_variable("TWITTER_EMAIL", none_allowed=True)


# def get_password(env):
#     dotenv.load_dotenv(env, verbose=True)
#     return load_env_variable("TWITTER_PASSWORD", none_allowed=True)


# def get_username(env):
#     dotenv.load_dotenv(env, verbose=True)
#     return load_env_variable("TWITTER_USERNAME", none_allowed=True)


import os
import random
import time
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import dotenv

def load_env_variable(key, default_value=None, none_allowed=False):
    v = os.getenv(key, default=default_value)
    if v is None and not none_allowed:
        raise RuntimeError(f"{key} returned {v} but this is not allowed!")
    return v

def get_email(env):
    dotenv.load_dotenv(env, verbose=True)
    return load_env_variable("TWITTER_EMAIL", none_allowed=True)

def get_password(env):
    dotenv.load_dotenv(env, verbose=True)
    return load_env_variable("TWITTER_PASSWORD", none_allowed=True)

def get_username(env):
    dotenv.load_dotenv(env, verbose=True)
    return load_env_variable("TWITTER_USERNAME", none_allowed=True)

