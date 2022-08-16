import os
import json
import random
import discord
import requests
import keep_alive
from discord.ext import commands
import dot.engine, dot.short, dot.numbers
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

token = os.environ['TOKEN']
bot = commands.Bot(command_prefix='.')
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command('help')

@bot.event
async def on_ready():
  await bot.change_presence(
    activity=discord.Activity(
      type=discord.ActivityType.watching,
      name="you from a distance"
    )
  )

  print(f'Logged in as {bot.user} (ID: {bot.user.id})')
  print('------')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('I use slash commands')

@slash.slash(name='Ping', description="Check the bot's latency.")
async def ping(ctx:SlashContext):
  """Check out Dot's latency."""
  await ctx.send(f'Pong... `{round(bot.latency * 1000)}ms`')

@slash.slash(name='Search', description='Searches something on google.',
            options=[
              create_option(
                name="query",
                description="Your search:",
                option_type=3,
                required=True
              )
            ])

async def search(ctx:SlashContext, query:str):
  await ctx.send(embed=dot.engine.search(query))

@slash.slash(name='Shorten', description='Link shortener')
async def shorten(ctx:SlashContext, url:str):
  await ctx.send(embed=dot.short.shorten(url))

@slash.slash(name='QR', description='Make a QR code')
async def QR(ctx:SlashContext, link:str, size:int = 0):
  await ctx.send(f'https://qrtag.net/api/qr_{size}.png?url={link}')

@slash.slash(
  name='numberfacts', 
  description='Random Fatcs on Random Numbers',
  options=[
    create_option(
      name="category",
      description="Pick out of four different categories of facts.",
      option_type=3,
      required=False,
      choices=[
        "Trivia",
        "Year",
        "Date",
        "Math"
      ]
    ),
    create_option(
      name="number",
      description="If you want a specific number",
      option_type=4,
      required=False
    )
  ]
)
async def numberfacts(ctx:SlashContext, category:str = 'trivia', number:int = 'random'):
  await ctx.send(embed=dot.numbers.number(category.lower(), number))

keep_alive.keep_alive()
bot.run(token)