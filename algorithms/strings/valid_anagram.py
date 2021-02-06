"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def n(s,t):
    print(set(t),set(s))
    return set(s) == set(t)


if __name__ == '__main__':

    a = 'anagram'
    b = 'nagaram'
    c = 'coffee'
    d = 'efoefc'

    print(isAnagram(a,b))
    print(isAnagram(c,d))
    print(n(c,d))