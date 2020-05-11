import sys
from appJar import gui

# get path for resources
if getattr(sys, 'frozen', False):
    # pylint: disable=no-member
    running_dir = sys._MEIPASS + "/"
else:
    running_dir = "./"

# create a GUI variable called app
app = gui()
app.setSize("600x400")
app.setIcon(running_dir + "creeper.ico")
app.setTitle("Minecraft Savegame Restore")
app.addLabel("title", "asd")

# start the GUI
app.go()