import curses
from curses import wrapper
from selection import Select

def main(stdscr: curses.window):
    stdscr.refresh()
    curses.curs_set(0)

    options = [
        {
            "text": "1asdhsdjkfhshdfsdf",
            "action": "do"
        },
        {
            "text": "2",
            "action": "do2"
        },
        {
            "text": "3",
            "action": "do3"
        }
    ]

    select = Select(options, stdscr)
    sel = select.select()
    print(sel)

wrapper(main)