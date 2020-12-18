from youtube_client import YouTubeClient
from spotify_client import SpotifyClient
import os


def run():
    #1. Get a list of playlist from YT
    youtube_client=YouTubeClient('./creds/client_secret.json')
    spotify_client=SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists=youtube_client.get_playlists()


    #2 Ask which playlist we want MV from
    for index,playlist in enumerate(playlists):
        print(f"{index}:{playlist.title}")
    choice=int(input("Enter your choice"))
    chosen_playlist=playlists[choice]
    print(f"You selected: {chosen_playlist.title}")


    #3 For each vid get song information from Yt
    
    songs = youtube_client.get_videos_from_playlists(chosen_playlist.id)
    print(f"Attempting to add {len(songs)}")


    #4 Search for songs on Spotify
    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist} - {song.track} to your Spotify Liked Songs")




if __name__=='__main__':
    run()
