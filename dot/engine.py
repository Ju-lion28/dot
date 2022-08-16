import os
import json
import discord
import requests

api_key = os.environ['ENGINE']


def search(query):
  response = requests.get(
    f'https://serpapi.com/search.json?engine=google&q={query}&api_key={api_key}'
  )
  json_data = json.loads(response.text)

  title = f'Google search result for: {query}'
  search_url = json_data["search_metadata"]["google_url"]
  description = 'These are the first 4 links that show up to your search on google.'
  google_colour = discord.Colour.from_rgb(219, 68, 55)
  
  title1 = json_data["organic_results"][0]["title"]
  link1 = json_data["organic_results"][0]["link"]
  
  title2 = json_data["organic_results"][1]["title"]
  link2 = json_data["organic_results"][1]["link"]
  
  title3 = json_data["organic_results"][2]["title"]
  link3 = json_data["organic_results"][2]["link"]
    
  title4 = json_data["organic_results"][3]["title"]
  link4 = json_data["organic_results"][3]["link"]

  embed = discord.Embed(title=title, url=search_url, description=description, colour=google_colour)

  embed.add_field(name=f'**1**: {title1}', value=link1, inline=False)
  embed.add_field(name=f'**2**: {title2}', value=link2, inline=False)
  embed.add_field(name=f'**3**: {title3}', value=link3, inline=False)
  embed.add_field(name=f'**4**: {title4}', value=link4, inline=False)

  return embed