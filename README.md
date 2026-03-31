# Joel's Calculator

A simple calculator application built with Python and Tkinter.

## Overview

This project creates a basic desktop calculator with a graphical user interface. It allows users to enter numbers and perform simple arithmetic operations through clickable buttons.

## Features

- Numeric buttons from `0` to `9`
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`x`)
- Modulus (`%`)
- Clear button (`AC`)
- Equals button (`=`)
- Tkinter-based GUI

## Requirements

- Python 3.x
- Tkinter

Tkinter is included with most standard Python installations.

## How To Run

1. Save your calculator code in a file named `calculator.py`.
2. Open a terminal in this project folder.
3. Run:

```bash
python calculator.py
```

## Project Structure

`calculator.py` contains:

- the Tkinter window setup
- the display entry widget
- button definitions
- input handling logic
- expression evaluation logic

## Notes

- The calculator currently uses Python's `eval()` to calculate results.
- `eval()` works for simple projects, but it is not a safe choice for untrusted input.
- The multiplication button displays `x`, but internally uses `*` for calculation.

