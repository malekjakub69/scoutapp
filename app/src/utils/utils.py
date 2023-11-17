import os


def get_absolute_path(*args: str) -> str:
    return os.path.abspath(os.path.join(*args))
