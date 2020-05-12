import sys
import glob
import os
from appJar import gui

# get path for resources
if getattr(sys, 'frozen', False):
    # pylint: disable=no-member
    running_dir = sys._MEIPASS + "/"
else:
    running_dir = "./"

# get latest backup
minecraft_backup_dir = os.path.expandvars(r'%APPDATA%\.minecraft\backups\*')
files = glob.glob(minecraft_backup_dir)
minecraft_backup_filepath = max(files, key=os.path.getctime)
minecraft_backup_filename = os.path.basename(minecraft_backup_filepath)

# create a GUI variable called app
app = gui("Minecraft Savegame Restore", "400x200")
app.setIcon(running_dir + "creeper.ico")
app.addLabelEntry("Backup-File")
app.setEntry("Backup-File", minecraft_backup_filename)
app.getLabelWidget("Backup-File")

# start the GUI
app.go()