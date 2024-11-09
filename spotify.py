import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    def __init__(self, date):
        self.year = date[:4]
        self.client_id = "67138083f2be452b9f8d43ace3545d7a"
        self.client_secret = "ba6e4f9829ea4f9dbff980eec28ddc31"
        self.redirect_uri = 'http://example.com'
        scope = 'playlist-modify-private'
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope=scope,
                redirect_uri=self.redirect_uri,
                client_id=self.client_id,
                client_secret=self.client_secret,
                show_dialog=True,
                cache_path="token.txt",
                username="Swkratis",
            )
        )
        self.user_id = self.sp.current_user()["id"]

    def create_list(self, songs, artists):
        song_uris = []
        for n in range(len(songs)):
            uri = self.get_song_uri(songs[n], artists[n])
            if uri != 'N/A':
                song_uris.append(uri)
            else:
                pass
                # print(f"URI not found for song: {songs[n]}, artist: {artists[n]}")
        return song_uris

    def get_song_uri(self, song, artist):
        try:
            query = f"track:{song} artist:{artist}"
            results = self.sp.search(q=query, limit=1, type='track')
            if results['tracks']['items']:
                return results['tracks']['items'][0]['uri']
            else:
                return 'N/A'
        except Exception as e:
            print(f"An error occurred: {e}")
            return 'N/A'

    def create_playlist(self, date, list_songs, artists):
        playlist = self.sp.user_playlist_create(user=self.user_id, name=date, description=f"Top 100 songs of {date}",
                                                public=False)
        playlist_id = playlist['id']
        songs = self.create_list(list_songs, artists)
        self.sp.playlist_add_items(playlist_id, songs)
