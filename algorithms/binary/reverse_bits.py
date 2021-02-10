"""
Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 
represents the unsigned integer 43261596, so return 964176192 which its binary 
representation is 00111001011110000010100101000000.
"""


def reverseBits(n: int) -> int:
    rep = list("{:032b}".format(n))
    rep.reverse()
    return int(''.join(rep),2)


def reverseBitsBitwise(n: int) -> int:
    output, power = 0, 31
    while n:
        output += (n&1) << power
        n = n >> 1
        power -= 1
    return output