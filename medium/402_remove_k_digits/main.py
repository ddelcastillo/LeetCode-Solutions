class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        return self.solve_3(num, k)

    def solve_1(self, num: str, k: int) -> str:
        """Naive approach, terribly optimized, requires parsing huge integer strings to integer, which
        requires modifying Python's int max str digits. About T = O(k^n), death.
        """
        if k <= 0:
            return num
        results = [self.solve_1(num[:i] + num[i + 1 :], k - 1) for i in range(len(num))]
        return str(min(int(x) for x in results))

    @staticmethod
    def solve_2(num: str, k: int) -> str:
        """So this approach comes after I learned about the Monotonic Stack data structure and its algorithm. The idea
        is that the algorithm is greedy and doesn't care about the digits to the right, since you want the larger
        value representations to be minimized (e.g., thousands, millions, over tenths).
        """
        stack: list[str] = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:  # Increasing monotonic stack.
                k -= 1
                stack.pop()
            if stack or digit != "0":
                stack.append(digit)
        result: str = "".join(stack)
        if k > 0:  # If number is digit monotonic but still can remove digits
            result = result[: len(result) - k]
        return result or "0"

    @staticmethod
    def solve_3(num: str, k: int) -> str:
        """This is the same implementation as solve_2 but with a couple optimizations: 1) it's actually not necessary
        to check for 0s as the greedy algorithm simply will not pop anything and the string can be stripped of 0s.
        """
        stack: list[str] = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:  # Increasing monotonic stack.
                k -= 1
                stack.pop()
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        result: str = "".join(stack).lstrip("0")
        return result or "0"
