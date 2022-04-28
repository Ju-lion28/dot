import os
import json
import discord
import requests

def shorten(long_url):
  response = requests.get(f'https://api.shrtco.de/v2/shorten?url={long_url}')
  json_data = json.loads(response.text)

  long_link = json_data["result"]["original_link"]

  short1 = json_data["result"]["full_short_link"]
  short2 = json_data["result"]["full_short_link2"]

  title = "Link Shortener"
  description = f"""Original link: {long_link}
  ⮩ Shortened v1: {short1}
  ⮩ Shortened v2: {short2}"""
  colour = discord.Colour.from_rgb(33,37,63)
  
  stuff = discord.Embed(title=title, description=description, colour=colour)
  stuff.set_footer(text='Both links do the same thing')

  return stuff