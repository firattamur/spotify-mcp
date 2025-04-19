# Spotify MCP

A Model Control Protocol (MCP) integration for Spotify that allows you to control your Spotify playback through AI assistants.

## Features

- **Search**: Search for songs on Spotify
- **Play**: Play songs on your active Spotify device
- **Pause**: Pause currently playing music

## Prerequisites

- Python 3.11 or higher
- Spotify Developer credentials

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/spotify-mcp.git
   cd spotify-mcp
   ```

2. Set up a virtual environment:
   ```bash
   uv venv
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

## Configuration

1. Create a Spotify application at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)

2. Get your Client ID and Client Secret from your Spotify application

3. Update `main.py` with your credentials:
   ```python
   SPOTIPY_CLIENT_ID = "your-spotify-client-id"
   SPOTIPY_CLIENT_SECRET = "your-spotify-client-secret"
   ```

## Usage

Run the MCP server:
```bash
python main.py
```

When you run the application for the first time, a browser window will open asking you to log in to your Spotify account and authorize the application.

## How It Works

This project uses:
- [MCP (Model Control Protocol)](https://github.com/model-control-protocol/mcp): For creating AI-controlled tools
- [Spotipy](https://spotipy.readthedocs.io/): Python client for the Spotify Web API

The MCP server exposes three functions that can be called by AI assistants:
- `search`: Find songs on Spotify
- `play`: Play a specific song
- `pause`: Pause the currently playing song

