from unittest import mock
from blessed import Terminal
import time


class ConsoleRenderer:
    def __init__(self, speed=None, terminal=None):
        # Use ConsoleRenderer(terminal=MagicMock) to mock
        self.term = terminal or Terminal()

    def _init(self):
        _console_config_init = (
            self.term.fullscreen(),
            self.term.cbreak(),
            self.term.hidden_cursor(),
        )
        # HACK: Because this functions are meant to be used as with ctx managers
        self.ctx_generators = [
            ctx_mgr.func(self.term) for ctx_mgr in _console_config_init
        ]
        [next(i) for i in self.ctx_generators]

    def _terminate(self):
        for gen in self.ctx_generators:
            try:
                next(gen)
            except StopIteration:
                pass

    def __enter__(self):
        self._init()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if not exc_type:
            with self.term.location(y=self.term.height - 2, x=0):
                print(self.term.black_on_white(" press any key to exit "))
                val = ""
                while val == "":
                    val = self.term.inkey(timeout=3)
            self._terminate()
        else:
            # Exit Fullscreen before return which will raise traceback
            print(self.term.clear())
            self._terminate()
