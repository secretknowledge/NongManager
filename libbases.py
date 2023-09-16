from easysettings import EasySettings
import os


def get_appdata():
    with open(os.path.join(os.getcwd(), "APPDATA.txt")) as f:
        return f.read()


class FileManager:
    """
    Manages creating, deleting, and modifying files within
    the NongManager application
    """

    def __init__(self, appdata_path):
        self.appdata_path = appdata_path
        self.settings = EasySettings(os.path.join(self.appdata_path, "NONGMANAGER.conf"))

    def install_nong(self, data, id_):
        out = os.path.join(self.appdata_path, id_)
        old = os.path.join(self.appdata_path, f"{id_}_old.mp3")
        if not os.path.exists(old):
            self.settings.set(id_, "1")  # 1=NoNG is in use, 0=NoNG is not active
            self.settings.save()

            os.rename(out, old)

            with open(out, "wb") as f:
                f.write(data)

            return True  # Installed successfully

        else:
            return False  # Exists

    def toggle_nong(self, id_):
        out = os.path.join(self.appdata_path, id_)
        old = os.path.join(self.appdata_path, f"{id_}_old.mp3")

        self.settings.set(0 if self.settings.get(id_) == 1 else 1)

        with open(out, "rb") as f:
            swap = f.read()

        os.remove(out)
        os.rename(old, out)

        with open(old, "wb") as f:
            f.write(swap)
