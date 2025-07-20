# 🎛️ Retro Game Console (Raspberry Pi 5)

🕹️ A retro-inspired Python-based game launcher designed to run on Raspberry Pi 5, capable of launching emulated games and displaying a stylish menu interface. Built with Pygame, this project delivers an authentic arcade feel with keyboard navigation, game preview images, and direct launching support for ROMs and emulators.

## 📦 Features

- 🎮 Pygame-powered game launcher UI with controller/keyboard navigation
- 🗂️ Scans and lists ROMs from a designated directory
- 🖼️ Displays custom thumbnails for each game
- 🚀 Launch games via command-line emulators (e.g., RetroArch, MAME, etc.)
- 🧠 Save your favorites for quick access
- ⚙️ Configurable via a JSON file

## 🧰 Requirements

- Python 3.7+
- Pygame
- Raspberry Pi OS
- Pre-installed emulators (e.g., RetroArch, MAME)

Install dependencies:

```bash
pip install pygame
```

## 🗂️ Directory Structure

```
retro-game-console/
├── main.py               # Main launcher script
├── config.json           # Configuration file for ROM path and emulator command
├── assets/
│   ├── background.png    # UI background
│   ├── fonts/            # Custom fonts
│   └── thumbs/           # Game thumbnails
├── roms/                 # Your game ROMs
└── README.md             # This file
```

## ⚙️ Configuration

Create a `config.json` file:

```json
{
  "rom_path": "./roms",
  "emulator_command": "retroarch -L /path/to/core.so {rom}"
}
```

## 🚀 Usage

```bash
python3 main.py
```

Navigate with arrow keys or a gamepad. Press Enter to launch a selected game.

## 🧠 Tips

- Ensure your ROMs are compatible with the specified emulator.
- Update thumbnails by placing `.png` files in the `assets/thumbs/` directory with the same base name as the ROM.

## 🤖 Future Improvements

- Gamepad configuration UI
- Multiple emulator profiles
- Background music
- Save states and metadata display

## 📷 Screenshots

*Add your launcher screenshots here!*

## 🧑‍💻 Author

Crafted with ❤️ for retro game lovers using Raspberry Pi 5.
