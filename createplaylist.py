import json
import requests
from secrets.py import spotify_user_id, spotify_token

class CreatePlaylist: 
  def __init__(self):
    self.user_id = spotify_user_id

  def getYoutubeClient(self):
    pass

  def getLikedVideos(self):
    pass

  def createPlaylist(self):
    request_body = json.dumps(
      "name": "Youtube Liked Vids",
      "description": "All Liked Youtube Videos",
      "public": True
    )

    query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
    response = requests.post(
      query,
      data = request_body,
      headers={
        "Content-Type":"application/json",
         "Authorization":"Bearer {}".format(spotify_token)
      }
    )
    response.json = response.json()

    return response_json["id"]

  def getSpotifyUri(self, song_name, artist):
    query = "https://api.spotify.com/v1/search?q=track:{}%20artist:{}&type=track" -H "Authorization: Bearer {your access token}"

  def addSongToPlaylist(self):
    pass