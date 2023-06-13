import customtkinter
import os

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

if os.name == 'nt':
    appdata_folder = os.getenv("LOCALAPPDATA") + "\\GeometryDash"
elif os.name == 'posix':
    appdata_folder = "Your Geometry Dash AppData folder"
else:
    appdata_folder = "This is a bug. Please report it as an issue on Github."


class Setup(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("NongManager Setup")
        self.geometry(f"{500}x{300}")
        self.resizable(False, False)

        self.desc = customtkinter.CTkLabel(self, text="NongManager Setup:")
        self.info = customtkinter.CTkLabel(self, text="Setup will now setup to the current directory.\n If this is not the directory you would like to setup in,\n please close the program and rerun the executable\n in directory you would like")
        self.label = customtkinter.CTkLabel(self, text="Please enter your Geometry Dash AppData folder.\nIf you are on windows, you should not have to change this.")
        self.appdata = customtkinter.CTkEntry(self, textvariable=customtkinter.StringVar(value=appdata_folder), width=350)
        self.submit = customtkinter.CTkButton(self, text="Setup", width=350, command=self.setup)

        self.desc.pack(pady=(10,10))
        self.info.pack()
        self.label.pack(pady=(10,10))
        self.appdata.pack(pady=(5,5))
        self.submit.pack()

    def setup(self):
        with open(os.path.join(os.getcwd(), "APPDATA.txt"), "w") as f:
            f.write(self.appdata.get())
        self.destroy()


if __name__ == '__main__':
    setup = Setup()
    setup.mainloop()
