from typing import List
import time


class Insertion:
    """
    Insertion

    Complexity:
    Type: In Place
    Stable: Yes

    https://www.youtube.com/watch?v=OGzPmgsI-pQ&feature=emb_title
    """

    DEFAULT_FRAME_SPEED = 0.1

    def __init__(self, renderer, speed=None):
        self.renderer = renderer
        self.frame_speed = speed if speed is not None else self.DEFAULT_FRAME_SPEED

    def sort(self, arr: List[int]) -> List[int]:
        """
        K:      1
        A: [ 3, 1, 2, 7 ]
        """
        n = len(arr)
        key = 1  # Where  k = sorted sublist key

        while key < n:
            i = key - 1
            subkey = key
            while i >= 0:
                if arr[subkey] < arr[i]:
                    arr[subkey], arr[i] = arr[i], arr[subkey]
                    subkey = i
                    i -= 1
                    swapped = True
                else:
                    i -= 1
                    swapped = False
                self.render_frame(arr, key, subkey, i, swapped=swapped)
            key += 1

        self.render_frame(arr, key, subkey, i, done=True)
        return arr

    def render_frame(self, arr, key, subkey, i, swapped=False, done=False):
        time.sleep(self.frame_speed)

        for n, value in enumerate(arr):
            bar = f"\t{value * '▆'}"
            with self.renderer.term.location(x=0, y=n):
                print(self.renderer.term.clear_eol())

            swapped
            with self.renderer.term.location(x=0, y=n):
                if done:
                    print(self.renderer.term.green(f"✓{bar}"))
                elif swapped and n == subkey:
                    print(self.renderer.term.bold_red(f" {bar}"))
                elif not swapped and n == subkey:
                    print(self.renderer.term.bold_blue(f" {bar}"))
                elif n < key:
                    print(self.renderer.term.green(f"✓{bar}"))
                elif n == i:
                    print(self.renderer.term.bold_ref(f" {bar}"))
                elif n == key:
                    print(self.renderer.term.bold_blue(f"K {bar}"))
                else:
                    print(self.renderer.term.bold_white(f" {bar}"))

        with self.renderer.term.location(y=len(arr), x=0):
            print(self.renderer.term.clear_eos())
            print(
                self.renderer.term.bright_black(
                    f"Insertion Sort (k={key} subkey={subkey} i={i} swapped={swapped})"
                )
            )
