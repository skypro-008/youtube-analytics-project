import os
import datetime

import isodate as isodate
from googleapiclient.discovery import build
class PlayList:
   def __init__(self,playlist_id):
       self.playlist_id = playlist_id
       self.url = "https://www.youtube.com/playlist?list="+playlist_id
       self.title= self.playlist_title()

   def youtube_api_key(self):
       api_key: str = os.getenv('YouTube_API')
       youtube = build('youtube', 'v3', developerKey=api_key)
       return youtube

   def playlist(self): #best video
       playlist_id = self.playlist_id
       playlist_videos =self.youtube_api_key().playlistItems().list(playlistId=playlist_id,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()
       video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
       return video_ids

   def playlist_title(self):
       video_id = self.playlist()[0]
       video_response = self.youtube_api_key().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=video_id
                                                             ).execute()
       video_title = video_response['items'][0]['snippet']['title']
       return video_title.partition('.')[0]




   def show_best_video(self):#best video
       max_number = []
       mx_num = 0
       for i in range(len(self.playlist())):
           video_id = self.playlist()[i]
           video_response = self.youtube_api_key().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                  id=video_id
                                                  ).execute()
           like_count = video_response['items'][0]['statistics']['likeCount']

           max_number.append(like_count)
           mx_num = max(max_number)

       if like_count == mx_num:
           return "https://youtu.be/"+video_id

   @property
   def total_duration(self):
       time_mas = []
       video_response = self.youtube_api_key().videos().list(part='contentDetails,statistics',
                                              id=','.join(self.playlist())
                                              ).execute()
       # printj(video_response)

       for video in video_response['items']:
           # YouTube video duration is in ISO 8601 format
           iso_8601_duration = video['contentDetails']['duration']
           duration = isodate.parse_duration(iso_8601_duration)
           time_mas.append(str(duration))
       mysum = datetime.timedelta()
       for i in time_mas:
           (h, m, s) = i.split(':')
           d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
           mysum += d
       return mysum
