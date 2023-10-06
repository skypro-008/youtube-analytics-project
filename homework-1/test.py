import os


#os.putenv('YT_API_KEY','AIzaSyDoXfDhCmEBqP323Mfo599sILGCvB9-Gb4')
api_key: str = os.getenv('YT_API_KEY')
print(api_key)
#api_key = 'AIzaSyDoXfDhCmEBqP323Mfo599sILGCvB9-Gb4'
"""
youtube = build("youtube", "v3", developerKey=api_key)

video_id = "dQw4w9WgXcQ"
request = youtube.videos().list(part="snippet,contentDetails", id=video_id)
response = request.execute()

print(response)"""
