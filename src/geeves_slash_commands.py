#! /usr/bin/env python3

import base64
import requests
import click

from credentials import read_discord_client_credentials
from pprint import pprint
from discord_api import DiscordApi


@click.group()
def geeves_slash_commands():
    pass


@geeves_slash_commands.command()
@click.argument("client_credentials_path", type=click.Path(exists=True))
def register_global(client_credentials_path):
    """
    Register the slash commands for geeves
    """

    discord_credentials = read_discord_client_credentials(client_credentials_path)
    discord_api = DiscordApi(discord_credentials)
    pprint(
        discord_api.create_global_application_commands(
            discord_credentials.client_id,
            {
                "name": "seansmagicbutton",
                "description": "Attempt to turn the valheim game server on.",
                "options": [],
            },
        )
    )

@geeves_slash_commands.command()
@click.argument("client_credentials_path", type=click.Path(exists=True))
def register_guild(client_credentials_path):
    """
    Register the slash commands for geeves with our very cool Discord server
    """

    discord_credentials = read_discord_client_credentials(client_credentials_path)
    discord_api = DiscordApi(discord_credentials)
    pprint(
        discord_api.create_guild_application_commands(
            discord_credentials.client_id,
            discord_credentials.guild_id,
            {
                "name": "seansmagicbutton",
                "description": "Attempt to turn the valheim game server on.",
                "options": [],
            },
        )
    )


@geeves_slash_commands.command()
@click.argument("client_credentials_path", type=click.Path(exists=True))
def get(client_credentials_path):
    """
    Get slash commands currently registered for geeves
    """
    discord_credentials = read_discord_client_credentials(client_credentials_path)
    discord_api = DiscordApi(discord_credentials)
    pprint(discord_api.get_global_application_commands(discord_credentials.client_id))


if __name__ == "__main__":
    geeves_slash_commands()
