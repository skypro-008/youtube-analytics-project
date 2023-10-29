import datetime

from src.playlist import PlayList

if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    print(pl.video_ids)
    assert pl.title == "Moscow Python Meetup №81. Вступление."
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration
    print(str(duration))
    #assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    print(duration.total_seconds())# == 6592.0
    # assert duration.total_seconds() == 6592.0

    # assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
    print(pl.show_best_video)
