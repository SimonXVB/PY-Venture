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

        self._update()

    def set_options(self, options: list[dict[str, str]]):
        self.options = options
        self._update()
    
    def get_current_selection(self) -> int:
        return self.current_selection

    def select(self):
        """
        Enables selection and returns selected option when ENTER key is hit
        """

        self._update()

        while True:
            input: int = self.stdscr.getch()

            if input == curses.KEY_DOWN:
                if self.current_selection + 1 > len(self.options) - 1:
                    self.current_selection = 0
                else:
                    self.current_selection = self.current_selection + 1

                self._update()
            elif input == curses.KEY_UP:

                if self.current_selection - 1 < 0:
                    self.current_selection = len(self.options) - 1
                else:
                    self.current_selection = self.current_selection - 1

                self._update()
            elif input == curses.KEY_ENTER or input == 10 or input == 13:
                return self.options[self.current_selection]
            

    def _update(self):
        """
        Update selection window
        """

        self.window.clear()

        for i, el in enumerate(self.options):
            prefix = "-> " if i == self.current_selection else "  "

            self.window.addstr(i, 0, prefix + el["text"])

        self.window.refresh()