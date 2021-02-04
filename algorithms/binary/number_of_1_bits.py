"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
"""

# One-liner
def hammingWeightSimple(n: int) -> int:
    return bin(n).count('1')


# Version that uses a Counter object
def hammingWeightCounter(n: int) -> int:
    c = Counter(bin(n)[2:])
    return c['1']


# Removing the right-most '1'
def hammingWeightPop(n: int) -> int:
    result = 0
    while n:
        n = n&(n-1)
        result += 1
    return result

