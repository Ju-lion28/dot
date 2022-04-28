import requests
import discord
import json

def text_generator(text : str):
  r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
      'text': text,
    },
    headers={'api-key': '3a1a25cc-12ea-451c-a10a-0c1c7c3374aa'}
  )
  json_data = json.loads(r.text)

  formated = f"```{json_data}```"
  
  return formated