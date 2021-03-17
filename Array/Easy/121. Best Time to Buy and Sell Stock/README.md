# 121. Best Time to Buy and Sell Stock

## Problem Statement

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Challenges

To find the maximum peak after the minimum valley.

## Solution Explained

1. Initialise `max_profit = 0` and `min_price = prices[0]`
2. Iterate through the array and find the profit for each element, `prices[i] - min_price`.
3. If the profit for the current element is larger than the previous greatest profit then it is the maximum profit now.
4. If the current price is smaller than the current minimum price then the current element is now the minimum price.
