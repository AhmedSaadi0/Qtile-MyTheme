#!/bin/sh

nm-applet -sm-disable &
blueman-applet &
xrandr --output eDP-1 &
xfce4-screensaver &
xfce4-power-manager &
setxkbmap -layout "us,ar" -option "grp:win_space_toggle" &
/usr/lib/polkit-kde-authentication-agent-1 &
picom -b --experimental-backends --dbus --config ~/.config/qtile/picom/picom-no-blur.conf &
deadd-notification-center &