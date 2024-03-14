def isWinner(x, nums):
    """
    Evaluates the winner of a prime game session within x rounds of play
    """
    if x < 1 or not nums:
        return None
    mariasWins, bensWins = 0, 0
    for n in nums:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        primesCount = sum(1 for i in range(2, n + 1) if primes[i])
        bensWins += primesCount % 2 == 0
        mariasWins += primesCount % 2 == 1
    if mariasWins == bensWins:
        return None
    return 'Maria' if mariasWins > bensWins else 'Ben'