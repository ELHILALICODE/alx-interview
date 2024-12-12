#!/usr/bin/python3
"""
Prime Game module
"""

def is_prime(num):
    """Check if a number is a prime number"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    """Generate a list of prime numbers up to n"""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game

    x: number of rounds
    nums: list of numbers for each round

    Returns:
        Name of the player that won the most rounds, or None if it's a tie
    """
    if not nums or x < 1:
        return None

    maria_score = 0
    ben_score = 0

    for n in nums[:x]:
        primes = generate_primes(n)
        if not primes:
            ben_score += 1
            continue

        turn = 0  # 0 for Maria, 1 for Ben
        while primes:
            # Maria's and Ben's turns alternately
            primes = [p for p in primes if p % primes[0] != 0]
            turn = 1 - turn

        if turn == 1:  # Ben couldn't play
            maria_score += 1
        else:
            ben_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
