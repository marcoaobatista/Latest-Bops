import requests
import base64
import json
from os import environ
from dotenv import load_dotenv

LAST_N_TRACKS = 15

class SpotifyClient():
    def __init__(self, token):
        self.TOKEN = token

    def get_latest_tracks_uris(self, playlist_id):
        headers = {
            "Authorization": f"Bearer {self.TOKEN}",
        }

        # Get the total number of tracks in the playlist.
        response = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=total",
                                headers=headers)

        if response.status_code != 200:
            raise Exception("Failed to get playlist: ", response.content)

        total_tracks = response.json()['total']

        # Calculate the offset from the beginning of the list.
        offset = max(total_tracks - LAST_N_TRACKS, 0)

        # Get the track at that offset.
        response = requests.get(
            f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items%28track%28name%2Curi%29%29&offset={offset}",
            headers=headers)

        if response.status_code != 200:
            raise Exception("Failed to get playlist tracks: ", response.content)

        tracks = response.json()['items']

        uris = [track['track']['uri'] for track in tracks]
        uris.reverse()

        return uris

    def add_to_playlist(self, playlist_id, uris):
        headers = {
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json"
        }

        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        data = json.dumps({"uris": uris, "position": 0})

        response = requests.post(url, headers=headers, data=data)

        if response.status_code != 201:
            raise Exception("Failed to add tracks to playlist: ", response.content)

        print("Successfully added tracks to playlist.")

    def delete_tracks_from_playlist(self, playlist_id):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        headers = {
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to get playlist tracks: ", response.content)

        tracks = response.json()['items']
        uris = [{"uri": track['track']['uri']} for track in tracks]

        data = json.dumps({"tracks": uris})

        response = requests.delete(url, headers=headers, data=data)

        if response.status_code != 200:
            raise Exception("Failed to delete tracks from playlist: ", response.content)

        print("Successfully deleted tracks from playlist.")


def get_access_token(client_id, client_secret, refresh_token):
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode('utf-8')).decode('utf-8')

    headers = {
        "Authorization": f"Basic {auth_header}",
    }

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

    if response.status_code != 200:
        raise Exception("Failed to refresh access token: ", response.content)

    access_token = response.json()['access_token']

    print("Successfully got access token")

    return access_token

def main():
    load_dotenv()

    client_id = environ['SPOTIFY_LTBS_CLIENT_ID']
    client_secret = environ['SPOTIFY_LTBS_CLIENT_SECRET']
    refresh_token = environ['SPOTIFY_LTBS_REFRESH_TOKEN']
    main_playlist_id = environ['SPOTIFY_LTBS_SOURCE_ID']
    target_playlist_id = environ['SPOTIFY_LTBS_TARGET_ID']

    access_token = get_access_token(client_id, client_secret, refresh_token)

    spotify_client = SpotifyClient(access_token)

    spotify_client.delete_tracks_from_playlist(target_playlist_id)
    uris = spotify_client.get_latest_tracks_uris(main_playlist_id)
    spotify_client.add_to_playlist(target_playlist_id, uris)


if __name__ == "__main__":
    main()