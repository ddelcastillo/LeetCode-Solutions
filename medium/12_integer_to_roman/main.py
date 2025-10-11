from typing import Final

integer_to_roman_dict: Final[dict[int, str]] = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
substractive_forms: Final[dict[int, str]] = {900: "CM", 400: "CD", 90: "XC", 40: "XL", 9: "IX", 4: "IV"}
roman_values: Final[list[int]] = [1000, 500, 100, 50, 10, 5, 1]


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_int_raw_string: str = ""
        roman_num_residue: int = num
        roman_num_residue_str: str = str(num)
        for i in range(len(roman_values)):
            if (value := roman_values[i]) > roman_num_residue:
                continue
            else:
                if (lead := roman_num_residue_str[0]) in ("4", "9"):
                    substractive_value: int = int(f"{lead}{'0' * (len(roman_num_residue_str) - 1)}")
                    roman_int_raw_string += substractive_forms.get(substractive_value)
                    roman_num_residue -= substractive_value
                else:
                    q, roman_num_residue = divmod(roman_num_residue, value)
                    roman_int_raw_string += q * integer_to_roman_dict[value]
                roman_num_residue_str = str(roman_num_residue)
        return roman_int_raw_string


if __name__ == "__main__":
    print(Solution().intToRoman(1994))
