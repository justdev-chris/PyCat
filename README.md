# 🐱 PyCat - A Cat-Themed Programming Language

> *"Meow means print, CatGets means =, and everything is cats!"*

PyCat is a fun, cat-themed programming language that compiles to Python. Write code with cat-themed keywords and watch it run! :3

## 🚀 Quick Start

### Run a PyCat program:
```
pycat hello.pycat
```

### Example `hello.pycat`:
```
Meow("Hello from PyCat! 🐱")
name CatGets Beg("What's your cat's name? ")
Purr("Hello, " CatSpeak(name) "!")
```

## 📖 Language Guide

### Basic Syntax:
```
# Variables
x CatGets 5
name CatGets "Whiskers"

# Output
Meow("Hello")        # Print
Purr("Happy!")       # 😺 Print
Hiss("Warning!")     # 😾 Print

# Input
age CatGets ToCatYears(Beg("Age? "))

# Conditionals
IfHungry x > 3:
    Meow("Big number!")
Otherwise:
    Meow("Small number!")

# Loops
ForPrey i InLitterbox CatRange(5):
    Meow(i)

# Functions
Defur feed_cat(treats):
    Fetch treats * 2

# Math
result CatGets 10 PlusCat 5
result CatGets x TimesCat y
```

### All Keywords:

| PyCat | Python | Description |
|-------|--------|-------------|
| `Meow` | `print` | Output text |
| `Beg` | `input` | Get input |
| `CatGets` | `=` | Assignment |
| `IfHungry` | `if` | Condition |
| `Otherwise` | `else` | Else clause |
| `ForPrey` | `for` | Loop |
| `Defur` | `def` | Function |
| `Fetch` | `return` | Return value |
| `PlusCat` | `+` | Addition |
| `SameAs` | `==` | Equality |
| ...and 100+ more! | | |

## 🛠️ Installation

### Method 1: Download Executable
# Windows 
1. Download `PyCat-WIndows.zip` from [Releases](https://github.com/justdev-chris/PyCat/releases)
2. Run: `SETUP.bat`

# If your on Linux/MacOS,
  ``
 curl -L -o pycat https://github.com/justdev-chris/pycat/releases/latest/download/pycat-macos
``or /pycat-linux `` 
chmod +x pycat
`` ``
./pycat --help
`` 
- Or install globally
`` 
sudo mv pycat /usr/local/bin/
`` ``
pycat --help
``
### Method 2: Build from Source
```
git clone https://github.com/justdev-chris/pycat.git
cd pycat
pip install pyinstaller
pyinstaller pycat.spec
# Output: dist/pycat.exe
```

## 📁 Project Structure
```
pycat/
├── src/
│   ├── main.py          # Entry point
│   ├── keywords.py      # ALL translations
│   └── __init__.py
├── pycat_entry.py       # PyInstaller entry
├── pycat.spec          # Build configuration
└── examples/
    ├── hello.pycat
    ├── calculator.pycat
    └── game.pycat
```

## 🎮 Examples

Check the `examples/` folder:
- `hello.pycat` - Basic Hello World
- `calculator.pycat` - Math operations
- `game.pycat` - Guess the number game
- `demo.pycat` - Showcase of all features

## 🤔 Why PyCat?

Because programming should be:
- **Fun** - Cat-themed syntax!
- **Educational** - Learn concepts through cats
- **Simple** - Readable like English
- **Powerful** - Full Python compatibility

## 🐾 Contributing

Found a bug? Want more cat words?
1. Fork the repo
2. Add your feature
3. Submit a pull request!

## 📄 License

MIT License - do whatever you want with cats!

## 👤 Author

**justdev-chris**
- GitHub: [@justdev-chris](https://github.com/justdev-chris)
- Website: [catsdevs.online](https://catsdevs.online)

---

*Made with many 😸 and too much catnip*
