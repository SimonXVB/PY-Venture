import curses
from curses import wrapper
from selection import Select
from textbox import Textbox

def main(stdscr: curses.window):
    stdscr.refresh()
    stdscr.scrollok(True)
    curses.curs_set(0)

    options = [
        {
            "text": "1asdhsdjkfhshdfsdfgdfghdkfh",
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

    textbox = Textbox(stdscr, "Hello")
    select = Select(options, stdscr)

    while True:
        sel = select.select()
        textbox.set_text(sel["text"])
    

wrapper(main)