#!/bin/sh

nm-applet -sm-disable &
blueman-applet &
xrandr --output eDP-1 &
xfce4-screensaver &
xfce4-power-manager &
picom -b --experimental-backends --dbus --config ~/.config/qtile/picom/sharp_shado.conf &
dunst -config ~/.config/qtile/dunst/dunstrc_nord &
setxkbmap -layout "us,ar" -option "grp:win_space_toggle" &
/usr/lib/polkit-kde-authentication-agent-1 &
