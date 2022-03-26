from libqtile import bar, qtile, widget

from colors import gruvbox


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
        "rofi -show p -MODi p:~/.config/qtile/rofi/rofi-power-menu -theme power-menu-theme-right"
    )


def open_screens():
    qtile.cmd_spawn("systemsettings5 kcm_kscreen")


def open_xfce4_power_manager_settings():
    qtile.cmd_spawn("xfce4-power-manager-settings")


my_bar = bar.Bar([
    # --------------
    #   ايقاف التشغيل
    # --------------
    # widget.TextBox(
    #     background=gruvbox['bg'],
    #     text=" خروج",
    #     padding=10,
    #     # font="Font Awesome 5 Free Solid",
    #     # mouse_callbacks={
    #     #     lazy.spawn(
    #     #         "rofi -show p -modi p:/home/ahmed/.config/rofi/rofi-power-menu -theme power-menu-theme"
    #     #     )
    #     # },
    # ),
    widget.TextBox(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_power_options, },
    ),

    # --------------
    #   برامج الخلفية
    # --------------
    widget.Systray(
        background=gruvbox['bg'],
        padding=10
    ),
    widget.Spacer(length=10),
    # new_left_arrow(gruvbox['bg'], gruvbox['widget-bg']),

    # new_right_arrow(gruvbox['magenta'], gruvbox['bg']),

    # ----------
    #   الساعة
    # ----------
    widget.Clock(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        format="%I:%M - %A %d (%B)",
    ),
    widget.TextBox(
        background=gruvbox['light-yellow'],
        foreground=gruvbox['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
        margin=2
    ),
    widget.Spacer(length=10),

    # --------
    #   الرام
    # --------
    widget.Memory(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        format="{MemPercent: .0f} %",
        font="Font Awesome 5 Free Solid",
        # plasma-systemmonitor
        mouse_callbacks={'Button1': open_plasma_systemmonitor, },
    ),
    widget.TextBox(
        text='',
        background=gruvbox['cyan'],
        foreground=gruvbox['widget-fg'],
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        margin=2
    ),
    widget.Spacer(length=10),

    # ----------
    #   المعالج
    # ----------
    widget.CPU(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        fill_color=gruvbox['widget-fg'],
        graph_color=gruvbox['magenta'],
        format='{load_percent}%',
        font="Font Awesome 5 Free Solid",
        border_width=0,
        line_width=0,
        mouse_callbacks={'Button1': open_gnome_system_monitor, },
    ),
    widget.TextBox(
        background=gruvbox['dark-yellow'],
        foreground=gruvbox['widget-fg'],
        text=' ',
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_gnome_system_monitor, },
    ),
    widget.Spacer(length=10),

    # ----------
    #   NvidiaSensors
    # ----------
    widget.NvidiaSensors(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        # configured_keyboards=['us','ar'],
        # foreground=gruvbox['dark-magenta'],
        # format="{percent:2.0%}",
        font="Font Awesome 5 Free Solid",
    ),
    # -------------
    #   حرارة المعالج
    # -------------
    widget.ThermalSensor(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
    ),
    widget.TextBox(
        background=gruvbox['orange'],
        foreground=gruvbox['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
    ),
    widget.Spacer(length=10),

    # ----------
    #   البطارية
    # ----------
    widget.Battery(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        # foreground=gruvbox['dark-magenta'],
        format="{percent:2.0%}",
        charge_char="",
        empty_char="",
        full_char="",
        font="Font Awesome 5 Free Solid",
        notify_below=25,
        mouse_callbacks={'Button1': open_xfce4_power_manager_settings, },
    ),
    widget.BatteryIcon(
        background=gruvbox['dark-blue'],
        mouse_callbacks={'Button1': open_xfce4_power_manager_settings, },
        # scale=1,
        # theme_path="/home/ahmed/.config/qtile/battery-icons"
        # foreground=gruvbox['dark-magenta'],
        # format="{watt:.2f} W - {percent:2.0%} ",
    ),
    widget.Spacer(length=10),

    # ----------
    #   السطوع
    # ----------
    widget.Backlight(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        backlight_name="intel_backlight",
        # brightness_file="/sys/class/backlight/intel_backlight",
        # max_brightness_file="/sys/class/backlight/intel_backlight",
        # foreground=gruvbox['dark-magenta'],
        format="{percent:2.0%}",
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_screens, },
    ),
    widget.TextBox(
        background=gruvbox['lime'],
        foreground=gruvbox['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_screens, },
    ),
    widget.Spacer(length=10),

    # ---------------
    #   مستوى الصوت
    # ---------------
    widget.Volume(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        # foreground=gruvbox['dark-magenta'],
        # format="{percent:2.0%}",
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_audio_devices, },
    ),
    widget.TextBox(
        background=gruvbox['light-cyan'],
        foreground=gruvbox['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_audio_devices, },
    ),
    widget.Spacer(length=10),

    # ----------
    #   KeyboardLayout
    # ----------
    # widget.KeyboardLayout(
    #     background=gruvbox['yellow'],
    #     configured_keyboards=['us', 'ar'],
    #     # foreground=gruvbox['dark-magenta'],
    #     # format="{percent:2.0%}",
    #     font="Font Awesome 5 Free Solid",
    # ),

    # --------
    #   النت
    # --------
    widget.Net(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        format='{up}  {down} ',
        font="Font Awesome 5 Free Solid",
    ),
    widget.TextBox(
        background=gruvbox['purple'],
        foreground=gruvbox['widget-fg'],
        text='',
        padding=10,
        font="Font Awesome 5 Free Solid",
        mouse_callbacks={'Button1': open_audio_devices, },
    ),
    # ----------
    #   الوسط
    # ----------
    # new_right_arrow(gruvbox['bg'], gruvbox['widget-bg']),
    widget.Prompt(),
    widget.WindowName(
        # format='{name}',
        parse_text=""
    ),
    # new_left_arrow(gruvbox['bg'], gruvbox['dark-yellow']),


    # -------------
    #   TaskList
    # -------------
    # widget.TaskList(
    #     # background=gruvbox['widget-bg'],
    #     # foreground=gruvbox['widget-fg'],
    #     padding=8,
    #     borderwidth=1,
    #     # margin=3,
    #     # max_title_width=0,
    #     fontsize=0,
    #     icon_size=6,
    #     # unfocused_border=gruvbox['magenta']
    #     # format="{percent:2.0%}",
    #     # font="Font Awesome 5 Free Solid",
    # ),


    widget.WindowCount(
        background=gruvbox['widget-bg'],
        foreground=gruvbox['widget-fg'],
        show_zero=True
    ),
    widget.CurrentLayoutIcon(
        background=gruvbox["fg"],
        foreground=gruvbox['widget-fg'],
        scale=0.65,
    ),

    new_left_arrow(gruvbox['bg'], gruvbox['dark-bg']),

    widget.GroupBox(
        background=gruvbox['box_bg'],
        foreground=gruvbox["box_fg"],
        active=gruvbox["box_active"],
        inactive=gruvbox["box_inactive"],

        block_highlight_text_color=gruvbox['block_highlight'],
        highlight_color=gruvbox['box_highlight'],
        
        highlight_method='line',
        disable_drag=True,
        borderwidth=1,
        # padding=3,
    ),
    # widget.Spacer(
    #     background=gruvbox['gray'],
    #     padding=10
    # ),
],
    background=gruvbox['bg'],
    size=20,
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
)
