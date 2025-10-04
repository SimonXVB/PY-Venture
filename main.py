import curses
from curses import wrapper
from screen import Screen
from textbox import Textbox
from selection import Select
from input import Input

options = [
    {
        "text": "opt1",
        "action": "do1"
    },
    {
        "text": "opt2",
        "action": "do2"
    },
    {
        "text": "opt3",
        "action": "do3"
    }
]

content = r"""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXX(0>XXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXX//\XXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXV_/_XXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

def init_ui():
    """
    Initialize UI
    """

    # Create general UI window
    # 25 Lines, 50 Columns
    wrapper_win = curses.newwin(25, 50, 0, 0)
    text_win = curses.newwin(4, 48, 14, 1)
    interact_win = curses.newwin(7, 48, 17, 1)

    wrapper_win.border(curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK, curses.ACS_BLOCK)
    text_win.border(0, 0, 0, 0, 0, 0, 0, 0)
    interact_win.border(0, 0, curses.ACS_HLINE, 0, curses.ACS_VLINE, curses.ACS_VLINE, 0, 0)
    
    wrapper_win.refresh()
    text_win.refresh()
    interact_win.refresh()

def main(stdscr: curses.window):
    stdscr.refresh()
    curses.curs_set(0)

    init_ui()

    Screen(content)
    tex = Textbox("Hello")
    Select(options, stdscr)
    inp = Input("Test", stdscr)

    while True:
        val = inp.enable_input()
        tex.set_text(val)
wrapper(main)