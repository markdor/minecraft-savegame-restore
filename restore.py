# import the library
from appJar import gui
# create a GUI variable called app
app = gui()
app.setIcon("creeper.ico")
app.setTitle("Minecraft Savegame Restore")
app.addLabel("title", "asd")

# start the GUI
app.go()