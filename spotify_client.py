

import requests
import urllib.parse

class SpotifyClient(object):
    def __init__(self,api_token):
        self.api_token=api_token


    def search_song(self,artist,track):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            track,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.api_token)
            }
        )
        response_json = response.json()
        songs = response_json['tracks']['items']
        # only use the first song
        uri = songs[0]["uri"]

        return uri


    def add_song_to_spotify(self,song_id):
        url="http//api.spotify.com/v1/me/tracks"
        response=requests.put(
            url,
            json={
                "ids":[song_id]
                },
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {self.api_token}"
                }
            )
        return response.ok
    




