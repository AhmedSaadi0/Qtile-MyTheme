from libqtile import bar, widget

from colors import c1 as theme
from functions import (open_audio_devices, open_gnome_system_monitor, open_notification_center,
                       open_plasma_systemmonitor, open_power_options,
                       open_xfce4_power_manager_settings, toggle_redshift)


def lower_left_triangle(bg_color, fg_color):
    return widget.TextBox(
        text='',
        padding=0,
        fontsize=18,
        font="Iosevka Custom",
        background=bg_color,
        foreground=fg_color,
    )

def lower_right_triangle(bg_color, fg_color):
    return widget.TextBox(
        text='',
        padding=0,
        fontsize=18,
        font="Iosevka Custom",
        background=bg_color,
        foreground=fg_color,
    )


screen1_bar = bar.Bar(
    [
        widget.Spacer(
            length=10,
            background=theme['p1'],
        ),

        # --------------
        #   ايقاف التشغيل
        # --------------
        # lower_left_triangle(
        #     bg_color=theme['p1'],
        #     fg_color=theme['p1'],
        # ),
        widget.TextBox(
            background=theme['p1'],
            foreground=theme['widget-bg'],
            text='',
            # padding=10,
            # font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_power_options, },
        ),
        lower_left_triangle(
            bg_color=theme['p1'],
            fg_color=theme['p6'],
        ),

        widget.TextBox(
            background=theme['p6'],
            foreground=theme['widget-fg'],
            text='',
            # padding=10,
            # font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_notification_center, },
        ),
        lower_left_triangle(
            bg_color=theme['p6'],
            fg_color=theme['p2'],
        ),

        # --------------
        #   برامج الخلفية
        # --------------
        widget.Systray(
            background=theme['p2'],
            foreground=theme['widget-fg'],
            padding=10
        ),
        lower_left_triangle(
            bg_color=theme['p2'],
            fg_color=theme['p3'],
        ),
        # ----------
        #   البطارية
        # ----------
        widget.Battery(
            background=theme['p3'],
            foreground=theme['widget-fg'],
            low_background=theme['danger'],
            low_percentage=0.2,
            format="{percent:2.0%} {char}",
            charge_char="",
            full_char="",
            empty_char="",
            discharge_char="",
            unknown_char="",
            update_interval=1,
            font="Font Awesome 5 Free Solid",
            notify_below=20,
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
        ),
        # widget.BatteryIcon(
        #     background=theme['p3'],
        #     mouse_callbacks={
        #         'Button1': open_xfce4_power_manager_settings, },
        #     update_interval=1,
        #     notify_below=20,
        #     theme_path="/home/docs/checkouts/readthedocs.org/user_builds/qtile/checkouts/latest/libqtile/resources/battery-icons",
        #     # scale=1,
        #     # foreground=theme['dark-magenta'],
        #     # format="{watt:.2f} W - {percent:2.0%} ",
        # ),
        lower_left_triangle(
            bg_color=theme['p3'],
            fg_color=theme['p4'],
        ),

        # ----------
        #   السطوع
        # ----------
        widget.Backlight(
            background=theme['p4'],
            foreground=theme['widget-fg'],
            backlight_name="intel_backlight",
            # brightness_file="/sys/class/backlight/intel_backlight",
            # max_brightness_file="/sys/class/backlight/intel_backlight",
            # foreground=theme['dark-magenta'],
            format="{percent:2.0%} ",
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': toggle_redshift, },
        ),
        lower_left_triangle(
            bg_color=theme['p4'],
            fg_color=theme['p5-d'],
        ),
        # ---------------
        #   مستوى الصوت
        # ---------------
        # widget.Volume(
        #     background=theme['p5-d'],
        #     foreground=theme['widget-fg'],
        #     # foreground=theme['dark-magenta'],
        #     format=" {percent:2.0%}",
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_audio_devices, },
        # ),
        widget.Volume(
            background=theme['p5-d'],
            foreground=theme['widget-fg'],
            # foreground=theme['dark-magenta'],
            # format=" {percent:2.0%}",
            fmt='{} ',
            # emoji=True,
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        lower_left_triangle(
            bg_color=theme['p5-d'],
            fg_color=theme['p5-l'],
        ),

        # --------
        #   النت
        # --------
        widget.Net(
            background=theme['p5-l'],
            foreground=theme['widget-bg'],
            format='{up}  {down} ',
            font="Font Awesome 5 Free Solid",
        ),
        lower_left_triangle(
            bg_color=theme['p5-l'],
            fg_color=theme['bg'],
        ),

        # ------------------------------------------------
        # ------------------ بداية الوسط -------------------
        # ------------------------------------------------
        widget.Spacer(),
        # lower_left_triangle(
        #     bg_color=theme['bg'],
        #     fg_color=theme['p7'],
        # ),
        widget.Clock(
            background=theme['p7'],
            foreground=theme['widget-bg'],
            format="(%I:%M) - %A, %d %B ",
        ),
        # lower_right_triangle(
        #     bg_color=theme['bg'],
        #     fg_color=theme['p7'],
        # ),
        widget.Spacer(),
        # ------------------------------------------------
        # ------------------ نهاية الوسط -------------------
        # ------------------------------------------------

        # -------------
        #   حرارة المعالج
        # -------------
        lower_left_triangle(
            bg_color=theme['bg'],
            fg_color=theme['p6'],
        ),
        widget.ThermalSensor(
            background=theme['p6'],
            foreground=theme['widget-fg'],
            # format="{thermal:2.0%} - "
        ),
        lower_left_triangle(
            bg_color=theme['p6'],
            fg_color=theme['p5'],
        ),

        # --------
        #   الرام
        # --------
        widget.Memory(
            background=theme['p5'],
            foreground=theme['widget-fg'],
            format="{MemPercent: .0f}% ",
            font="Font Awesome 5 Free Solid",
            # plasma-systemmonitor
            mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        ),
        lower_left_triangle(
            bg_color=theme['p5'],
            fg_color=theme['p8'],
        ),

        # ----------
        #   المعالج
        # ----------
        widget.CPUGraph(
            background=theme['p8'],
            foreground=theme['widget-fg'],
            fill_color=theme['widget-fg'],
            graph_color=theme['magenta'],
            format='{load_percent}%',
            font="Font Awesome 5 Free Solid",
            border_width=0,
            line_width=0,
            mouse_callbacks={'Button1': open_gnome_system_monitor, },
        ),
        lower_left_triangle(
            bg_color=theme['p8'],
            fg_color=theme['box_bg'],
        ),

        widget.GroupBox(
            background=theme['box_bg'],
            foreground=theme["box_fg"],
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

        lower_left_triangle(
            bg_color=theme['box_bg'],
            fg_color=theme['lime'],
        ),

        widget.WindowCount(
            background=theme['lime'],
            foreground=theme['widget-fg'],
            show_zero=True,
        ),
        # widget.CurrentLayout(
        #     background=theme['lime'],
        #     foreground=theme['widget-fg'],
        #     show_zero=True,
        # ),
        widget.CurrentLayoutIcon(
            background=theme["lime"],
            foreground=theme['widget-fg'],
            scale=0.65,
            padding=3,
        ),

    ],
    background=theme['bg'],
    size=22,
    border_width=[3, 3, 3, 3],  # Draw top and bottom borders
    border_color=[
        theme["bg"],
        theme["bg"],
        theme["bg"],
        theme["bg"]
    ]  # Borders are magenta
)

screen2_bar = bar.Bar(
    [
        widget.Spacer(
            length=10,
            background=theme['p1'],
        ),

        # ----------
        #   البطارية
        # ----------
        widget.Battery(
            background=theme['p1'],
            foreground=theme['widget-bg'],
            low_background=theme['danger'],
            low_percentage=0.2,
            format="{percent:2.0%} {char}",
            charge_char="",
            full_char="",
            empty_char="",
            discharge_char="",
            unknown_char="",
            update_interval=1,
            font="Font Awesome 5 Free Solid",
            # notify_below=20,
            mouse_callbacks={
                'Button1': open_xfce4_power_manager_settings, },
        ),
        lower_left_triangle(
            bg_color=theme['p1'],
            fg_color=theme['p4'],
        ),

        # ---------------
        #   مستوى الصوت
        # ---------------
        # widget.Volume(
        #     background=theme['p5-d'],
        #     foreground=theme['widget-fg'],
        #     # foreground=theme['dark-magenta'],
        #     format=" {percent:2.0%}",
        #     font="Font Awesome 5 Free Solid",
        #     mouse_callbacks={'Button1': open_audio_devices, },
        # ),
        widget.Volume(
            background=theme['p4'],
            foreground=theme['widget-fg'],
            # foreground=theme['dark-magenta'],
            # format=" {percent:2.0%}",
            fmt='{} ',
            # emoji=True,
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={'Button1': open_audio_devices, },
        ),
        lower_left_triangle(
            bg_color=theme['p4'],
            fg_color=theme['p5-l'],
        ),

        # --------
        #   النت
        # --------
        widget.Net(
            background=theme['p5-l'],
            foreground=theme['widget-bg'],
            format='{up}  {down} ',
            font="Font Awesome 5 Free Solid",
        ),
        lower_left_triangle(
            bg_color=theme['p5-l'],
            fg_color=theme['bg'],
        ),

        # ------------------------------------------------
        # ------------------ بداية الوسط -------------------
        # ------------------------------------------------
        widget.Spacer(),
        lower_left_triangle(
            bg_color=theme['bg'],
            fg_color=theme['p7'],
        ),
        widget.Clock(
            background=theme['p7'],
            foreground=theme['widget-bg'],
            format="(%I:%M) - %A, %d %B",
        ),
        lower_left_triangle(
            bg_color=theme['p7'],
            fg_color=theme['bg'],
        ),
        widget.Spacer(),
        # ------------------------------------------------
        # ------------------ نهاية الوسط -------------------
        # ------------------------------------------------

        # --------
        #   الرام
        # --------
        lower_left_triangle(
            bg_color=theme['bg'],
            fg_color=theme['p5'],
        ),
        widget.Memory(
            background=theme['p5'],
            foreground=theme['widget-fg'],
            format="{MemPercent: .0f}% ",
            font="Font Awesome 5 Free Solid",
            # plasma-systemmonitor
            mouse_callbacks={'Button1': open_plasma_systemmonitor, },
        ),
        lower_left_triangle(
            bg_color=theme['p5'],
            fg_color=theme['p8'],
        ),

        # ----------
        #   المعالج
        # ----------
        widget.CPUGraph(
            background=theme['p8'],
            foreground=theme['widget-fg'],
            fill_color=theme['widget-fg'],
            graph_color=theme['magenta'],
            format='{load_percent}%',
            font="Font Awesome 5 Free Solid",
            border_width=0,
            line_width=0,
            mouse_callbacks={'Button1': open_gnome_system_monitor, },
        ),
        lower_left_triangle(
            bg_color=theme['p8'],
            fg_color=theme['box_bg'],
        ),

        widget.GroupBox(
            background=theme['box_bg'],
            foreground=theme["box_fg"],
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

        lower_left_triangle(
            bg_color=theme['box_bg'],
            fg_color=theme['lime'],
        ),

        widget.WindowCount(
            background=theme['lime'],
            foreground=theme['widget-fg'],
            show_zero=True,
        ),
        widget.CurrentLayoutIcon(
            background=theme["lime"],
            foreground=theme['widget-fg'],
            scale=0.65,
            padding=3,
        ),

    ],
    background=theme['bg'],
    size=22,
    border_width=[3, 3, 3, 3],  # Draw top and bottom borders
    border_color=[
        theme["bg"],
        theme["bg"],
        theme["bg"],
        theme["bg"]
    ]  # Borders are magenta
)
