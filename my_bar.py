from libqtile import bar, widget

from colors import style as theme
from functions import (open_audio_devices, open_gnome_system_monitor,
                       open_plasma_systemmonitor, open_power_options,
                       open_xfce4_power_manager_settings, toggle_redshift)


screen1_bar = bar.Bar(
    [
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
            background=theme['red'],
            foreground=theme['widget-fg'],
            text='',
            # padding=10,
            # font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_power_options, },
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
            background=theme['purple'],
            foreground=theme['widget-fg'],
            text='',
            padding=7,
            # font="Font Awesome 5 Free Solid",
            # mouse_callbacks={'Button1': open_power_options, },
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
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
        ),
        widget.BatteryIcon(
            background=theme['cyan'],
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
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
            mouse_callbacks={'Button1': toggle_redshift, },
        ),
        widget.TextBox(
            background=theme['lime'],
            foreground=theme['widget-fg'],
            text='',
            padding=10,
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': toggle_redshift, },
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

        # ------------------------------------------------
        # ------------------ بداية الوسط -------------------
        # ------------------------------------------------
        widget.Spacer(),
        # ----------
        #   الساعة
        # ----------
        widget.Clock(
            background=theme['widget-bg'],
            foreground=theme['widget-fg'],
            format="(%I:%M) - %A, %d %B",
        ),
        widget.TextBox(
            background=theme['light-yellow'],
            foreground=theme['widget-bg'],
            text='',
            padding=10,
            font="Font Awesome 5 Free Solid",
            margin=2
        ),
        widget.Spacer(),
        # ------------------------------------------------
        # ------------------ نهاية الوسط -------------------
        # ------------------------------------------------

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
            background=theme['dark-blue'],
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
        widget.CPUGraph(
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
            foreground=theme['widget-bg'],
            text=' ',
            padding=10,
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_gnome_system_monitor, },
        ),
        widget.Spacer(length=7),

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
    border_width=[7, 0, 7, 0],  # Draw top and bottom borders
    border_color=[
        theme["bg"],
        theme["bg"],
        theme["bg"],
        theme["bg"]
    ]  # Borders are magenta
)

screen2_bar = bar.Bar(
    [
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
            background=theme['cyan'],
            mouse_callbacks={'Button1': open_xfce4_power_manager_settings, },
            # scale=1,
            # color_path="/home/ahmed/.config/qtile/battery-icons"
            # foreground=theme['dark-magenta'],
            # format="{watt:.2f} W - {percent:2.0%} ",
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

        # -------------
        #   حرارة المعالج
        # -------------
        widget.ThermalZone(
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

        # ------------------------------------------------
        # ------------------ بداية الوسط -------------------
        # ------------------------------------------------
        widget.Spacer(),
        # ----------
        #   الساعة
        # ----------
        widget.Clock(
            background=theme['widget-bg'],
            foreground=theme['widget-fg'],
            format="(%I:%M) - %A, %d %B",
        ),
        widget.TextBox(
            background=theme['light-yellow'],
            foreground=theme['widget-bg'],
            text='',
            padding=10,
            font="Font Awesome 5 Free Solid",
            margin=2
        ),
        widget.Spacer(),
        # ------------------------------------------------
        # ------------------ نهاية الوسط -------------------
        # ------------------------------------------------

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
            background=theme['dark-blue'],
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
        widget.CPUGraph(
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
            foreground=theme['widget-bg'],
            text=' ',
            padding=10,
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_gnome_system_monitor, },
        ),
        widget.Spacer(length=7),

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
