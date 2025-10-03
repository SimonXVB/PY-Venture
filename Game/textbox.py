import curses

class Textbox:
    def __init__(self, text: str) -> None:
        """
        Initialize and display a new textbox with specified text
        """

        self.text = text
        self.window = curses.newwin(2, 46, 15, 2)

        self._update()

    def set_text(self, text: str):
        self.text = text
        self._update()

    def get_text(self):
        return self.text
    
    def _update(self):
        """
        Update textbox
        """
        self.window.clear()
        self.window.addstr(0, 1, self.text)
        self.window.refresh()