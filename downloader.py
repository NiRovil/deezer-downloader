from pydeezer import Deezer, Downloader
from pydeezer.constants import track_formats
import time
import requests
import json

# arl para efetuar o login na plataforma
arl = ""
deezer = Deezer(arl=arl)
download_dir = "" # diretório para salvar as musicas

URL = "" # http://api.deezer.com/ 'complementar com a playlist/album aqui'
response = requests.get(URL)

songs = []

with open('apideezer.json', 'w') as file:
    for id in response:
        file.write(id.decode('utf8'))
    file.close()

f = open('apideezer.json')
data = json.load(f)

for item in data['tracks']['data']:
    songs.append(item['id'])

downloader = Downloader(deezer, songs, download_dir, quality=track_formats.MP3_320, concurrent_downloads=2)
downloader.start()