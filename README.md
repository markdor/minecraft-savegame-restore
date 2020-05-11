# Minecraft Savegame Restore

Restores a savegame from a backuped world in Minecraft.

## Prerequisites

The GUI is created with [appJar](http://appjar.info/), you need to install it:

```
pip install appjar
```

## Compile To Executable

Use `pyinstaller` to create a single executable file:

```sh
pip install pyinstaller
pyinstaller --add-data "creeper.ico;." -i "creeper.ico" -F -w restore.py -n "Minecraft Savegame Restore"
```