#!/bin/sh
var=$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')
notify-send 'مستوى الصوت' -h string:synchronous:volume -h int:value:$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }') -h string:x-canonical-private-synchronous:script
