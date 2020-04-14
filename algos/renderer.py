from unittest import mock
from blessed import Terminal
import time


class Rendererable:
    DEFAULT_FRAME_SPEED = 0.1

    def __init__(self, render=True, speed=None):
        self.term = Terminal()
        self.FRAME_SPEED = speed or self.DEFAULT_FRAME_SPEED
        if not render:
            self.render = mock.MagicMock()

    def animate(self, arr):
        try:
            self.term.fullscreen()
            with self.term.cbreak(), self.term.hidden_cursor():
                print(self.term.clear())
                self.sort(arr)
                with self.term.location(y=self.term.height - 2, x=0):
                    print(self.term.black_on_white(" press any key to exit "))
                    val = ""
                    while val == "":
                        val = self.term.inkey(timeout=3)

            self.term.exit_fullscreen()
            print(self.term.clear())
        except Exception as exc:
            # Exit Fullscreen before raise to capture traceback
            self.term.exit_fullscreen()
            raise exc

    def wait(self, seconds=None):
        seconds = seconds or self.FRAME_SPEED
        time.sleep(seconds)
