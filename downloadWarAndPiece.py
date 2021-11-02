#!/bin/python

"""
Downloads 'War and Piece' by Leo Tolstoy audiobook
in RU language from https://akniga.club
"""

from tqdm import tqdm
import requests

for i in range(1, 37):

  str_i = str(i).zfill(2)

  url = f"https://t2.akniga.club/b/33421/m2owf7ehbUWKQapYZaRB8w,,/{str_i}.%20%D0%A2%D0%BE%D0%BB%D1%81%D1%82%D0%BE%D0%B9%20%D0%9B%D0%B5%D0%B2%20-%20%D0%92%D0%BE%D0%B9%D0%BD%D0%B0%20%D0%B8%20%D0%BC%D0%B8%D1%80.mp3"
  print(f"Downloading {str_i}...")

  response = requests.get(url, stream=True)

  with open(f"{str_i}.mp3", "wb") as handle:
      for data in tqdm(response.iter_content()):
          handle.write(data)
