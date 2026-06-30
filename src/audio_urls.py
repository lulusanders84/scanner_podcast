import json
import pathlib

from src.walk import walk


def get(files_list):
	urls = []

	for file in files_list:
		urls.append(file["url"])

	return urls

def save_url(url: str, file_path: pathlib.Path):
	with open(file_path, "a") as f:
		f.write(url + "\n")


def save(audio_urls: list[str], file_path):
	for url in audio_urls:
		save_url(url, file_path)
