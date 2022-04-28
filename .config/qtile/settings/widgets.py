# MarcosRodrui
# Based on the Configuration of Antonio Sarosi

from libqtile import widget
from .theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        font='UbuntuMono Nerd Font',
        text="",
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        #separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=28,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=3,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(fg = "dark", bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['dark'],
        colour_no_updates=colors['dark'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color3', 'color4'),

    widget.CurrentLayout(**base(bg='color3'), padding=5),

    powerline('color2', 'color3'),

    widget.WidgetBox(**base(bg='color2'), widgets=[
        widget.CPU(**base(bg='color2')),
        widget.TextBox(**base(bg='color2'), text=' '),
        widget.ThermalSensor(**base(bg='color2')),
        widget.TextBox(**base(bg='color2'), text=' ', fontsize='23')],
        text_closed='  ',
        text_open=' ',
        fontsize=23
    ),

    widget.WidgetBox(**base(bg='color2', fg='dark'), widgets=[
        widget.TextBox(**base(bg='color2', fg='dark'), text='MEMORY'),
        widget.Memory(**base(bg='color2', fg='dark')),
        widget.TextBox(**base(bg='color2', fg='dark'), text='  ', fontsize='23')],
        text_closed=' ',
        text_open=' ',
        fontsize=23
    ),


    widget.WidgetBox(**base(bg='color2'), widgets=[
        widget.TextBox(**base(bg='color2'), text='GPU '),
        widget.NvidiaSensors(**base(bg='color2')),
        widget.TextBox(**base(bg='color2'), text='  ', fontsize='23')],
        text_closed=' ',
        text_open=' ',
        fontsize=23
    ),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M:%S'),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
]

widget_defaults = {
    'font': 'Hurmit Nerd Font',
    'fontsize': 16,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
