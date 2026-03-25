# Minesweeper

A classic **Minesweeper** game implemented in Python with a graphical interface.  
Inspired by the original logic puzzle game. ([Wikipedia](https://en.wikipedia.org/wiki/Minesweeper_(video_game)))

This project recreates the **Minesweeper** experience: a grid of hidden cells, some containing mines.  
The goal is to reveal all safe cells without triggering any mines, using the numerical hints revealed after each click.

## Features

- Randomly generated grid  
- Graphical interface using *CustomTkinter*  
- Multiple difficulties
- Cross-platform: Windows, macOS & Linux (Python required)
- Score system

## Installation (Windows only)

Download the latest release from the [releases](https://github.com/nicolas-riera/minesweeper/releases/latest) and extract the .zip file.

Then, launch ```Minesweeper.exe```.

## Controls

- Left mouse click:
    - Press on buttons
    - Dig a cell
- Right mouse click:
    - Place a flag
    - A second right click will place a question mark
    - A third one will reset the cell back to empty

## Run and Build from source

### Requirements
- Python **3.10+**
- PyInstaller -> ```python -m pip install pyinstaller```
- CustomTkinter -> ```python -m pip install customtkinter```

### Run

From the root folder, run :

```bash
python main.py
```

### Build

To build the game (in .exe for Windows, in .app on MacOs, and as a binary file on Linux), you need first to get the location of customtkiner:

```bash
pip show customtkinter
```

Then, copy the location and paste it in this pyinstaller command :

```bash
pyinstaller --onedir main.py --add-data "{path_to_customtkinter}/customtkinter;customtkinter/" --noconsole --name Minesweeper
```
## Authors

This project has been realised by [Nicolas](https://github.com/nicolas-riera), [Hugo](https://github.com/hugo-belaloui) and [Yaniss](https://github.com/yanissaouri)
