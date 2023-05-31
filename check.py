from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time
from options import DEVELOPER_KEY, CHANNEL_IDS

# Set up the API client

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# Define the channel IDs
last_video_ids = {}

# Make the API request to retrieve the channels' videos


def check():
    try:
        for channel_id in CHANNEL_IDS:
            search_response = youtube.search().list(
                channelId=channel_id,
                type="video",
                part="id,snippet",
                maxResults=1,
                order="date"
            ).execute()

            # Extract the video ID and title from the API response
            channel_name = search_response["items"][0]["snippet"]["channelTitle"]
            video_id = search_response["items"][0]["id"]["videoId"]
            video_title = search_response["items"][0]["snippet"]["title"]
            link = "https://www.youtube.com/watch?v=" + video_id

            # Check if the channel is already in the dictionary
            if channel_id in last_video_ids:
                last_video_id = last_video_ids[channel_id]
            else:
                last_video_id = None

            # Compare the current video ID with the last video ID for the channel
            if video_id != last_video_id:
                last_video_ids[channel_id] = video_id
                message = f"{channel_name} just uploaded a new video!\n{video_title}\n{link}"
                return message
                # You can send the message or perform any other action here
            else:
                pass
                #print(f"No new videos for {channel_name}.")

    except HttpError as e:
        print(f"An error occurred: {e} at {time.strftime('%H:%M:%S', time.localtime())}")
        return "An error occurred: %s" % e
