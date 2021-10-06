from pprint import pprint
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
USER = os.environ.get("USER")

user_choice = input("Enter date of choice for top 100 songs of that day(YYYY-MM-DD):\n")


response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_choice}")
html = response.text
soup = BeautifulSoup(html, "html.parser")

# adding songs into list after finding them
song_titles = soup.find_all(name="span", class_="chart-element__information__song")
song_list = [song.getText() for song in song_titles]
# print(song_list)

# Getting authorization and establishing profile with spotipy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE,
                                               username=USER))

results = sp.current_user()
USER = results["id"]


year = user_choice.split("-")[0]
print(year)

playlist = sp.user_playlist_create(user=USER, name=f"{user_choice} Billboard 100", public=False, collaborative=False, description=f"Top 100 songs for the week of {user_choice}")
print(playlist["id"])

tracks = []

# Searching for song
for songs in song_list:
    results = sp.search(q=f"track:{songs} year{year}",type="track")
    # print(results)

    try:
        uri = results["tracks"]["items"][0]["uri"]
        tracks.append(uri)
        # sp.playlist_add_items(playlist_id=playlist["id"], items=uri)
    except IndexError:
        print(f"{songs} doesn't exist in Spotify. Skipped")

pprint(tracks)
sp.user_playlist_add_tracks(user=USER, playlist_id=playlist["id"], tracks=tracks)
# for track in tracks:
