import requests
from collections import namedtuple

DiscordCredentials = namedtuple(
    "DiscordCredentials", "client_id client_secret guild_id"
)

DiscordToken = namedtuple("DiscordToken", "access_token scope token_type expires_in")


def get_token(discord_credentials):
    data = {
        "grant_type": "client_credentials",
        "scope": "bot applications.commands.update applications.commands",
        "client_id": discord_credentials.client_id,
        "guild_id": discord_credentials.guild_id,
        "response_type": "code",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(
        "https://discord.com/api/v8/oauth2/token",
        data=data,
        headers=headers,
        auth=(discord_credentials.client_id, discord_credentials.client_secret),
    )
    r.raise_for_status()
    return DiscordToken(**r.json())


def read_discord_client_credentials(discord_client_credentials_path):
    with open(discord_client_credentials_path) as f:
        lines = [line.strip() for line in f]
    return DiscordCredentials(lines[0], lines[1], lines[2])
