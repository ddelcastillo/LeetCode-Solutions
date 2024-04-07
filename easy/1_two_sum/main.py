from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map: dict[int, list[int]] = defaultdict(list)
        for i in range(len(nums)):
            num_map[nums[i]].append(i)
            if idx := num_map.get(target - nums[i]):
                if len(idx) > 1:
                    return idx  # => target = n + n
                if idx[0] != i:  # Avoid same number sum.
                    return [i, idx[0]]
