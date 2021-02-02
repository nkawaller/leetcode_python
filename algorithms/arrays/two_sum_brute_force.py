"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

def two_sum_brute_force(arr, target):
    for i in range(0,len(arr)-1):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return 'No match'


def two_sum_hash(arr, target):
    dictionary = {}
    for index, value in enumerate(arr):
        if (target-value) in dictionary:
            return [dictionary[target-value], index]
        else:
            dictionary[value] = index


if __name__ == '__main__':

    a = [1,2,3,4]
    print(two_sum_brute_force(a,7))
    print(two_sum_brute_force(a,8))
    print(two_sum_hash(a,3))
    print(two_sum_hash(a,7))
    print(two_sum_hash(a,8))