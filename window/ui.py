import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self, download_function):
        super().__init__()

        self.title("NongManager:")
        self.geometry("500x700")
        self.resizable(False, False)
        self.download_function = download_function

        self.youtube_link_var = ctk.IntVar()

        self.window_title = ctk.CTkLabel(self, text="NongManager")
        self.url_label = ctk.CTkLabel(self, text="URL")
        self.url_entry = ctk.CTkEntry(self, textvariable=ctk.StringVar(value="https://example.com/nong.mp3"), width=350)
        self.id_label = ctk.CTkLabel(self, text="NG ID")
        self.id_entry = ctk.CTkEntry(self, textvariable=ctk.StringVar(value="123456"), width=350)
        self.download_location_label = ctk.CTkLabel(self, text="GD AppData")
        self.download_location_entry = ctk.CTkEntry(self, textvariable=ctk.StringVar(value="%AppData%/Local/GeometryDash"), width=350)
        self.youtube_link = ctk.CTkCheckBox(self, text="Youtube Link", variable=self.youtube_link_var)
        self.inject_button = ctk.CTkButton(self, text="Inject", command=lambda: download_function(("youtube" if self.youtube_link_var.get() == 1 else "link"), self.download_location_entry.get(), self.id_entry.get(), self.url_entry.get()))

        self.window_title.pack(pady=(50,100))
        self.url_label.pack(pady=(0,15))
        self.url_entry.pack(pady=(0,25))
        self.id_label.pack(pady=(0,15))
        self.id_entry.pack(pady=(0,25))
        self.download_location_label.pack(pady=(0,15))
        self.download_location_entry.pack(pady=(0,50))
        self.youtube_link.pack(pady=(0,50))
        self.inject_button.pack()
