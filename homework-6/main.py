from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.title is None
    assert broken_video.like_count is None
