from typing import List
import time


class Insertion:
    """
    Insertion

    Complexity: n * n / n
    Type: In Place
    Stable: Yes

    https://www.youtube.com/watch?v=OGzPmgsI-pQ&feature=emb_title
    """

    DEFAULT_FRAME_SPEED = 0.1

    def __init__(self, renderer, speed=None):
        self.renderer = renderer
        self.frame_speed = speed if speed is not None else self.DEFAULT_FRAME_SPEED

    def sort(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for key in range(1, n):

            i = key  # tracks item down as it swaps its way down to the correct position
            j = key - 1  # tracks index of numbers it's comparing i to
            while j >= 0:
                should_swap = arr[i] < arr[j]
                if should_swap:
                    arr[i], arr[j] = arr[j], arr[i]
                    i -= 1
                else:
                    j -= 1
                self.render_frame(arr, key, i, j, swapped=should_swap)

        self.render_frame(arr, key, i, j, done=True)
        return arr

    def render_frame(self, arr, key, i, j, swapped=False, done=False):
        time.sleep(self.frame_speed)

        for n, value in enumerate(arr):
            bar = f"\t{value * '▆'}"
            with self.renderer.term.location(x=0, y=n):
                print(self.renderer.term.clear_eol())

            swapped
            with self.renderer.term.location(x=0, y=n):
                if done:
                    print(self.renderer.term.green(f"✓{bar}"))
                elif swapped and (n == i or n == j):
                    print(self.renderer.term.bold_red(f"▲{bar}"))
                elif n == j:
                    print(self.renderer.term.bold_yellow(f" {bar}"))
                elif n == key:
                    print(self.renderer.term.bold_blue(f"K {bar}"))
                elif n < key:
                    print(self.renderer.term.green(f"✓{bar}"))
                else:
                    print(self.renderer.term.bold_white(f" {bar}"))

        with self.renderer.term.location(y=len(arr), x=0):
            print(self.renderer.term.clear_eos())
            print(
                self.renderer.term.bright_black(
                    f"Insertion Sort (k={key} i={i} j={j} swapped={swapped})"
                )
            )
