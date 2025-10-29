from typing import Final
from collections import defaultdict
import string

LETTER_TO_NUM_DICT: Final[dict[str, int]] = {
    "a": 2,
    "b": 3,
    "c": 5,
    "d": 7,
    "e": 11,
    "f": 13,
    "g": 17,
    "h": 19,
    "i": 23,
    "j": 29,
    "k": 31,
    "l": 37,
    "m": 41,
    "n": 43,
    "o": 47,
    "p": 53,
    "q": 59,
    "r": 61,
    "s": 67,
    "t": 71,
    "u": 73,
    "v": 79,
    "w": 83,
    "x": 89,
    "y": 97,
    "z": 101,
}


class Solution:
    def _generate_prime_sieve(self, n: int) -> list[int]:
        if n < 2:
            return []
        is_prime: list[bool] = [True] * (n + 1)
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
        return [i for i in range(2, n + 1) if is_prime[i]]

    def _multiply_list(self, values: list[int]) -> int:
        prod: int = 1
        for value in values:
            prod *= value
        return prod

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups_dict: dict[int, list[str]] = defaultdict(list)
        value: int = 0
        for word in strs:
            anagram_groups_dict[self._multiply_list(LETTER_TO_NUM_DICT[i] for i in word)].append(word)
        return list(anagram_groups_dict.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
