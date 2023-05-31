from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time

# Set up the API client
DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# Define the channel ID
channel_id = "UCpeGzDObn7SZPcMmY-PQzMQ" # Bunz
times=0
last_video_id = ""



# Make the API request to retrieve the channel's videos
def check():
    global times, last_video_id
    if times==0:
        times+=1
        print("First time running. Skipping...")
        return False

    try:
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

        # Print the video id and last video id
        #print(f'Video ID: {video_id}, Last Video ID: {last_video_id}')

        if video_id != last_video_id:
            last_video_id = video_id
            return f"{channel_name} just uploaded a new video!\n{video_title}\n{link}"
        else:
            #print("No new videos.")
            return False

    except HttpError as e:
        print(f"An error occurred: {e} at {time.strftime('%H:%M:%S', time.localtime())}")
        return "An error occurred: %s" % e

