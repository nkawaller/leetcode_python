"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


def maxProfit(prices):
    if prices == []:
        return 0
    buy = prices[0]
    max_profit = 0

    for i in range(1,len(prices)):
        profit = prices[i] - buy
        if profit > max_profit:
            max_profit = profit
        if buy > prices[i]:
            buy = prices[i]

    return max_profit


def maxProfit2(prices):
    n = len(prices)
    if n < 2:
        return 0
    max_profit, min_stock = float('-inf'), prices[0]
    for p in prices:
        max_profit = max(max_profit, p - min_stock)
        min_stock = min(min_stock, p)
    return max_profit

a = [7,1,5,3,6,4]
b = [7,6,4,3,1]

print(maxProfit(a))
print(maxProfit(b))
