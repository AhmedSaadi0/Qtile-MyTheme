from libqtile import widget


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
