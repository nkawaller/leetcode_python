"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

def isPalindrome(s: str) -> bool:
    result = ''
    s = s.lower()
    for i in s:
        if i.isalnum():
            result += i
    return result == result[::-1]

if __name__ == '__main__':

    a = "A man, a plan, a canal: Panama"
    b = "race a car"
    print(isPalindrome(a))
    print(isPalindrome(b))