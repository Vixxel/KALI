````markdown
# KALI DEMO

A simple Python project demonstrating multimedia programming with Python.

## Features

- 🖼️ Opens multiple independent image windows using Tkinter.
- 🔊 Plays multiple overlapping instances of an audio clip.
- 📁 Replaces PNG files located only inside the project's own `gallery` folder.
- 📦 Compatible with PyInstaller for building a standalone executable.

## Project Structure

```text
KALI/
│
├── main.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── image.png
│   └── sound.mp3
│
└── gallery/
    ├── image1.png
    ├── image2.png
    ├── image3.png
    └── image4.png
```

## Requirements

- Python 3.10+
- Pillow
- pygame

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running

```bash
python main.py
```

## Building an Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build:

```bash
python -m PyInstaller ^
--onefile ^
--windowed ^
--add-data "assets;assets" ^
--add-data "gallery;gallery" ^
main.py
```

The executable will be created in:

```text
dist/main.exe
```

## Included Assets

### assets/

Contains the multimedia resources used by the applicastion.

- `image.png`
- `sound.mp3`

### gallery/

Contains demonstration PNG files that are replaced with the bundled `image.png` when the program runs. The application only modifies files inside this folder.

## Libraries Used

- Pillow
- pygame
- tkinter (included with Python)

## License

Released under the MIT License.
````
