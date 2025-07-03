import os
import json
from mcp.server.fastmcp import FastMCP
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# --- MCP Server Setup ---
mcp = FastMCP("youtube_music")

# --- YouTube API Setup ---
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_youtube_service():
    creds = None
    if os.path.exists("youtube.token"):
        creds = Credentials.from_authorized_user_file("youtube.token", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secrets.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("youtube.token", "w") as token:
            token.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)

# --- MCP Tools ---
@mcp.tool()
def list_my_playlists(query: str) -> str:
    """List my playlists containing selected word."""
    youtube = get_youtube_service()
    request = youtube.playlists().list(
        part="snippet",
        mine=True
    )
    response = request.execute()
    playlists = []
    for item in response["items"]:
        if query.lower() in item["snippet"]["title"].lower():
            playlists.append(item["snippet"]["title"])
    return "\n".join(playlists) if playlists else "No playlists found."

@mcp.tool()
def list_songs(query: str) -> str:
    """List the songs containing specified word."""
    youtube = get_youtube_service()
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        videoCategoryId="10"  # Music
    )
    response = request.execute()
    songs = []
    for item in response["items"]:
        songs.append(item["snippet"]["title"])
    return "\n".join(songs) if songs else "No songs found."

# --- AWS Lambda Handler ---
def lambda_handler(event, context):
    return mcp.run(transport='aws_lambda', event=event, context=context)

# --- Main Execution ---
if __name__ == "__main__":
    # This part is for local testing and initial authorization
    if not os.path.exists("client_secrets.json"):
        print("Please place your 'client_secrets.json' file in the root directory.")
    else:
        get_youtube_service() # This will trigger the auth flow if needed
        print("YouTube token generated successfully.")
        print("You can now deploy the server to AWS Lambda.")
