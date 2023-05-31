# YouTube Channel Watcher Bot
This code sets up a bot that monitors a specific YouTube channel for new video uploads and sends a notification to a Discord channel when a new video is detected. It utilizes the YouTube Data API v3 and the Discord.py library.

## Prerequisites
Before running this code, make sure you have the following:

Google API key: You need to obtain a YouTube Data API v3 key. Replace the DEVELOPER_KEY variable with your own API key. Instructions on obtaining an API key can be found in the YouTube API documentation.

Discord bot token: You need to create a Discord bot and obtain its token. Replace the key variable with your Discord bot token. Instructions on creating a Discord bot and getting its token can be found in the Discord.py documentation.

Installed dependencies: Make sure you have the necessary dependencies installed. You can install them using pip:
```
pip install google-api-python-client 
pip install discord.py
```
## Options
The options aren't really options, they just contain the keys/channels you want. 
The code supports multiple channels at once.
