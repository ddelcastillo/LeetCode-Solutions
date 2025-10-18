from typing import Final

digit_to_chars_dict: Final[dict[str, list[str]]] = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}
digit_to_num_chars_dict: Final[dict[str, int]] = {"2": 3, "3": 3, "4": 3, "5": 3, "6": 3, "7": 4, "8": 3, "9": 4}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        n: int = len(digits)
        number_of_combinations: int = 1
        cum_num_combinations: list[int] = [0] * (n + 1)

        i: int = 0
        j: int = 0
        res: int = 0
        k: int = 0
        combination: str = ""

        for i in range(n):
            number_of_combinations *= digit_to_num_chars_dict[digits[i]]
            cum_num_combinations[i + 1] = number_of_combinations

        combinations: list[str] = [digits or ""] * number_of_combinations if number_of_combinations > 0 else []
        for i in range(number_of_combinations):
            combination = ""
            res = i
            for j in range(n):
                if cum_num_combinations[j] <= i:
                    num_chars: int = digit_to_num_chars_dict[digits[j]]
                    k = res % num_chars
                    res = (res - k) // num_chars
                    combination += digit_to_chars_dict[digits[j]][k]
                else:
                    combination += digit_to_chars_dict[digits[j]][0]
            combinations[i] = combination
        return combinations


if __name__ == "__main__":
    print(Solution().letterCombinations(digits="234"))
