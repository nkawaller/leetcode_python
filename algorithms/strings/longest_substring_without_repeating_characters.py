"""
Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Time: O(n)
Space: O(n)
"""

def lengthOfLongestSubstring(s: str) -> int:
    result = 0
    char_set = set()
    left_pointer = 0
    for right_pointer in range(len(s)):
        while s[right_pointer] in char_set:
            char_set.remove(s[left_pointer])
            left_pointer += 1
        char_set.add(s[right_pointer])
        result = max(result, right_pointer - left_pointer + 1)
    return result