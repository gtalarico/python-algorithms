from typing import List
from algos.renderer import Rendererable


class Bubble(Rendererable):
    """
    Bubble

    Complexity: N*N / N
    Type: In Place
    Stable: Yes

    https://www.youtube.com/watch?v=xWBP4lzkoyM&feature=emb_title
    """

    def sort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 1):
            swapped = False
            for j in range(0, n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    self.render(arr, i, j, swapped=True)
                else:
                    self.render(arr, i, j, swapped=False)
            if not swapped:
                break
        self.render(arr, i, j, done=True)
        return arr

    def render(self, arr, i, j, swapped=False, done=False):
        self.wait()

        for n, value in enumerate(arr):
            bar = f"\t{value * '▆'}"

            with self.term.location(x=0, y=n):
                print(self.term.clear_eol())

            with self.term.location(x=0, y=n):
                if done:
                    print(self.term.green(f"✓{bar}"))
                elif swapped and n == j:
                    print(self.term.bold_red(f"j{bar}"))
                elif swapped and n == j + 1:
                    print(self.term.bold_blue(f"▲{bar}"))
                elif n == j:
                    print(self.term.bold_blue(f"j{bar}"))
                elif n == i:
                    print(self.term.green(f"i{bar}"))
                elif n <= i:
                    print(self.term.green(f"{bar}"))
                else:
                    print(self.term.bold_white(f"{bar}"))

        with self.term.location(y=len(arr), x=0):
            print(self.term.clear_eos())
            print(self.term.bright_black(f"Bubble Sort (i={i} swapped={swapped})"))
