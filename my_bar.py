from libqtile import bar, qtile, widget

from colors import style as theme
from keys import ROFI_THEME


def left_half_circle(fg_color):
    return widget.TextBox(
        text='\uE0B6',
        fontsize=28,
        foreground=fg_color,
        padding=0)


def right_half_circle(fg_color):
    return widget.TextBox(
        text='\uE0B4',
        fontsize=28,
        foreground=fg_color,
        padding=0)


def lower_left_triangle(bg_color, fg_color):
    return widget.TextBox(
        text='\u25e2',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color)


def left_arrow(bg_color, fg_color):
    return widget.TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=22,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color):
    return widget.TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=22,
        background=bg_color,
        foreground=fg_color)


def new_right_arrow(bg_color, fg_color):
    return widget.TextBox(
        text='',
        padding=0,
        fontsize=20,
        background=bg_color,
        foreground=fg_color)


def new_left_arrow(bg_color, fg_color):
    return widget.TextBox(
        text='',
        padding=0,
        fontsize=20,
        background=bg_color,
        foreground=fg_color)


def open_plasma_systemmonitor():
    qtile.cmd_spawn("plasma-systemmonitor")


def open_gnome_system_monitor():
    qtile.cmd_spawn("gnome-system-monitor")


def open_audio_devices():
    qtile.cmd_spawn("pavucontrol-qt")


def open_power_options():
    qtile.cmd_spawn(
        f"rofi -show p -MODi p:~/.config/qtile/{ROFI_THEME}/rofi-power-menu -theme ~/.config/qtile/rofi/power-menu-theme-right"
    )


def open_screens():
    qtile.cmd_spawn("systemsettings5 kcm_kscreen")


def open_xfce4_power_manager_settings():
    qtile.cmd_spawn("xfce4-power-manager-settings")


