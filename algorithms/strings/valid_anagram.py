"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""

# Time = O(n log n)
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# Time = 0(n)
# Space = 0(n)... really O(1) because we know that there will be max 26 letters
def isAnagramHash(s: str, t: str) -> bool:
    lib = {}

    for char in s:
        if char not in lib:
            lib[char] = 0
        lib[char] += 1

    for char in t:
        if char not in lib:
            lib[char] = 0
        lib[char] -= 1

    for key in lib.keys():
        if lib[key] != 0:
            return False

    return True




if __name__ == '__main__':

    a = 'anagram'
    b = 'nagaram'
    c = 'coffee'
    d = 'efoefc'

    print(isAnagram(a,b))
    print(isAnagram(c,d))
    print(isAnagramHash(a,b))
    print(isAnagramHash(c,d))