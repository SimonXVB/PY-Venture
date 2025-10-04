import curses

class Select: 
    def __init__(self, options: list[dict[str, str]], stdscr: curses.window) -> None:
        """
        Initialize and display a new selection instance with specified options
        """

        self.stdscr = stdscr
        self.window = curses.newwin(5, 46, 18, 2)
        self.options: list[dict[str, str]] = options
        self.current_selection = 0

    def set_options(self, options: list[dict[str, str]]):
        self.options = options
        self.update()
    
    def get_current_selection(self) -> int:
        return self.current_selection

    def enable_selection(self):
        """
        Enables and displays selection window. 
        Returns selected option when ENTER key is pressed.
        """

        self.update()

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
            elif input == 10 or input == 13:
                return self.options[self.current_selection]
            
    def hide_selection(self):
        self.window.clear()
        self.window.refresh()

    def update(self):
        """
        Update selection window
        """

        self.window.clear()

        for i, el in enumerate(self.options):
            prefix = "-> " if i == self.current_selection else "  "

            self.window.addstr(i, 0, prefix + el["text"])

        self.window.refresh()