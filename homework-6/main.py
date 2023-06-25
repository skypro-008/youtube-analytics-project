from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.title_video is None
    assert broken_video.likes_count_video is None
