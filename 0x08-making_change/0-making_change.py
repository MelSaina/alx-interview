#!/usr/bin/python3
"""
Defines a make change function
"""
def makeChange(coins, total):
    """
    Minium coins required
    """
    if total < 1:
        return 0

    # Initialize an array to store the minimum number of coins for each value from 0 to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate over each coin value and update the min_coins array
    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1