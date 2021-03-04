"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""


# Brute force
# Time = O(n log n) - Because sort() runs in that time
# Space = O(1)


def missing_number_sorting(nums):
    nums.sort()

    if nums[-1] != len(nums):
        return len(nums)
    elif nums[0] != 0:
        return 0

    for i in range(1, len(nums)):
        expected_num = nums[i-1] + 1
        if nums[i] != expected_num:
            return expected_num


# Hash set
# Time = O(n)
# Space = O(n)


def missing_number_hash(nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number


# Bit Manipulation
# Time = 0(n)
# Space = O(1)

def missing_number_bit(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing
