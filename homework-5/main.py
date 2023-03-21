import datetime

from src.playlist import PlayList

if __name__ == '__main__':
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    assert pl.title == "Редакция. АнтиТревел"
    assert pl.url == "https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb"

    duration = pl.total_duration
    assert str(duration) == "3:41:01"
    assert issubclass(duration, datetime.timedelta)
    assert duration.total_seconds() == 13261.0

    assert pl.show_best_video() == "https://youtu.be/9Bv2zltQKQA"
