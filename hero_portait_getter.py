import scrapy
import os
import wget


with open('heros.txt', 'r') as f:
    for line in f:
        line = line.strip().lower().replace(" ", "_").replace("'","")
        file = wget.download("http://cdn.dota2.com/apps/dota2/images/heroes/" + line + "_vert.jpg")
