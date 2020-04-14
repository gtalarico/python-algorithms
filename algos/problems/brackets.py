from algos.renderer import Rendererable


class BalancedBracked(Rendererable):
    def sort(self, string: str) -> bool:
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
                self.render(string, stack, i)
                continue
            if not (stack and brackets[stack.pop()] == char):
                self.render(string, stack, i, failed=True)
                return False
            self.render(string, stack, i)
        result = not stack
        self.render(string, stack, i, failed=not result)
        return result

    def render(self, string, stack, i, failed=False):
        self.wait(seconds=0.3)

        with self.term.location(x=0, y=0):
            for n, char in enumerate(string):
                if n < i:
                    color = self.term.bold_green
                elif n == i and failed:
                    color = self.term.bold_red
                elif n == i:
                    color = self.term.bold_white
                elif n > i:
                    color = self.term.bold_bright_black
                print(f"{color}{char}", end="")
        with self.term.location(x=0, y=1):
            print(self.term.clear_eol())
            with self.term.location(x=i, y=1):
                print(self.term.bright_blue(f"▲"))

        with self.term.location(y=2, x=0):
            print(self.term.clear_eos())
            s = "".join(stack)
            print(self.term.bright_black(f"Balanced Brackets (i={i} stack= |{s}| )"))
