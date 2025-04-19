from mcp.server.fastmcp import FastMCP
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "<your-spotify-client-id>"
SPOTIPY_CLIENT_SECRET = "<your-spotify-client-secret>"
SPOTIPY_REDIRECT_URI = "http://127.0.0.1:8888/callback"
SPOTIPY_SCOPE = "user-modify-playback-state user-read-playback-state"

spotify_client: Spotify = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SPOTIPY_SCOPE,
    )
)


mcp: FastMCP = FastMCP(
    name="Spotify MCP",
    description="A MCP for Spotify",
)


@mcp.tool()
def search(song_name: str):
    """Search for a song on Spotify"""
    results = spotify_client.search(q=song_name, type="track")
    return results["tracks"]["items"][0]["uri"]


@mcp.tool()
def play(song_uri: str):
    """Play a song on Spotify"""
    spotify_client.start_playback(uris=[song_uri])
    return "Playing song"


@mcp.tool()
def pause():
    """Pause a song on Spotify"""
    spotify_client.pause_playback()
    return "Paused song"


if __name__ == "__main__":
    mcp.run()
