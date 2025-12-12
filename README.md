# gimp-add-guides-33-66

# Add Guides 33% / 66% for GIMP 3

Python script for GIMP 3 that adds horizontal and vertical guides at positions 33% and 66%.

## Installation
Copy `add-guides-33-66.py` to:

- macOS: `~/Library/Application Support/GIMP/3.0/plug-ins/`
- Linux: `~/.config/GIMP/3.0/plug-ins/`

Ensure it has execute permissions:

```bash
chmod +x add-guides-33-66.py
```

## Log
To check if there are any problems with the script's execution, you can run GIMP using:

```bash
gimp --verbose 2>&1 | grep -i "python\|error\|guide"
```