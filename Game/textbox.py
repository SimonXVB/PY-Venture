import curses

class Textbox:
    def __init__(self, stdscr: curses.window, text: str) -> None:
        self.text = text
        self.stdscr = stdscr
        self.window = curses.newwin(3, len(self.text) + 4, 0, 0)

        self.update()

    def set_text(self, text: str):
        self.text = text
        self.update()

    def get_text(self):
        return self.text
    
    def update(self):
        """
        Update textbox
        """
        self.window.erase()
        self.window.refresh()

        self.window.resize(3, len(self.text) + 4)

        self.window.addstr(1, 2, self.text)
        self.window.border(0, 0, 0, 0, 0, 0, 0, 0)
    
        self.window.refresh()