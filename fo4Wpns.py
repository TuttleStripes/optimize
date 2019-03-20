'''
Example:
finds the optimal weapon for each of the stats: Damage per shot, Damage per second, Fire rate, Range, Accuracy
'''

from bs4 import BeautifulSoup
from itertools import chain
import numpy as np
import optimize
import re
import requests


req = requests.get('https://fallout.fandom.com/wiki/Fallout_4_weapons')
soup = BeautifulSoup(req.text, 'html.parser')

ranged = soup.find_all('table')[7:12]
data = [[td.get_text().strip() for td in i.find_all('td')] for i in ranged]
data = np.array(list(chain(*data))).reshape(-1, 16)
usedData = data[:, 1:7]

#weapon names
names = usedData.transpose()[0]

#constructes the weapon statistics
stats = usedData[:, 1:]
flat = list(stats.flatten())
for i, v in enumerate(flat):
  try:
    flat[i] = float(v)
  except ValueError:
    flat[i] = float('nan')
stats = np.array(flat).reshape(-1, 5)

#stat titles: Damage per shot, Damage per second, Fire rate, Range, Accuracy
span = [i.find('span') for i in ranged[0].find_all('th')]
titles = []
for i in span:
  try:
    titles.append(i['title'])
  except:
    pass
titles = titles[1:6]

#THIS IS WHERE I USE OPTIMIZE!!!
#finds the optimal weapon for each stat in titles
optimized = dict(
  (titles[i], tuple(usedData[optimize.forIndex(stats, i), [0,i+1]]))
  for i in range(5)
)

for k, v in optimized.items():
  print(f'{k}:', end='\n\t')
  print(f'Weapon: {v[0]}', end='\n\t')
  print(f'Stat: {v[1]}')
