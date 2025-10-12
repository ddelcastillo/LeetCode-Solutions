from typing import Final

roman_to_int_dict: Final[dict[str, int]] = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


class Solution:
    def romanToInt(self, s: str) -> int:
        n: int = len(s)
        if not s:
            return 0
        if n == 1:
            return roman_to_int_dict.get(s)
        final_val: int = 0
        i: int = 0
        while i < n:
            roman_val: int = roman_to_int_dict[s[i]]
            if i + 1 < n:
                if (next_roman_val := roman_to_int_dict[s[i + 1]]) > roman_val:
                    final_val += next_roman_val - roman_val
                    i += 1
                else:
                    final_val += roman_val
            else:
                final_val += roman_val
            i += 1

        return final_val


if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))
