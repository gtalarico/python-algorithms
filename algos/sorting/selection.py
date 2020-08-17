from typing import List
import time


class Selection:
    """
    Selection Sort

    Complexity: N*N / N*N
    Type: In Place
    Stable: No

    https://www.youtube.com/watch?v=xWBP4lzkoyM&feature=emb_title
    """

    DEFAULT_FRAME_SPEED = 0.1

    def __init__(self, renderer, speed=None):
        self.renderer = renderer
        self.frame_speed = speed if speed is not None else self.DEFAULT_FRAME_SPEED

    def sort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(0, n - 1, +1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
                self.render_frame(arr, i, j, min_index)
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

        self.render_frame(arr, i, j, min_index, done=True)
        return arr

    def render_frame(self, arr, i, j, min_index, done=False):
        time.sleep(self.frame_speed)
        for n, value in enumerate(arr):
            bar = f"\t {value * '▆'}"
            with self.renderer.term.location(x=0, y=n):
                print(self.renderer.term.clear_eol())
            with self.renderer.term.location(x=0, y=n):
                if n < i or done:
                    color, symbol = self.renderer.term.green, "✓"
                elif n == min_index:
                    color, symbol = self.renderer.term.bold_red, "min"
                elif n == i:
                    color, symbol = self.renderer.term.bold_yellow, "i"
                elif n == j:
                    color, symbol = self.renderer.term.bold_blue, "j"
                else:
                    color, symbol = self.renderer.term.bold_white, ""
                print(f"{color} {symbol} {bar}")
        with self.renderer.term.location(y=len(arr), x=0):
            print(self.renderer.term.clear_eos())
            print(
                self.renderer.term.bright_black(
                    f"Selection Sort (i={i} j={j} min={min_index})"
                )
            )
