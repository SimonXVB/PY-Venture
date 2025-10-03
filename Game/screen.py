import curses

class Screen:
    def __init__(self, content: str) -> None:
        self.window = curses.newwin(13, 47, 1, 2)
        self.content: str = content

        self.update()

    def set_content(self, content: str):
        self.content = content
        self.update()

    def update(self):
        """
        Update screen window
        """

        self.window.clear()
        self.window.addstr(0, 0, self.content)
        self.window.refresh()