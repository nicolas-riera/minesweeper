# Minesweeper

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

