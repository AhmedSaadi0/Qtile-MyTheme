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
        # widget.TextBox(
        #     background=theme['widget-bg'],
        #     foreground=theme['orange'],
        #     text='خروج',
        #     # padding=10,
        #     # font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_power_options, },
        # ),
        widget.TextBox(
            background=theme['bg'],
            foreground=theme['orange'],
            text='',
            # padding=10,
            fontshadow=theme['bg'],
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_power_options, },
        ),
        widget.Spacer(length=7),

        # --------------
        #   برامج الخلفية
        # --------------
        widget.Systray(
            background=theme['widget-bg'],
            fontshadow=theme['bg'],
            foreground=theme['orange'],
            padding=10
        ),
        widget.TextBox(
            background=theme['widget-bg'],
            foreground=theme['purple'],
            fontshadow=theme['bg'],
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
            foreground=theme['cyan'],
            # foreground=theme['dark-magenta'],
            format="{percent:2.0%}",
            fontshadow=theme['bg'],
            charge_char="",
            empty_char="",
            full_char="",
            font="Font Awesome 5 Free Solid",
            notify_below=25,
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
        ),
        widget.BatteryIcon(
            background=theme['widget-bg'],
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
            foreground=theme['light-yellow'],
            backlight_name="intel_backlight",
            # brightness_file="/sys/class/backlight/intel_backlight",
            # max_brightness_file="/sys/class/backlight/intel_backlight",
            # foreground=theme['dark-magenta'],
            fontshadow=theme['bg'],
            format="{percent:2.0%}  ",
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': toggle_redshift, },
        ),
        widget.Spacer(length=7),

        # ---------------
        #   مستوى الصوت
        # ---------------
        widget.Volume(
            background=theme['widget-bg'],
            foreground=theme['blue'],
            # foreground=theme['dark-magenta'],
            format="{percent:2.0%} ",
            font="Font Awesome 5 Free Solid",
            fontshadow=theme['bg'],
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        widget.TextBox(
            background=theme['widget-bg'],
            foreground=theme['blue'],
            text='',
            padding=5,
            fontsize=12,
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        widget.Spacer(length=7),

        # --------
        #   النت
        # --------
        widget.Net(
            background=theme['widget-bg'],
            foreground=theme['purple'],
            fontshadow=theme['bg'],
            format='{up}  {down}   ',
            font="Font Awesome 5 Free Solid",
        ),
        widget.Spacer(length=7),

        # --------
        #   Wallpaper
        # --------
        widget.Wallpaper(
            background=theme['widget-bg'],
            foreground=theme['pink'],
            fontshadow=theme['bg'],
            label="",
            directory="/media/shared/Pictures/fav/new/nordic-wallpapers",
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
            foreground=theme['light-yellow'],
            format="(%I:%M) - %A, %d %B  ",
            fontshadow=theme['bg'],
        ),
        # widget.TextBox(
        #     background=theme['widget-bg'],
        #     foreground=theme['purple'],
        #     text='',
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     margin=2
        # ),
        widget.Spacer(),
        # ------------------------------------------------
        # ------------------ نهاية الوسط -------------------
        # ------------------------------------------------

        # -------------
        #   حرارة المعالج
        # -------------
        widget.ThermalSensor(
            background=theme['widget-bg'],
            foreground=theme['orange'],
            fontshadow=theme['bg'],
        ),
        widget.TextBox(
            background=theme['widget-bg'],
            foreground=theme['orange'],
            fontshadow=theme['bg'],
            text='',
            padding=5,
            fontsize=12,
            font="Font Awesome 5 Free Solid",
        ),
        widget.Spacer(length=7),


        # --------
        #   الرام
        # --------
        widget.Memory(
            background=theme['widget-bg'],
            foreground=theme['good_green'],
            format="{MemPercent: .0f} %  ",
            fontshadow=theme['bg'],
            font="Font Awesome 5 Free Solid",
            # plasma-systemmonitor
            mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        ),
        # widget.TextBox(
        #     text='',
        #     background=theme['dark-blue'],
        #     foreground=theme['widget-fg'],
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        #     margin=2
        # ),
        widget.Spacer(length=7),

        # ----------
        #   المعالج
        # ----------
        widget.CPUGraph(
            background=theme['widget-bg'],
            foreground=theme['dark-yellow'],
            fill_color=theme['dark-yellow'],
            graph_color=theme['magenta'],
            # format='{load_percent}%',
            font="Font Awesome 5 Free Solid",
            border_width=0,
            line_width=0,
            mouse_callbacks={'Button1': open_gnome_system_monitor, },
        ),
        # widget.TextBox(
        #     background=theme['dark-yellow'],
        #     foreground=theme['widget-bg'],
        #     text=' ',
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_gnome_system_monitor, },
        # ),
        widget.Spacer(length=7),

        widget.GroupBox(
            background=theme['widget-bg'],
            foreground=theme["box_fg"],
            active=theme["box_active"],
            inactive=theme["box_inactive"],

            # لون نص الصفحة المحددة
            block_highlight_text_color=theme['block_highlight'],
            # لون المحدد
            highlight_color=theme['box_highlight'],

            highlight_method='line',
            disable_drag=True,
            borderwidth=2,
            padding=4,
        ),

        widget.Spacer(length=7),

        widget.WindowCount(
            background=theme['widget-bg'],
            foreground=theme['pink'],
            show_zero=True,
        ),
        widget.CurrentLayoutIcon(
            background=theme["widget-bg"],
            foreground=theme['pink'],
            scale=0.65,
            padding=3,
        ),

        widget.Spacer(length=7),

    ],
    background=theme['bg'],
    size=22,
    border_width=[4, 0, 4, 0],  # Draw top and bottom borders
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
            foreground=theme['cyan'],
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
            background=theme['widget-bg'],
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
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
            foreground=theme['blue'],
            # foreground=theme['dark-magenta'],
            format="{percent:2.0%} ",
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        widget.TextBox(
            background=theme['widget-bg'],
            foreground=theme['blue'],
            text='',
            padding=5,
            fontsize=12,
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        widget.Spacer(length=7),

        # --------
        #   النت
        # --------
        widget.Net(
            background=theme['widget-bg'],
            foreground=theme['purple'],
            format='{up}  {down}   ',
            font="Font Awesome 5 Free Solid",
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
            foreground=theme['light-yellow'],
            format="(%I:%M) - %A, %d %B  ",
        ),
        # widget.TextBox(
        #     background=theme['widget-bg'],
        #     foreground=theme['purple'],
        #     text='',
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     margin=2
        # ),
        widget.Spacer(),
        # ------------------------------------------------
        # ------------------ نهاية الوسط -------------------
        # ------------------------------------------------

        # -------------
        #   حرارة المعالج
        # -------------
        widget.ThermalSensor(
            background=theme['widget-bg'],
            foreground=theme['orange'],
        ),
        widget.TextBox(
            background=theme['widget-bg'],
            foreground=theme['orange'],
            text='',
            padding=5,
            fontsize=12,
            font="Font Awesome 5 Free Solid",
        ),
        widget.Spacer(length=7),


        # --------
        #   الرام
        # --------
        widget.Memory(
            background=theme['widget-bg'],
            foreground=theme['good_green'],
            format="{MemPercent: .0f} %  ",
            font="Font Awesome 5 Free Solid",
            # plasma-systemmonitor
            mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        ),
        # widget.TextBox(
        #     text='',
        #     background=theme['dark-blue'],
        #     foreground=theme['widget-fg'],
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        #     margin=2
        # ),
        widget.Spacer(length=7),

        # ----------
        #   المعالج
        # ----------
        widget.CPUGraph(
            background=theme['widget-bg'],
            foreground=theme['dark-yellow'],
            fill_color=theme['dark-yellow'],
            graph_color=theme['magenta'],
            # format='{load_percent}%',
            font="Font Awesome 5 Free Solid",
            border_width=0,
            line_width=0,
            mouse_callbacks={'Button1': open_gnome_system_monitor, },
        ),
        # widget.TextBox(
        #     background=theme['dark-yellow'],
        #     foreground=theme['widget-bg'],
        #     text=' ',
        #     padding=10,
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_gnome_system_monitor, },
        # ),
        widget.Spacer(length=7),

        widget.GroupBox(
            background=theme['widget-bg'],
            foreground=theme["box_fg"],
            active=theme["box_active"],
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
            foreground=theme['pink'],
            show_zero=True,
        ),
        widget.CurrentLayoutIcon(
            background=theme["widget-bg"],
            foreground=theme['pink'],
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
