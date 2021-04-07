# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
import subprocess
import socket
import os
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
alt = "mod1"
cntrlR="Control_R"
cntrlL="Control_L"
pgdn="Page_Down"
pgup="Page_Up"
space="sapce"
terminal = 'konsole'

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([alt],"Shift_L",lazy.widget["keyboardlayout"].next_keyboard(),desc="next kbd layout"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -s set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -s set 5%-")),
    Key([alt], "XF86AudioRaiseVolume", lazy.spawn("brightnessctl -s set +5%")),
    Key([alt], "XF86AudioLowerVolume", lazy.spawn("brightnessctl -s set 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("/usr/bin/pulseaudio-ctl mute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("/usr/bin/pulseaudio-ctl up")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("/usr/bin/pulseaudio-ctl down")),
    Key(["control"], pgdn,lazy.next_screen(),desc='Move focus to next monitor'),
    Key(["control"], pgup,lazy.prev_screen(), desc='Move focus to prev monitor'),
]

group_names = [("1: Mail", {'layout': 'monadwide', 'spawn':"thunderbird"}),
               ("2: Comfy", {'layout': 'monadtall'}),
               ("3: Comfy", {'layout': 'monadwide'}),
               ("4: vim", {'layout': 'monadtall'}),
               ("5: Notes", {'layout': 'columns'}),
               ("6: Media", {'layout': 'columns'}),
               ("7: Editing", {'layout': 'columns'}),
               ("8: zoom/teams/discord", {'layout': 'max'}),
               ("9: VM's", {'layout': 'max'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))       # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True)))
  
stdmargin = 15
layouts = [
    layout.Columns(border_focus_stack='#d75f5f',margin=stdmargin),
    layout.Max(margin=stdmargin),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    #layout.Bsp(margin=stdmargin),
    layout.Matrix(margin=stdmargin),
    layout.MonadTall(margin=stdmargin),
    layout.MonadWide(margin=stdmargin),
    #layout.RatioTile(margin=stdmargin),
    #layout.Tile(margin=stdmargin),
    #layout.TreeTab(margin=stdmargin),
    #layout.VerticalTile(margin=stdmargin),
    #layout.Zoomy(margin=stdmargin),
]


floating_layout = layout.Floating()

# vim: tabstop=4 shiftwidth=4 expandtab
@hook.subscribe.client_new
def floating_dialogs(w):
    dialog = w.window.get_wm_type() == 'dialog'
    transient = w.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True
    else:
        namex = w.window.get_name()
        if('kuake' in namex):
            w.floating=True
        elif ('scord' in namex):
            w.floating=True





gruvbox = {
	"fg"	:["#fbf1c7","#ebdbb2","#d5c4a1","#bdae93","#a89984"],
	"bg"	:["#282828","#3c3836","#504945","#665c54","#7c6f64","#1d2021","#32302f"],
	"colors":{
		"red"	:["#cc241d","#fb4934"],
		"green"	:["#98971a","#b8bb26"],
		"yellow":["#d79921","#fabd2f"],
		"blue"	:["#458588","#83a598"],
		"purple":["#b16286","#d3869b"],
		"aqua"	:["#689d6a","#8ec07c"],
		"grey"	:["#a89984","#928374"],
		"orange":["#d65d0e","#fe8019"]
	}
}

widget_defaults = dict(
    font='agave nerd font',
    fontsize=15,
    padding=3,
	background = gruvbox["bg"][0], 
	foreground = gruvbox["fg"][1], 
	inactive = gruvbox["fg"][4],
	active = gruvbox["fg"][0], 
	size_percent = 50
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        wallpaper='/home/josfemova/Pictures/wallpapers/pixel2.jpg',
        wallpaper_mode='fill',
        bottom=bar.Bar(
            [
                widget.CurrentLayout(background=gruvbox["bg"][2]),
                widget.TextBox(text='>',background = gruvbox["bg"][2]),
                widget.TextBox(text='Battery:',background=gruvbox["bg"][1]),
				widget.Battery(
					background = gruvbox["bg"][1],
                    foreground=gruvbox["colors"]["green"][0],
                    low_foreground=gruvbox["colors"]["red"][0],
                    low_percentage=0.3),
                widget.TextBox(text='>',background = gruvbox["bg"][1]),
				widget.TextBox(text='brightness:', background= gruvbox["bg"][2]),
                widget.Backlight(
					background=gruvbox["bg"][2],
					backlight_name='intel_backlight',change_command='brightnessctl s {0}',
					foreground= gruvbox["colors"]["blue"][1]
				),
                widget.TextBox(text='>',background = gruvbox["bg"][2]),
                widget.CurrentScreen(),
                widget.KeyboardLayout(configured_keyboards=['us','latam']),
                widget.GroupBox(),
                widget.Prompt(),
                #widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
				widget.Spacer(background=gruvbox["bg"][0]),
                widget.Clock(
                    format='%a %d/%m/%y %I:%M %p'),
                widget.QuickExit(foreground = gruvbox["colors"]["red"][0]),
                widget.Wlan(interface="wlp2s0"),
                widget.Volume(
                    step=5,
                    volume_app='pacmixer',
                    volume_down_command='/usr/bin/pulseaudio-ctl down',
                    volume_up_command='/usr/bin/pulseaudio-ctl up',
                    mute_commad='/usr/bin/pulseaudio-ctl mute',
                ), 
            ],
            24,
        ),
    ),Screen(
        wallpaper='/home/josfemova/Pictures/wallpapers/pixel2.jpg',
        wallpaper_mode='fill',
        bottom=bar.Bar(
            [
                widget.CurrentLayout(background=gruvbox["bg"][2]),
                widget.TextBox(text='>',background = gruvbox["bg"][2]),
                widget.TextBox(text='Battery:',background=gruvbox["bg"][1]),
				widget.Battery(
					background = gruvbox["bg"][1],
                    foreground=gruvbox["colors"]["green"][0],
                    low_foreground=gruvbox["colors"]["red"][0],
                    low_percentage=0.3),
                widget.TextBox(text='>',background = gruvbox["bg"][1]),
				widget.TextBox(text='brightness:', background= gruvbox["bg"][2]),
                widget.Backlight(
					background=gruvbox["bg"][2],
					backlight_name='intel_backlight',change_command='brightnessctl s {0}',
					foreground= gruvbox["colors"]["blue"][1]
				),
                widget.TextBox(text='>',background = gruvbox["bg"][2]),
                widget.CurrentScreen(),
                widget.KeyboardLayout(configured_keyboards=['us','latam']),
                widget.GroupBox(),
                widget.Prompt(),
                #widget.WindowName(),
                widget.Sep(background = gruvbox["bg"][2]),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
				widget.Spacer(background=gruvbox["bg"][0]),
                widget.Clock(
                    format='%d-%m-%Y %a %I:%M %p'),
                widget.QuickExit(foreground = gruvbox["colors"]["red"][0]),
                widget.Wlan(interface="wlp2s0"),
                widget.Volume(
                    step=5,
                    volume_app='pacmixer',
                    volume_down_command='/usr/bin/pulseaudio-ctl down',
                    volume_up_command='/usr/bin/pulseaudio-ctl up',
                    mute_commad='/usr/bin/pulseaudio-ctl mute',
                ), 
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk         Key([mod], "period",              lazy.next_screen(),              desc='Move focus to next monitor'              ),          Key([mod], "comma",              lazy.prev_screen(),              desc='Move focus to prev monitor'              ),
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

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
def start_once():
	processes = [
		['setxkbmap', '-option', 'caps:escape'],['picom'],['yakuake']]
	for p in processes:
		subprocess.Popen(p)
