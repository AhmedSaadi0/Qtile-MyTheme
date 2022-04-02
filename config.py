# from logging import disable
import os
import subprocess
from typing import List  # noqa: F401

from libqtile import hook, layout
from libqtile.config import Click, Drag, Key, Match, Screen, Group
from libqtile.lazy import lazy

# from keys import mod as mod
from layouts import workspaces
# from my_bar import my_bar, screen2_bar
from bar_color_theme import screen1_bar, screen2_bar
from keys import keys, MOD as mod
from colors import style as color

groups = []

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(
        Group(
            workspace["name"],
            matches=matches,
            layout=workspace["layout"],
            spawn=workspace["spawn"],
            label=workspace["label"],
        ))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(),
            desc="التحويل الى المجموعة",
        ))
    keys.append(
        Key(
            [mod, "shift"],
            workspace["key"],
            lazy.window.togroup(workspace["name"]),
            desc="انقل البرنامج الى المجموعة",
        ))


layouts = [
    layout.MonadTall(
        border_focus=color["border_active"],
        border_normal=color['border_inactive'],
        border_on_single=True,
        border_width=1,
        margin=8,
        margin_on_single=8,
        align=layout.MonadTall._right,
    ),
    layout.RatioTile(
        border_focus=color["border_active"],
        border_normal=color['border_inactive'],
        border_on_single=True,
        border_width=1,
        margin=4,
        margin_on_single=4,
        fancy=True,
    ),
    layout.Floating(
        border_focus=color["border_active"],
        border_normal=color['border_inactive'],
        border_on_single=True,
        border_width=1,
    ),
    layout.Columns(
        border_focus="#e6bd7c",
        border_normal="#2c2f36",
        border_on_single=True,
        border_width=1,
        margin=4,
        margin_on_single=4,
        insert_position=1,
    ),
    # layout.Stack(num_stacks=2),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JF Flat",
    fontsize=14,
    padding=10,
    margin=4
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper_mode="fill",
        top=screen1_bar,
        # wallpaper="/media/shared/Pictures/fav/new/nordic-wallpapers/underwater.png",
        # wallpaper="/media/shared/Pictures/fav/new/nordic-wallpapers/ign_astronautInTheOcean.png",
        wallpaper="~/.config/qtile/wallpapers/background.png",
        # wallpaper="/media/shared/Pictures/fav/day/1.jpg",
        # wallpaper="/media/shared/Pictures/fav/new/gruvbox-wallpaper/hotline-miami.jpg",
        # wallpaper="/media/shared/Pictures/fav/new/gruvbox-wallpaper/soviet-rocket.jpg",
        # wallpaper="/media/shared/Pictures/fav/new/gruvbox-wallpaper/houses.jpg",
        # wallpaper="~/.config/qtile/splash.png",
        # wallpaper="~/.config/qtile/nord.png",
    ),
    Screen(
        wallpaper_mode="fill",
        top=screen2_bar,
        # wallpaper="/media/shared/Pictures/fav/new/nordic-wallpapers/wild.png",
        wallpaper="/media/shared/Pictures/fav/new/gruvbox-wallpaper/houses.jpg",
    ),

]

# Drag floating layouts.
mouse = [
    Drag(
        [mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
follow_mouse_focus = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/sh/autostart.sh')
    subprocess.run([home])


@hook.subscribe.startup_complete
def set_screens():
    home = os.path.expanduser('~/.config/qtile/sh/set-screens.sh')
    subprocess.run([home])
