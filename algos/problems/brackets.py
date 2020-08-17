import time


class BalancedBracked:

    DEFAULT_FRAME_SPEED = 0.3

    def __init__(self, renderer, speed=None):
        self.renderer = renderer
        self.frame_speed = speed if speed is not None else self.DEFAULT_FRAME_SPEED

    def run(self, string: str) -> bool:
        """
        Balanced Brackets

        Time Complexity: n
        Space Complexity: n
        """
        brackets = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for i, char in enumerate(string):
            if char in brackets.keys():
                stack.append(char)
                self.render_frame(string, stack, i)
                continue
            if not (stack and brackets[stack.pop()] == char):
                self.render_frame(string, stack, i, failed=True)
                return False
            self.render_frame(string, stack, i)
        result = not stack
        self.render_frame(string, stack, i, failed=not result)
        return result

    def render_frame(self, string, stack, i, failed=False):
        time.sleep(self.frame_speed)

        with self.renderer.term.location(x=0, y=0):
            for n, char in enumerate(string):
                if n < i:
                    color = self.renderer.term.bold_green
                elif n == i and failed:
                    color = self.renderer.term.bold_red
                elif n == i:
                    color = self.renderer.term.bold_white
                elif n > i:
                    color = self.renderer.term.bold_bright_black
                print(f"{color}{char}", end="")
        with self.renderer.term.location(x=0, y=1):
            print(self.renderer.term.clear_eol())
            with self.renderer.term.location(x=i, y=1):
                print(self.renderer.term.bright_blue(f"▲"))

        with self.renderer.term.location(y=2, x=0):
            print(self.renderer.term.clear_eos())
            s = "".join(stack)
            print(
                self.renderer.term.bright_black(
                    f"Balanced Brackets (i={i} stack= '{s}' )"
                )
            )
