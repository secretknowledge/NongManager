"""
NongManager

Handles nongs (not on newgrounds songs)
in GeometryDash
Supports MacOS, Linux, and Windows
"""
import manager.nongutils as nongutils
import window.ui as ui

if __name__ == "__main__":
    app = ui.App(nongutils.download_song)
    app.mainloop()
