import customtkinter
from easysettings import EasySettings
import os

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


def get_appdata():
    with open(os.path.join(os.getcwd(), "APPDATA.txt")) as f:
        return f.read()


settings = EasySettings(os.path.join(get_appdata(), "NONGMANAGER.conf"))


class InstallMenu(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.desc = customtkinter.CTkLabel(self, text="Add NoNG from...", width=200)
        self.separator = customtkinter.CTkLabel(self, text="_______________________")

        self.newgrounds_button = customtkinter.CTkButton(self, text="Newgrounds")
        self.songfilehub_button = customtkinter.CTkButton(self, text="SongFileHub")
        self.remote_url_button = customtkinter.CTkButton(self, text="Remote URL")
        self.youtube_url_button = customtkinter.CTkButton(self, text="Youtube URL")
        self.local_file_button = customtkinter.CTkButton(self, text="Local File")

        self.desc.pack(pady=(25,0))
        self.separator.pack(pady=(5,40))

        self.newgrounds_button.pack(pady=(10,20))
        self.songfilehub_button.pack(pady=(10,20))
        self.remote_url_button.pack(pady=(10,20))
        self.youtube_url_button.pack(pady=(10,20))
        self.local_file_button.pack(pady=(10,0))


class NoNGMenu(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{800}x{500}")
        self.resizable(False, False)
        self.title("NongManager")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.install_menu = InstallMenu(self)
        self.nongmenu = NoNGMenu(self)

        self.install_menu.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.nongmenu.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == '__main__':
    app = App()
    app.mainloop()