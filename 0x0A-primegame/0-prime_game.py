#!/usr/bin/python3
"""
Defines a Prime game
"""
def isWinner(x, nums):
    """
    Evaluates the winner of a prime game session within x rounds of play
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    wins = {'Maria': 0, 'Ben': 0}
    for _ in range(x):
        primes = [i for i in nums if is_prime(i)]
        if not primes:
            wins[['Maria', 'Ben'][_ % 2]] += 1
        else:
            nums.remove(primes[0])

    return max(wins, key=wins.get) if wins['Maria'] > wins['Ben'] else ('Ben' if wins['Maria'] < wins['Ben'] else None)