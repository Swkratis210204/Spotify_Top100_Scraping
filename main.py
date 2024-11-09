from scraping import Billboard
from spotify import Spotify
import re

date = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD: ")

ob = Billboard(date)
table = ob.scrape_billboard()
songs = []
artists = []
for i in table:
    songs.append(i[0])
    if "Featuring" in i[1]:
        name = i[1].split("Featuring")
        main_name = name[0].strip()
        featured_artists = name[1].strip() if len(name) > 1 else ""
        artists.append(f"{main_name},{featured_artists}")
    else:
        artists.append(i[1])


spotify = Spotify(date)
spotify_playlist = spotify.create_playlist(date, songs, artists)
