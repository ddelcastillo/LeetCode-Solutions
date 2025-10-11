import logging

logger: logging.Logger = logging.getLogger(name=__name__)
logging.basicConfig(level=logging.INFO)


class Solution:
    def maxArea(self, height: list[int]) -> int:
        n: int = len(height)
        i: int = 0
        j: int = n - 1
        area: int = 0
        max_area: int = 0
        while i <= j:
            if (area := min(height[i], height[j]) * (j - i)) > max_area:
                max_area = area
            if height[j] < height[i]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                if i + 1 < j:
                    if height[i + 1] > height[j - 1]:
                        j -= 1
                    else:
                        i += 1
                else:
                    i += 1  # End of algorithm, continuation condition
        return max_area


if __name__ == "__main__":
    print(Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
