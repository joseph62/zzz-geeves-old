import requests

from credentials import get_token

BASE_URL = "https://discord.com/api/v8"


class DiscordApi:
    def __init__(self, discord_credentials):
        self.discord_token = get_token(discord_credentials)
        self.headers = {"Authorization": f"Bearer {self.discord_token.access_token}"}

    def _create_application_commands(self, command_definition, url):
        r = requests.post(url, headers=self.headers, json=command_definition)
        r.raise_for_status()
        return r.json()

    def create_guild_application_commands(
        self, client_id, guild_id, command_definition
    ):
        url = f"{BASE_URL}/applications/{client_id}/guilds/{guild_id}/commands"
        return self._create_application_commands(command_definition, url)

    def create_global_application_commands(self, client_id, command_definition):
        url = f"{BASE_URL}/applications/{client_id}/commands"
        return self._create_application_commands(command_definition, url)

    def get_global_application_commands(self, client_id):
        url = f"{BASE_URL}/applications/{client_id}/commands"
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        return r.json()
