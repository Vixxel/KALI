# KALI

A lightweight Python multimedia demonstration project showcasing image rendering, audio playback, threading, file manipulation, and executable packaging.

---

## ✨ Features

- 🖼️ Displays multiple independent image windows.
- 🔊 Plays multiple overlapping audio instances.
- 📁 Demonstrates controlled file manipulation within the project's own directory.
- ⚡ Multi-threaded image and audio execution.
- 📦 Ready for packaging with PyInstaller.
- 🪟 Native Windows desktop application.

---

## 📂 Project Structure

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

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Vixxel/KALI.git
cd KALI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

## 🛠️ Build Executable

Install PyInstaller

```bash
pip install pyinstaller
```

Compile

```bash
python -m PyInstaller --onefile --windowed ^
--add-data "assets;assets" ^
--add-data "gallery;gallery" ^
main.py
```

The executable will be generated inside:

```text
dist/
```

---

## 📦 Requirements

- Python 3.10+
- Pillow
- pygame
- tkinter (included with Python)

---

## 📚 Technologies Used

- Python
- Pillow
- pygame
- tkinter
- PyInstaller
- Threading
- File Management

---

## 🎯 Project Goals

This project was created to practice and demonstrate:

- Desktop application development
- Multimedia programming
- Asset management
- Multi-threading
- File system operations
- Executable distribution

---

## 📌 Notes

This project is intended as an educational demonstration of multimedia programming in Python.

The application operates only on resources contained within its own project directory and does not interact with arbitrary files elsewhere on the system.

---

## 📈 Future Improvements

- Theme support
- Configuration file
- GIF animation support
- Custom executable icon
- Additional multimedia effects
- Cross-platform improvements

---

## 📄 License

This project is licensed under the MIT License.

Feel free to fork, modify, and experiment with the project.
