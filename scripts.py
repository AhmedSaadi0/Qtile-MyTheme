import os
import subprocess


def toggle_redshift():
    home = os.path.expanduser('~/.config/qtile/sh/redshift.sh')
    subprocess.run([home])

def show_volume():
    home = os.path.expanduser('~/.config/qtile/sh/show_vol.sh')
    subprocess.run([home])
