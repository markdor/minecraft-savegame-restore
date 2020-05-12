import sys
import glob
import os
import tempfile
import shutil
import zipfile
from appJar import gui

def log(message):
    app.setLabel("logger", app.getLabel("logger") + "\n" + message)

def press(button):
    if button == "Exit":
        app.stop()
    else:
        restore()

def restore():
    temp_dirpath = tempfile.mkdtemp()
    log("temporary dir: "+ temp_dirpath)
    log("unzipping " + minecraft_backup_filename)
    with zipfile.ZipFile(minecraft_backup_filepath, 'r') as zip_ref:
        zip_ref.extractall(temp_dirpath)
    temp_savedir_path = max(glob.glob(temp_dirpath + r'\*'), key=os.path.getctime)
    temp_savedir = os.path.basename(temp_savedir_path)    
    target_savedir_path = minecraft_save_dir + '\\' + temp_savedir
    if(os.path.isdir(target_savedir_path)):
        log("deleting savegame '" + temp_savedir + "'")
        shutil.rmtree(target_savedir_path)
    log("copying savegame")
    shutil.copytree(temp_savedir_path, target_savedir_path)
    log("deleting temporary dir")
    shutil.rmtree(temp_dirpath)
    log("done")

# get path for resources
if getattr(sys, 'frozen', False):
    # pylint: disable=no-member
    running_dir = sys._MEIPASS + "/"
else:
    running_dir = "./"

minecraft_backup_dir = os.path.expandvars(r'%APPDATA%\.minecraft\backups')
minecraft_save_dir = os.path.expandvars(r'%APPDATA%\.minecraft\saves')

# get latest backup
minecraft_backup_filepath = max(glob.glob(minecraft_backup_dir + r'\*'), key=os.path.getctime)
minecraft_backup_filename = os.path.basename(minecraft_backup_filepath)

# create a GUI variable called app
app = gui("Minecraft Savegame Restore", "600x250")
app.setResizable(canResize=False)
app.setIcon(running_dir + "creeper.ico")

app.addLabelEntry("Backup-File")
app.setEntry("Backup-File", minecraft_backup_filename)
app.setEntryState("Backup-File", "disabled")

app.addButtons(["Ok", "Exit"], press)

app.addLabel("logger", "starting up")
app.getLabelWidget("logger").config(font="Courier 10")
app.setLabelRelief("logger", "sunken")
app.setLabelHeight("logger", 10)
app.setLabelWidth("logger", 60)
app.setLabelAnchor("logger", "sw")

# start the GUI
app.go()