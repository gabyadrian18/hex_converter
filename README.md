
# HEX Converter CLI 🔥

---

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7+-blue?logo=python">
  <img src="https://img.shields.io/badge/CLI-Easy--to--use-green">
  <img src="https://img.shields.io/badge/tests-passing-brightgreen">
  <img src="https://img.shields.io/badge/license-MIT-yellow">
</p>

---

## ✨ About

**HEX Converter CLI** is a blazing fast and flexible command-line tool for decoding and visualizing hex strings in all the formats you ever wanted:  
**Unsigned/Signed/Float (8/16/32 bit), ASCII, and all major endianness (Big, Little, Mid)!**

> 🪄 Convert like a PRO. Get instant insight into what your hex bytes *actually mean*.

---

## 🚀 Features

- ⚡ **Instant hex interpretation** (decimal, float, ASCII)
- 🔄 **Supports Big, Little, and Mid-endian**
- 🖨️ **Pretty terminal output (aligned columns)**
- 🔎 **8/16/32-bit, ASCII, float32** — all in one shot!
- 🧪 **Includes unit tests**
- 🦾 **Clean Python code, modular & extendable**

---

## 📸 Demo

```bash
$ python cli.py 2A3F42B9

Type                  Big (ABCD)        Mid-Little (CDAB)      Little (DCBA)         
------------------------------------------------------------------------------------
Unsigned 8-bit        185               -                      42                    
Signed 8-bit          -71               -                      42                    
Unsigned 16-bit       17081             -                      10815                 
Signed 16-bit         17081             -                      10815                 
Unsigned 32-bit       708788921         1119431231             708788921             
Signed 32-bit         708788921         1119431231             708788921             
Float 32-bit          1.6987356888e-13  92.5825119019          1.6987356888e-13      
ASCII                 *?B.              B.*?                   .B?*                  
Hex                   2A3F42B9          42B92A3F               B9423F2A              
```

---

## 🏁 Quickstart

1. **Clone the repo**

    ```bash
    git clone https://github.com/yourusername/hex_converter.git
    cd hex_converter
    ```

2. **Run with Python**  
   (Python 3.7 or newer)

    ```bash
    python cli.py 48656C6C6F
    ```

    Or simply run and input hex interactively:

    ```bash
    python cli.py
    # Paste your hex string!
    ```

---

## 📦 Installation (optional, as package)

If you want to use it as a Python module:

```bash
pip install .
```

Then in Python:

```python
from hex_converter.converter import get_conversions
conversions = get_conversions('2A3F42B9')
print(conversions)
```

---

## 🧩 Project Structure

```
hex_converter/
├── cli.py              # CLI entry point
├── hex_converter/
│   ├── converter.py    # Core conversion logic
│   ├── utils.py        # Pretty print & helpers
│   └── __init__.py
├── tests/
│   └── test_converter.py
├── README.md
└── .gitignore
```

---

## 🛠️ Development & Testing

- To run the tests:
    ```bash
    python tests/test_converter.py
    ```

---

## ❓ FAQ

- **Q: Does it handle odd-length hex strings?**  
  A: Yes! It automatically pads them for you.

- **Q: What is “Mid-Little Endian”?**  
  A: It’s a fun mode (e.g., CDAB for 4 bytes) used in some PLC/Modbus systems.

- **Q: What if I enter a weird or short hex?**  
  A: It does its best to show all formats that fit.

- **Q: Can I import the logic into my own script?**  
  A: Yes! See [Installation](#installation-optional-as-package).

---

## 🤝 Contributing

1. Fork this repo 🍴  
2. Make your changes 🚀  
3. Submit a pull request ✨

All contributions, issues and feature requests are welcome!

---

## ⚖️ License

MIT License © [yourusername]

---

## 🙏 Credits

Made with ❤️ by Gabi (and ChatGPT for README style).  
Hex string conversions inspired by real-life debugging sessions.

---

## ⭐ If you like it, star the repo!

---
