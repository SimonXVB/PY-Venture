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

def main(stdscr: curses.window):
    stdscr.refresh()

    win = curses.newwin(15, 60, 0, 0)
    win.border(0, 0, 0, 0, 0, 0, 0, 0)

    win.refresh()
    curses.curs_set(0)

    textbox = Textbox("Hello")
    select = Select(options, stdscr)

    while True:
        sel = select.select()
        textbox.set_text(sel["text"])

    

wrapper(main)