"""
NongManager

Handles nongs (not on newgrounds songs)
in GeometryDash
Supports MacOS, Linux, and Windows
"""
import libui
import os
import setup


if __name__ == "__main__":
    if not os.path.exists(os.path.join(os.getcwd(), "APPDATA.txt")):
        app = setup.Setup()
        app.mainloop()
    else:
        app = libui.App()
        app.mainloop()
