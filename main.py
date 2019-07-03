# Daooda BA
# WeekEnd-Challenge-3

import os
import csv
import requests
from bs4 import BeautifulSoup

requete = requests.get("https://www.brainyquote.com/top_100_quotes")
brainyquote = requete.content
recup = BeautifulSoup(brainyquote)

div = recup.find_all("div", {"class": "listPositionNum"})
span = recup.find_all("span", {"class": "block-quote"})
desc = recup.find_all("a", {"class": "block-author"})

liste_nombre = [elt.string.strip() for elt in div]
liste_quote = [elt.string.strip() for elt in span]
liste_nom = [elt.string.strip() for elt in desc]

with open("files.csv", "w", encoding="utf-8") as fichier
    writer = csv.writer(fichier)

j = len(liste_nombre)
i = 0
with open("files.csv", "w", encoding="utf-8") as fichier
    writer = csv.writer(fichier)
    while i < j:
        writer.writerow((liste_nombre[i], liste_quote[i], liste_nom[i]))
        i+=1