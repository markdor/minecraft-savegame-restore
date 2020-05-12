import sys
import glob
import os
from appJar import gui

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        restore()

def restore():
    app.setMessage("logger", app.getMessage("logger") + "\nhuhu")

# get path for resources
if getattr(sys, 'frozen', False):
    # pylint: disable=no-member
    running_dir = sys._MEIPASS + "/"
else:
    running_dir = "./"

# get latest backup
minecraft_backup_dir = os.path.expandvars(r'%APPDATA%\.minecraft\backups\*')
minecraft_save_dir = os.path.expandvars(r'%APPDATA%\.minecraft\saves')
minecraft_backup_filepath = max(glob.glob(minecraft_backup_dir), key=os.path.getctime)
minecraft_backup_filename = os.path.basename(minecraft_backup_filepath)

# create a GUI variable called app
app = gui("Minecraft Savegame Restore", "600x100")
app.setIcon(running_dir + "creeper.ico")

app.addLabelEntry("Backup-File")
app.setEntry("Backup-File", minecraft_backup_filename)
app.setEntryState("Backup-File", "disabled")

app.addButtons(["Ok", "Cancel"], press)

app.addMessage("logger", "starting up")
app.setMessageWidth("logger", 600)

# start the GUI
app.go()