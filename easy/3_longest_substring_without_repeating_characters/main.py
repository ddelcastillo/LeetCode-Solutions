class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, left, right, chars = 0, 0, 0, set()
        for right in range(len(s)):
            if (char := s[right]) not in chars:
                chars.add(char)
                max_length = max(max_length, right - left + 1)
            else:
                while (char := s[left]) != s[right]:  # Slide the window
                    chars.remove(char)
                    left += 1
                chars.remove(char)
                left += 1
                chars.add(s[right])
        return max_length
