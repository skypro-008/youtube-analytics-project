import datetime
import sys
from pathlib import Path


# Добавьте корневую директорию проекта в путь Python
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.playlist import PlayList

if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0
    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
