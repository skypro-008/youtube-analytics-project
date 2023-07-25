import json
import os

from googleapiclient.discovery import build

from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'



    #print(video1.video_data)
    # print(video2.video_title)
    # print(video2.view_count)
    # print(video2.like_count)
    # print(video2.comment_count)
    # print(video2.video_data)
    print(video2.fetch_playlist_data())
