"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1
"""


def maxSubArray(nums):

    total_sum = max_sum = nums[0]

    for i in nums[1:]:
        total_sum = max(i, total_sum + i)
        max_sum = max(total_sum, max_sum)
    return max_sum


if __name__ == '__main__':

    a = [-2,1,-3,4,-1,2,1,-5,4]
    b = [1]
    print(maxSubArray(a))
    print(maxSubArray(b))