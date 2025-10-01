import curses
from curses import wrapper
from selection import Select

def main(stdscr: curses.window):
    options = [
        {
            "text": "1",
            "action": "do"
        },
        {
            "text": "2",
            "action": "do2"
        }
    ]

    select = Select(options, stdscr)
    select.select()

wrapper(main)