my_bar = bar.Bar([
    widget.Spacer(length=7),

    # --------------
    #   ايقاف التشغيل
    # --------------
    widget.TextBox(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        text='خروج',
        # padding=10,
        # font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_power_options, },
    ),
    widget.TextBox(
        background=theme['cyan'],
        foreground=theme['widget-fg'],
        text='',
        # padding=10,
        # font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_power_options, },
    ),
    widget.Spacer(length=7),

    # ----------
    #   الساعة
    # ----------
    widget.Clock(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        format="%I:%M - %A %d (%B)",
    ),
    widget.TextBox(
        background=theme['light-yellow'],
        foreground=theme['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
        margin=2
    ),
    widget.Spacer(length=7),

    # --------------
    #   برامج الخلفية
    # --------------
    widget.Systray(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        padding=10
    ),
    widget.TextBox(
        background=theme['red'],
        foreground=theme['widget-fg'],
        text='',
        padding=7,
        # font="Font Awesome 5 Free Solid",
        # mouse_callbacks={'Button1': open_power_options, },
    ),
    widget.Spacer(length=7),

    # --------
    #   الرام
    # --------
    widget.Memory(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        format="{MemPercent: .0f} %",
        font="Font Awesome 5 Free Solid",
        # plasma-systemmonitor
        mouse_callbacks={'Button1': open_plasma_systemmonitor, },
    ),
    widget.TextBox(
        text='',
        background=theme['cyan'],
        foreground=theme['widget-fg'],
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        margin=2
    ),
    widget.Spacer(length=7),

    # ----------
    #   المعالج
    # ----------
    widget.CPU(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        fill_color=theme['widget-fg'],
        graph_color=theme['magenta'],
        format='{load_percent}%',
        font="Font Awesome 5 Free Solid",
        border_width=0,
        line_width=0,
        mouse_callbacks={'Button1': open_gnome_system_monitor, },
    ),
    widget.TextBox(
        background=theme['dark-yellow'],
        foreground=theme['widget-fg'],
        text=' ',
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_gnome_system_monitor, },
    ),
    widget.Spacer(length=7),

    # ----------
    #   NvidiaSensors
    # ----------
    widget.NvidiaSensors(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        # configured_keyboards=['us','ar'],
        # foreground=theme['dark-magenta'],
        # format="{percent:2.0%}",
        font="Font Awesome 5 Free Solid",
    ),
    # -------------
    #   حرارة المعالج
    # -------------
    widget.ThermalSensor(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
    ),
    widget.TextBox(
        background=theme['orange'],
        foreground=theme['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
    ),
    widget.Spacer(length=7),

    # ----------
    #   البطارية
    # ----------
    widget.Battery(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        # foreground=theme['dark-magenta'],
        format="{percent:2.0%}",
        charge_char="",
        empty_char="",
        full_char="",
        font="Font Awesome 5 Free Solid",
        notify_below=25,
        mouse_callbacks={'Button1': open_xfce4_power_manager_settings, },
    ),
    widget.BatteryIcon(
        background=theme['dark-blue'],
        mouse_callbacks={'Button1': open_xfce4_power_manager_settings, },
        # scale=1,
        # color_path="/home/ahmed/.config/qtile/battery-icons"
        # foreground=theme['dark-magenta'],
        # format="{watt:.2f} W - {percent:2.0%} ",
    ),
    widget.Spacer(length=7),

    # ----------
    #   السطوع
    # ----------
    widget.Backlight(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        backlight_name="intel_backlight",
        # brightness_file="/sys/class/backlight/intel_backlight",
        # max_brightness_file="/sys/class/backlight/intel_backlight",
        # foreground=theme['dark-magenta'],
        format="{percent:2.0%}",
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_screens, },
    ),
    widget.TextBox(
        background=theme['lime'],
        foreground=theme['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_screens, },
    ),
    widget.Spacer(length=7),

    # ---------------
    #   مستوى الصوت
    # ---------------
    widget.Volume(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        # foreground=theme['dark-magenta'],
        # format="{percent:2.0%}",
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_audio_devices, },
    ),
    widget.TextBox(
        background=theme['light-cyan'],
        foreground=theme['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_audio_devices, },
    ),
    widget.Spacer(length=7),

    # ----------
    #   KeyboardLayout
    # ----------
    # widget.KeyboardLayout(
    #     background=theme['yellow'],
    #     configured_keyboards=['us', 'ar'],
    #     # foreground=theme['dark-magenta'],
    #     # format="{percent:2.0%}",
    #     font="Font Awesome 5 Free Solid",
    # ),

    # --------
    #   النت
    # --------
    widget.Net(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        format='{up}  {down} ',
        font="Font Awesome 5 Free Solid",
    ),
    widget.TextBox(
        background=theme['purple'],
        foreground=theme['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_audio_devices, },
    ),
    widget.Spacer(length=7),

    # --------
    #   الخلفيات
    # --------
    # widget.Wallpaper(
    #     directory="/media/shared/Pictures/fav/",
    #     background=theme['widget-bg'],
    #     foreground=theme['widget-fg'],
    #     font="Font Awesome 5 Free Solid",
    # ),
    # widget.TextBox(
    #     background=theme['yellow'],
    #     foreground=theme['widget-fg'],
    #     text='',
    #     padding=10,
    #     font="Font Awesome 5 Free Solid",
    #     mouse_callbacks={'Button1': open_audio_devices, },
    # ),
    # ----------
    #   الوسط
    # ----------
    # new_right_arrow(theme['bg'], theme['widget-bg']),
    # widget.Prompt(),
    # widget.WindowName(
    #     # background=theme['widget-bg'],
    #     # foreground=theme['widget-fg'],
    #     # format='{name}',
    #     parse_text="",
    # ),
    widget.Spacer(),
    # new_left_arrow(theme['bg'], theme['dark-yellow']),

    # -------------
    #   TaskList
    # -------------
    # widget.TaskList(
    #     # background=theme['widget-bg'],
    #     # foreground=theme['widget-fg'],
    #     padding=8,
    #     borderwidth=1,
    #     # margin=3,
    #     # max_title_width=0,
    #     fontsize=0,
    #     icon_size=6,
    #     # unfocused_border=theme['magenta']
    #     # format="{percent:2.0%}",
    #     # font="Font Awesome 5 Free Solid",
    # ),

    widget.GroupBox(
        background=theme['widget-bg'],
        foreground=theme["widget-bg"],
        active=theme["widget-fg"],
        inactive=theme["box_inactive"],

        # لون نص الصفحة المحددة
        block_highlight_text_color=theme['block_highlight'],
        # لون المحدد
        highlight_color=theme['box_highlight'],

        highlight_method='line',
        disable_drag=True,
        borderwidth=3,
        padding=4,
    ),

    widget.Spacer(length=7),

    widget.WindowCount(
        background=theme['widget-bg'],
        foreground=theme['widget-fg'],
        show_zero=True,
    ),
    widget.CurrentLayoutIcon(
        background=theme["lime"],
        foreground=theme['widget-fg'],
        scale=0.65,
        padding=3,
    ),

    widget.Spacer(length=7),

],
    background=theme['bg'],
    size=22,
    border_width=[6, 0, 6, 0],  # Draw top and bottom borders
    border_color=[
        theme["bg"],
        theme["bg"],
        theme["bg"],
        theme["bg"]
]  # Borders are magenta
)
