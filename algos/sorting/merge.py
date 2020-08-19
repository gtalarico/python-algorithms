from typing import List
import time


class MergeSort:
    """
    Merge Sort

    Complexity:
    Type:
    Stable: No

    https://
    """

    DEFAULT_FRAME_SPEED = 0.1

    def __init__(self, renderer, speed=None):
        self.renderer = renderer
        self.frame_speed = speed if speed is not None else self.DEFAULT_FRAME_SPEED

    def sort(self, arr: List[int], r_offset=0, level=0) -> List[int]:
        def merge_arrays(arr1, arr2):
            merged_array = []
            while len(arr1) > 0 and len(arr2) > 0:
                if arr1[0] < arr2[0]:
                    merged_array.append(arr1[0])
                    arr1.pop(0)
                else:
                    merged_array.append(arr2[0])
                    arr2.pop(0)
            for i in arr1 + arr2:
                merged_array.append(i)

            return merged_array

        # Only here if first call
        if r_offset == 0:
            self.render_frame(arr, offset=0, initial=True, level=level, sorted=False)

        arr_len = len(arr)
        if arr_len > 1:
            mid_index = arr_len // 2
            L, R = arr[:mid_index], arr[mid_index:]
            sorted_left = self.sort(L, r_offset=r_offset, level=level + 1)
            sorted_right = self.sort(R, r_offset=r_offset + mid_index, level=level + 1)
            sorted_array = merge_arrays(sorted_left, sorted_right)

            self.render_frame(sorted_array, offset=r_offset, level=level, sorted=True)

        else:
            self.render_frame(arr, offset=r_offset, level=level, sorted=False)
            return arr

        # Only print final one at end
        if r_offset == 0:
            self.render_frame(sorted_array, offset=0, sorted=True)
        return sorted_array

    def render_frame(self, arr, offset, initial=False, level=0, sorted=False):
        time.sleep(self.frame_speed)
        if initial:
            time.sleep(self.frame_speed * 2)
        # print(self.renderer.term.clear())

        for n, value in enumerate(arr):
            n = n + offset
            bar = f"\t {value * '▆'}"
            with self.renderer.term.location(x=0, y=n):
                print(self.renderer.term.clear_eol())

            with self.renderer.term.location(x=0, y=n):
                if initial:
                    print(self.renderer.term.dimgray(f"{bar}"))
                elif len(arr) == 1:
                    print(self.renderer.term.bold_red(f"{level}{bar}"))
                elif len(arr) == 2:
                    print(self.renderer.term.bold_yellow(f"{level}{bar}"))
                elif sorted and level != 0:
                    print(self.renderer.term.green(f"{bar}"))
                elif sorted:
                    print(self.renderer.term.green(f"✓{bar}"))
                else:
                    print(self.renderer.term.bold_white(f"{bar}"))

        # if initial:
        with self.renderer.term.location(x=0, y=offset + len(arr)):
            print(self.renderer.term.clear_eos())
            print(
                self.renderer.term.bright_black(
                    f"Selection Sort (level={level} len={len(arr)} offset={offset})"
                )
            )
