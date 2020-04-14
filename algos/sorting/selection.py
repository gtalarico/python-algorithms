from typing import List
from algos.renderer import Rendererable


class Selection(Rendererable):
    """
    Selection Sort

    Complexity: N*N / N*N
    Type: In Place
    Stable: No

    https://www.youtube.com/watch?v=xWBP4lzkoyM&feature=emb_title
    """

    def sort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(0, n - 1, +1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
                self.render(arr, i, j, min_index)
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

        self.render(arr, i, j, min_index, done=True)
        return arr

    def render(self, arr, i, j, min_index, done=False):
        self.wait()
        for n, value in enumerate(arr):
            bar = f"\t {value * '▆'}"
            with self.term.location(x=0, y=n):
                print(self.term.clear_eol())
            with self.term.location(x=0, y=n):
                if n < i or done:
                    color, symbol = self.term.green, "✓"
                elif n == min_index:
                    color, symbol = self.term.bold_red, "min"
                elif n == i:
                    color, symbol = self.term.bold_yellow, "i"
                elif n == j:
                    color, symbol = self.term.bold_blue, "j"
                else:
                    color, symbol = self.term.bold_white, ""
                print(f"{color} {symbol} {bar}")
        with self.term.location(y=len(arr), x=0):
            print(self.term.clear_eos())
            print(
                self.term.bright_black(f"Selection Sort (i={i} j={j} min={min_index})")
            )
