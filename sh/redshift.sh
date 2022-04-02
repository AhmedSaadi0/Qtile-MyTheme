#!/bin/sh
if [ ! -z $(pgrep redshift) ];
then
    redshift -x && pkill redshift && killall redshift
    dunstify -a "redshift" -u low -i display-brightness -h string:x-dunst-stack-tag:"وضع الليل" "ايقاف وضع الليل"
else
    redshift -l 0:0 -t 4500:4500 -r &>/dev/null &
    dunstify -a "redshift" -u low -i display-brightness -h string:x-dunst-stack-tag:"وضع الليل" "تشغيل وضع الليل"
fi
