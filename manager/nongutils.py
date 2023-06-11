"""
Get song off newgrounds from link, download to selected location
"""
from pytube import YouTube
import os
import requests


def download_song(platform, output_folder, n_id, url):
    """
    :param platform: youtube, url
    :param output_folder: location to save to
    :param n_id: newgrounds song id to replace
    :param url: url to download from
    :return:
    """
    if platform == "youtube":
        video = YouTube(url)
        audio = video.streams.filter(only_audio=True).first()
    elif platform == "link":
        audio = requests.get(url, allow_redirects=True)
    else:
        return False

    with open(os.path.join(output_folder, f"{n_id}.mp3"), "wb") as f:
        f.write(audio)

    return True
