import pathlib

from src.audio_urls import get, save
from src.walk import walk

PREFIX = "2026/06-30-26/05/Police Dispatch/"
URL_LISTS_FILE_NAME = PREFIX.rstrip("/").replace("/", "-").replace(" ", "_")
DIR_NAME = "../data/url_lists"
FILE_TYPE = "csv"

def get_path(file_name, dir_name=DIR_NAME, file_type=FILE_TYPE):
    dir_path = create_dir_path(dir_name)
    return create_file_path(dir_path, file_name, file_type)


def create_dir_path(dir_name: str):
    dir_path = pathlib.Path(dir_name)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def create_file_path(dir_path, file_name, file_type):
    file_path = pathlib.Path(dir_path / f"{file_name}.{file_type}")
    if not file_path.exists():
        file_path.touch()
        print(f"{file_path.name} created successfully.")
    else:
        print(f"{file_path.name} already exists.")
    return file_path





def get_url_list_filename(prefix):
    return prefix.rstrip("/").replace("/", "-").replace(" ", "_")


def retrieve(prefix):
    filename = get_url_list_filename(prefix)
    with open(get_path(filename), 'r') as f:
        return f.read().strip('\n').split('\n')


def create(prefix):
    url_file_path = get_path(get_url_list_filename(prefix))
    files_list = []
    for file in walk(prefix):
        files_list.append(file)
    audio_urls = get(files_list)
    save(audio_urls, url_file_path)