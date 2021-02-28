import base64
import requests
import click

from credentials import read_discord_client_credentials, get_token
from pprint import pprint


@click.command()
@click.argument("client_credentials_path", type=click.Path(exists=True))
def register_slash_commands(client_credentials_path):
    """
    Register the slash commands for geeves with our very cool Discord server
    """

    discord_credentials = read_discord_client_credentials(client_credentials_path)
    token = get_token(discord_credentials)

    #url = f"https://discord.com/api/v8/applications/{discord_credentials.client_id}/guilds/{discord_credentials.guild_id}/commands"
    url = f"https://discord.com/api/v8/applications/{discord_credentials.client_id}/commands"

    slash_command_definition = {
        "name": "seansmagicbutton",
        "description": "Attempt to turn the valheim game server on.",
        "options": [],
    }

    headers = {"Authorization": f"Bearer {token.access_token}"}

    r = requests.post(url, headers=headers, json=slash_command_definition)
    r.raise_for_status()
    pprint(r.json())

if __name__ == "__main__":
    register_slash_commands()