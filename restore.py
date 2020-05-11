import sys
from appJar import gui

# get path for resources
if getattr(sys, 'frozen', False): # Running as compiled
    running_dir = sys._MEIPASS + "/" # Same path name than pyinstaller option
else:
    running_dir = "./" # Path name when run with Python interpreter

# create a GUI variable called app
app = gui()
app.setIcon(running_dir + "creeper.ico")
app.setTitle("Minecraft Savegame Restore")
app.addLabel("title", "asd")

# start the GUI
app.go()