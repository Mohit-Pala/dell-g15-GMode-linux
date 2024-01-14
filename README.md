# dell-g15-GMode-toggle-linux

## works on DELL G15-5535 and DELL G15-5525 (RYZEN VERSION)

Python script to control dell GMode on linux

# Dependencies:
    acpi_call kernel module
    pkexec or sudo
    python

# Bind to shortcut on KDE:

move python script to `~/.local/bin/`

System settings -> shortcuts -> add command

add command `konsole -e python ~/.local/bin/g15-Gmode-linux.py` and bind to F9

