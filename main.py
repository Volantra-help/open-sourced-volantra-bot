import discord
from discord.ext import commands
from discord.ext.command import has_permissions
from discord_slash import SlashCommand # Importing the newly installed library.
import googletrans
from googletrans import Translator
import os
from dotenv import load_dotenv
import requests

load_dotenv()

client = discord.Client(intents=discord.Intents.all())
client = commands.Bot(command_prefix = '!',intents=discord.Intents.all())  # you can change this
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client xd

@slash.slash()
async def track(ctx, user: discord.Member = None):
    user = user or ctx.author
    spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)

    if spotify_result is None:
     await ctx.send(f'{user.name} is not listening to Spotify....')

    await ctx.send(f'https://open.spotify.com/track/{spotify_result.track_id}')



@slash.slash()
async def servers(ctx):
    a = discord.Embed(title="List of Guilds", description=f"{len(client.guilds)}")
    await ctx.send(embed=a)




@slash.slash()
async def translate(ctx, lang, *, args):
    e = discord.Embed(title="Translation successful",description="Translated")
    t = Translator()
    a = t.translate(args, dest=lang)
    await ctx.send(embed=e)
    await ctx.send(a.text)


token = os.getenv('DISCORD_TOKEN')

client.run(token)
