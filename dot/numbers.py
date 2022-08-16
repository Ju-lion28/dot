import discord
import json
import requests

def number(cat, num):
  response = requests.get(f'http://numbersapi.com/{num}/{cat}?json')
  json_data = json.loads(response.text)

  text = json_data["text"]
  number = json_data["number"]
  category = json_data["type"]

  colour = discord.Colour.from_rgb(252, 186, 3)

  facts = discord.Embed(title=number, description=text, colour=colour)
  facts.set_footer(text=category.upper())

  return facts