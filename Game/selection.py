import curses

class Select: 
    def __init__(self, options: list[dict[str, str]], stdscr: curses.window) -> None:
        """
        Initialize a new selection instance with specified options
        """

        self.options: list[dict[str, str]] = options
        self.stdscr = stdscr
        self.current_selection = 0

    def set_options(self, options: list[dict[str, str]]):
        self.options = options
    
    def get_current_selection(self) -> int:
        return self.current_selection

    def select(self):
        """
        Outputs a selection interface and returns selected option when ENTER key is hit
        """

        while True:
            input: int = self.stdscr.getch()

            if input == curses.KEY_DOWN:
                if self.current_selection + 1 > len(self.options) - 1:
                    self.current_selection = 0
                else:
                    self.current_selection = self.current_selection + 1

                self.update()
            elif input == curses.KEY_UP:
                if self.current_selection - 1 < 0:
                    self.current_selection = len(self.options) - 1
                else:
                    self.current_selection = self.current_selection - 1

                self.update()
            elif input == curses.KEY_ENTER or input == 10 or input == 13:
                return self.options[self.current_selection]
            

    def update(self):
        """
        Update selection window
        """

        self.stdscr.clear()

        for i, el in enumerate(self.options):
            if i == self.current_selection:
                self.stdscr.addstr("* " + el["text"] + "\n")
            else:
                self.stdscr.addstr("  " + el["text"] + "\n")