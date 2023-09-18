import os

from libbases import FileManager
import newgroundsdl
import pytube
import requests


class NoNGInstaller(FileManager):
    def __init__(self, appdata_path):
        super().__init__(appdata_path)
        # load config vars and stuff

    def install_newgrounds(self, id_):
        try:
            uri = newgroundsdl.getSongFileURI(f"https://www.newgrounds.com/audio/listen/{id_}")
            data = requests.get(uri)
            installed = self.install_nong(data, id_)

            if installed is False:
                return False
            return True  # Installed successfully

        except Exception as error:
            print(error)
            return False  # Something went wrong

    def install_songfilehub(self, id_):
        try:
            uri = f"https://songfilehub.com/api/v1/nongs?id={id_}"
            data = requests.get(uri)
            self.install_nong(data, id_)

            return True  # Installed successfully

        except Exception as error:
            print(error)
            return False  # Something when wrong

    def install_remote_uri(self, id_, remote_uri):
        try:
            uri = remote_uri
            data = requests.get(uri)
            installed = self.install_nong(data, id_)

            if installed is False:
                return False
            return True  # Installed successfully

        except Exception as error:
            print(error)
            return False  # Something went wrong

    def install_youtube_url(self, id_, url):
        out = os.path.join(self.appdata_path, id_)
        old = os.path.join(self.appdata_path, f"{id_}_old.mp3")
        
        try:
            if self.settings.has_option(id_):
                return False  # Exists
            video = pytube.YouTube(url)
            audio_streams = video.streams.filter(only_audio=True)
            best_stream = None
            for stream in audio_streams:
                if best_stream is not None:
                    if int(stream.abr[:-4]) > int(best_stream.abr[:-4]):
                        best_stream = stream
                else:
                    best_stream = stream

            try:
                os.rename(out, old)
            except FileNotFoundError:  # Original song mp3 does not exist, lets download it
                uri = newgroundsdl.getSongFileURI(f"https://www.newgrounds.com/audio/listen/{id_}")
                data = requests.get(uri)
                
                with open(out, "wb") as f:
                    f.write(data)

                os.rename(out, old)

            best_stream.download(output_path=os.path.join(self.appdata_path, id_))
            self.settings.set(id_, "1")  # 1=NoNG is in use, 0=NoNG is not active

        except Exception as error:
            print(error)
            return False  # Something went wrong

    def install_local_file(self, id_, path):
        try:
            with open(path, "rb") as f:
                data = f.read()

            self.install_nong(data, id_)

        except Exception as error:
            print(error)
            return False  # Something went wrong
