"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false
"""

def containsDuplicate(nums):
    num_set = set(nums)
    if len(num_set) != len(nums):
        return True
    return False

def containsDuplicateOneLiner(nums):
    return True if len(set(nums)) < len(nums) else False

if __name__ == "__main__":

    a = [1,2,3,4,1]
    b = [1,2,3,4,5]
    print(containsDuplicate(a))
    print(containsDuplicate(b))
    print(containsDuplicateOneLiner(a))
    print(containsDuplicateOneLiner(b))
