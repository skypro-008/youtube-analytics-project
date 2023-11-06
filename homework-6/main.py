from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.name_video is None
    assert broken_video.like_video is None

    print(broken_video.name_video)
    print(broken_video.like_video)