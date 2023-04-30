import requests
import spotipy
import pprint
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# SPOTIPY_CLIENT_ID = "23b35b25e5414b218e78950161dc7e64"
# SPOTIPY_CLIENT_SECRET = "8a8d6b9ac16e4390853269d8d8ebb733"
# OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
# OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
# REDIRECT_URI = "http://example.com"

which_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
print(which_year)

url = f"https://www.billboard.com/charts/hot-100/{which_year}"

# connect with the website
response = requests.get(url)
contents = response.text

# soup
soup = BeautifulSoup(contents, "html.parser")
rows = soup.find_all(name="h3", id="title-of-a-story",
                     class_="a-no-trucate")

# get name of songs in a list
name_of_songs = []
for row in rows:
    name_with_spaces = row.getText()
    name = ''.join(c for c in name_with_spaces if c != '\n' and c != '\t')
    name_of_songs.append(name)
print(name_of_songs)

# authenticate spotipy
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private, playlist-modify-public",
        show_dialog=True,
        cache_path="token.txt"
    ))

# current user
user_id = sp.current_user()["id"]
print(f"user_id = {user_id}")

# pprint setting
pp = pprint.PrettyPrinter(indent=2)

# list of searched tracks
list_of_tracks = []

print(f"search year = {which_year[:4]}")

# search track id for every song in billboard chart
# search(q, limit=10, offset=0, type='track', market=None)
for song in name_of_songs:
    try:
        searched_track = sp.search(
            q=f"remaster%20track:{song}%20year:{which_year[:4]}",
            type="track",
            limit=1
            )
        searched_track_id = searched_track["tracks"]["items"][0]["id"]
    except IndexError:
        print(f"{song} can't be found in Spotify.")
    else:
        # print(f"{song} {searched_track_id}")
        list_of_tracks.append(searched_track_id)

print(f"list of track id = {list_of_tracks}")


# create a playlist
# user_playlist_create(user, name, public=True, description='')
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{which_year} Billboard 100",
    description="A small project to practice API using")
pp.pprint(playlist)
playlist_id = playlist["id"]
print(f"playlist id = {playlist_id}")


# add every track to the playlist
# user_playlist_add_tracks(user, playlist_id, tracks, position=None)
add_tracks_result = sp.user_playlist_add_tracks(
    user=user_id,
    playlist_id=playlist_id,
    tracks=list_of_tracks)

