import discord
import argparse

parser = argparse.ArgumentParser(description='List all channels and IDs a bot token has')
parser.add_argument('token', help='Bot token')
token = parser.parse_args().token

client = discord.Client()

@client.event
async def on_ready():
    for c in client.get_all_channels():
        print(f'{c.guild} #{c.name} - {c.id}')
    await client.close()

client.run(token)
