from libqtile.config import Key
from libqtile.lazy import lazy

TERMINATE = "konsole"
MUSIC_PLAYER = "clementine"
FILE_MANAGER = "dolphin"

MOD = "mod4"
ALT = "mod1"

ROFI_THEME = 'rofi-colors'


app_keys = [
    Key(
        [MOD, "shift"],
        "e",
        lazy.spawn(FILE_MANAGER),
        desc="تشغيل دولفين"
    ),
    Key(
        [MOD, "shift"],
        "t",
        lazy.spawn("telegram-desktop"),
        desc="تشغيل تلقرام"
    ),
    Key(
        [MOD, "shift"],
        "f",
        lazy.spawn("firefox"),
        desc="تشغيل فايرفوكس"
    ),
    Key(
        [MOD, "shift"],
        "c",
        lazy.spawn("code"),
        desc="تشغيل vs code"
    ),
    Key(
        [MOD, "shift"],
        "a",
        lazy.spawn("prime-run studio"),
        desc="تشغيل اندرويد استودسو"
    ),
    Key(
        [MOD, "shift"],
        "p",
        lazy.spawn("prime-run pycharm"),
        desc="تشغيل pycharm"
    ),
    Key(
        [MOD], "c",
        lazy.spawn(MUSIC_PLAYER),
        desc="تشغيل مشغل الموسيقى"
    ),
    Key(
        [MOD], "v",
        lazy.spawn("easyeffects"),
        desc="تشغيل easyeffect"
    ),
    Key(
        [MOD], "z",
        lazy.spawn("xcolor -s"),
        desc="اختيار لون من الشاشة"
    ),
    Key(
        [MOD], "Return",
        lazy.spawn(TERMINATE),
        desc="تشغيل الطرفية"
    ),
    Key(
        [MOD], "t",
        lazy.spawn("sh .config/qtile/sh/redshift.sh"),
        desc="تشغيل الطرفية"
    ),
]

sys_keys = [
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set 5%+"),
        lazy.spawn("sh .config/qtile/sh/show_brightness.sh"),
        desc="رفع مستوى الاضائة"
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        lazy.spawn("sh .config/qtile/sh/show_brightness.sh"),
        desc="خفض مستوى الاضائة"
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer -q sset Master 5%+"),
        lazy.spawn("sh .config/qtile/sh/show_vol.sh"),
        desc="رفع مستوى الصوت"
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer -q sset Master 5%-"),
        lazy.spawn("sh .config/qtile/sh/show_vol.sh"),
        desc="خفض مستوى الصوت"
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        lazy.spawn("sh .config/qtile/sh/show_vol.sh"),
        desc="كتم الصوت"
    ),
    Key(
        [],
        "XF86AudioMicMute",
        lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"),
        # lazy.spawn("sh .config/qtile/sh/show_vol.sh"),
        desc="كتم المايك"
    ),
]

menu_keys = [
    Key(
        [MOD],
        "r",
        lazy.spawn("rofi -show drun"),
        desc="عرض قائمة التطبيقات"
    ),
    Key(
        [MOD],
        "l",
        lazy.spawn(
            f"rofi -show p -MODi p:~/.config/qtile/bin/rofi-power-menu -theme ~/.config/qtile/{ROFI_THEME}/power-menu-theme-right"),
        desc="عرض قائمة الطاقة"
    ),
    Key(
        [MOD],
        "h",
        lazy.spawn("rofi -show p -MODi p:~/.config/qtile/bin/oxid"),
        desc="عرض قائمة الطاقة"
    ),
    Key(
        [ALT],
        'Tab',
        lazy.spawn(
            f"rofi -show windowcd -theme ~/.config/qtile/{ROFI_THEME}/recent-app-theme.rasi"),
        desc="التنقل بين التطبيقات قيد التشغيل"
    ),
    Key(
        [MOD],
        'x',
        lazy.spawn("sh .config/qtile/sh/open_notification_center.sh"),
        desc="الاشعارات"
    ),
]


helper_keys = [
    Key(
        [MOD],
        "Left",
        lazy.layout.left(),
        desc="التركيز على النافذة التي في اليسار"
    ),
    Key(
        [MOD],
        "Right",
        lazy.layout.right(),
        desc="التركيز على النافذة التي في اليمين"
    ),
    Key(
        [MOD],
        "Down",
        lazy.layout.down(),
        desc="التركيز على النافذة التي في الاسفل"
    ),
    Key(
        [MOD],
        "Up",
        lazy.layout.up(),
        desc="التركيز على النافذة التي في الاعلى"
    ),

    Key(
        [MOD, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="تحريك النافذة الى اليسار"),
    Key(
        [MOD, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="تحريك النافذة الى اليمين"),
    Key(
        [MOD, "shift"],
        "Down",
        lazy.layout.shuffle_down(),
        desc="تحريك النافذة الى الاسفل"),
    Key(
        [MOD, "shift"],
        "Up",
        lazy.layout.shuffle_up(),
        desc="تحريك النافذة الى الاعلى"),

    Key(
        [MOD, "control"],
        "Left",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="تكبير النافذة الى جهة اليسار"),
    Key(
        [MOD, "control"],
        "Right",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="تكبير النافذة الى جهة اليمين"),
    Key(
        [MOD],
        "b",
        lazy.layout.normalize(),
        desc="استعادة حجم كل النوافذ"
    ),
    # Toggle between different layouts as defined below
    Key(
        [MOD], "Tab",
        lazy.next_layout(),
        desc="التغغير في وضع النوافذ"
    ),
    Key(
        [MOD, "control"],
        "r",
        lazy.restart(),
        desc="اعادة تشغيل qtile"
    ),
    Key(
        [MOD, ALT],
        "Right",
        lazy.to_screen(0),
        desc="اعادة تشغيل qtile"
    ),
    Key(
        [MOD, ALT],
        "Left",
        lazy.to_screen(1),
        desc="اعادة تشغيل qtile"
    ),


]

window_keys = [
    Key(
        [MOD],
        "q",
        lazy.window.kill(),
        desc="اقتل النافذة"
    ),
    Key(
        [MOD],
        "f",
        lazy.window.toggle_floating(),
        desc='التبديل بين وضع النافذة الطائفة'
    ),
    Key(
        [MOD],
        "m",
        lazy.window.toggle_fullscreen(),
        desc='التبديل بين وضع ملء الشاشة'
    ),
    Key(
        [MOD, ALT],
        "f",
        lazy.window.bring_to_front(),
        desc='التبديل بين وضع ملء الشاشة'
    ),
    Key(
        [MOD],
        "n",
        lazy.window.toggle_minimize(),
        desc='تصغير النافذة'
    ),
]


keys = helper_keys + app_keys + sys_keys + menu_keys + window_keys
