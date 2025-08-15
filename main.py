import discord
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
target_id = int(os.getenv('TARGET_USER_ID'))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == target_id:
        emojis = ['🇸', '🇾', '🇧', '🇦', '🇺']
        
        #run everything at once
        await asyncio.gather(
            *(message.add_reaction(emoji) for emoji in emojis),
            message.channel.send('neil sybau')
        )

client.run(token)