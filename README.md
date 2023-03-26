# Colorize
A small Colorama wrapper that improves syntax

## Prerequisites:
For the module to work, you'll need to have **colorama** installed on your machine:
```
pip install colorama
```

## How to import the module:
Place **colorize.py** in your root project folder and then use the following statement to import it:
```py
from colorize import colorize
```
## How to use:
### Basic syntax:
```py
colorize(string, color)
```
Available colors:
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- reset
### Example:
```py
colorize("Welcome!", "cyan")
```
### Notes:
1. **colorize()** returns a string
2. If the **string** argument isn't a string, colorize will automatically try to convert it to a string
