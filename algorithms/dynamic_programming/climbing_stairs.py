"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climbStairs(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    result = [0] * (n+1)
    result[0:3] = [0,1,2]

    for i in range(3, n+1):
        result[i] = result[i-1] + result[i-2]
    
    return result[n]


if __name__ == '__main__':

    print(climbStairs(5))
    print(climbStairs(6))
