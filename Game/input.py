import curses

class Input:
    def __init__(self, title: str, stdscr: curses.window) -> None:
        self.stdscr = stdscr
        self.window = curses.newwin(5, 46, 18, 2)
        self.title = title
        self.input: list[int] = []

        self.update()

    def set_title(self, title: str):
        self.title = title

    def enable_input(self):
        """
        Enables and displays input window. 
        Returns input when ENTER key is pressed.
        """
        curses.curs_set(1)

        while True:
            input: int = self.stdscr.getch()

            if input == 10 or input == 13:                      #Enter key
                return "".join([chr(i) for i in self.input])
            elif input == 8 or input == 127:                    #Backspace key
                if len(self.input) > 0:
                    self.input.pop()
                    self.update()
            elif input <= 255:
                if len(self.input) <= 44:
                    self.input.append(input)
                    self.update()

    def clear_input(self):
        self.input = []
        self.update()

    def hide_input(self):
        curses.curs_set(0)

        self.window.clear()
        self.window.refresh()

    def update(self):
        """
        Update input window
        """

        self.window.clear()

        self.window.addstr(self.title + ":\n") #Draw title
        self.window.addstr("".join([chr(i) for i in self.input])) #Draw content

        self.stdscr.move(self.window.getbegyx()[0] + 1, self.window.getbegyx()[1] + len(self.input)) #Move cursor next to content

        self.window.refresh()