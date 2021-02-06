# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from future.utils import bytes_to_native_str as n
import codecs
class Team:
  def __init__(self, name, league):
    self.name = name
    self.league = league

f = codecs.open("TeamBundisliga.txt", "r",'utf-8')
team = []
s = '1. FC Köln'
print(s)
for x in f:
 
  team.append(x)


s=""

for t in team:
    t.strip()
    s += f'"{t.strip()}",'

for i in range(0,len(team)):
    s += f'"Bundesliga",'
print(s)

print(u'"1. FC KÃ¶ln"')