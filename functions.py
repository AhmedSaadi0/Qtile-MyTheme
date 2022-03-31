import os
import subprocess
from libqtile import qtile
from keys import ROFI_THEME


def toggle_redshift():
    home = os.path.expanduser('bash ~/.config/qtile/sh/redshift.sh')
    subprocess.run([home])


def show_volume():
    home = os.path.expanduser('~/.config/qtile/sh/show_vol.sh')
    subprocess.run([home])


def open_plasma_systemmonitor():
    qtile.cmd_spawn("plasma-systemmonitor")


def open_gnome_system_monitor():
    qtile.cmd_spawn("gnome-system-monitor")


def open_audio_devices():
    qtile.cmd_spawn("pavucontrol-qt")


def open_power_options():
    qtile.cmd_spawn(
        f"rofi -show p -MODi p:~/.config/qtile/{ROFI_THEME}/rofi-power-menu -theme ~/.config/qtile/{ROFI_THEME}/power-menu-theme-right"
    )


def open_screens():
    qtile.cmd_spawn("systemsettings5 kcm_kscreen")


def open_xfce4_power_manager_settings():
    qtile.cmd_spawn("xfce4-power-manager-settings")
