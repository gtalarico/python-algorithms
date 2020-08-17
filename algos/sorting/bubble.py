from typing import List
import time


class Bubble:
    """
    Bubble

    Complexity: N*N / N
    Type: In Place
    Stable: Yes

    https://www.youtube.com/watch?v=xWBP4lzkoyM&feature=emb_title
    """

    DEFAULT_FRAME_SPEED = 0.1

    def __init__(self, renderer, speed=None):
        self.renderer = renderer
        self.frame_speed = speed if speed is not None else self.DEFAULT_FRAME_SPEED

    def sort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 1):
            swapped = False
            for j in range(0, n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    self.render_frame(arr, i, j, swapped=True)
                else:
                    self.render_frame(arr, i, j, swapped=False)
            if not swapped:
                break
        self.render_frame(arr, i, j, done=True)
        return arr

    def render_frame(self, arr, i, j, swapped=False, done=False):
        time.sleep(self.frame_speed)

        for n, value in enumerate(arr):
            bar = f"\t{value * '▆'}"
            with self.renderer.term.location(x=0, y=n):
                print(self.renderer.term.clear_eol())

            with self.renderer.term.location(x=0, y=n):
                if done:
                    print(self.renderer.term.green(f"✓{bar}"))
                elif swapped and n == j:
                    print(self.renderer.term.bold_red(f"j{bar}"))
                elif swapped and n == j + 1:
                    print(self.renderer.term.bold_blue(f"▲{bar}"))
                elif n == j:
                    print(self.renderer.term.bold_blue(f"j{bar}"))
                elif n == i:
                    print(self.renderer.term.green(f"i{bar}"))
                elif n <= i:
                    print(self.renderer.term.green(f"{bar}"))
                else:
                    print(self.renderer.term.bold_white(f"{bar}"))

        with self.renderer.term.location(y=len(arr), x=0):
            print(self.renderer.term.clear_eos())
            print(
                self.renderer.term.bright_black(
                    f"Bubble Sort (i={i} swapped={swapped})"
                )
            )
