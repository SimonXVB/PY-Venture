import curses
from curses import wrapper
from selection import Select
from textbox import Textbox

options = [
    {
        "text": "opt1",
        "action": "do"
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

    textbox = Textbox("Hello")
    select = Select(options, stdscr)

    while True:
        sel = select.select()
        textbox.set_text(sel["text"])
wrapper(main)