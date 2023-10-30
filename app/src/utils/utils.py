import datetime
import os


def get_absolute_path(*args: str) -> str:
    return os.path.abspath(os.path.join(*args))


def parse_date(date_string: str, fmt: str) -> datetime.date:
    try:
        date = datetime.datetime.strptime(date_string, fmt).date()
    except ValueError:
        date = datetime.date.today()
    return date


def parse_time(time_string: str, fmt: str) -> datetime.datetime:
    return datetime.datetime.strptime(time_string, fmt)


def get_latest_filename(path: str, name_pattern: str) -> str:
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files if name_pattern in basename]
    return max(paths, key=os.path.getctime)
