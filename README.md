# Digi Clock

A fullscreen cyberpunk-inspired digital clock built with Python and Tkinter.

## Features

* Fullscreen display
* Live clock updates every second
* Smooth fade animation
* Random clock movement to prevent screen burn-in
* ASCII art background
* ESC key to exit
* Lightweight and standalone executable

## Screenshot

(Add a screenshot here)

## Requirements

* Python 3.10+
* Tkinter (included with Python)

## Running from Source

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/digi-clock.git
cd digi-clock
```

Run:

```bash
python digi_clock.py
```

## Building the Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build:

```bash
pyinstaller --onefile --windowed digi_clock.py
```

The executable will be generated in:

```text
dist/digi_clock.exe
```

## Controls

| Key | Action           |
| --- | ---------------- |
| ESC | Exit application |

## Project Structure

```text
digi-clock/
├── digi_clock.py
├── README.md
├── .gitignore
```

## Future Improvements

* Multiple themes
* Better fade transitions
* Matrix-style background
* Weather integration
* Multi-monitor support

## License

MIT License
