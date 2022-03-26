from libqtile.config import Match

# Command to find out wm_class of window: xprop | grep WM_CLASS
workspaces = [
    {
        "name": "1",
        "key": "1",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class="konsole"),
        ],
        "spawn": [],
    },
    {
        "name": "2",
        "key": "2",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class="microsoft-edge"),
            Match(wm_class="google-chrome"),
            Match(wm_class="firefox"),
        ],
        "spawn": [],
    },
    {
        "name": "3",
        "key": "3",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class="code"),
            Match(wm_class="Code"),
        ],
        "spawn": ["google-chrome-stable"],
    },
    {
        "name": "4",
        "key": "4",
        "label": "",
        "layout": "max",
        "matches": [
            Match(wm_class="dolphin"),
            Match(wm_class="nemo"),
            Match(wm_class="ark"),
        ],
        "spawn": [],
    },
    {
        "name": "5",
        "key": "5",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class="jetbrains-idea"),
            Match(wm_class="jetbrains-pycharm"),
            Match(wm_class="jetbrains-clion"),
            Match(wm_class="jetbrains-goland"),
        ],
        "spawn": [],
    },
    {
        "name": "6",
        "key": "6",
        "label": "",
        "layout": "Floating",
        "matches": [
            Match(wm_class="vlc"),
            Match(wm_class="Clementine"),
            Match(wm_class="Pulseeffects"),
            Match(wm_class="mpv"),
            Match(wm_class="easyeffects"),
        ],
        "spawn": [],
    },
    {
        "name": "7",
        "key": "7",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class="TelegramDesktop"),
        ],
        "spawn": ["telegram-desktop"],
    },
]
