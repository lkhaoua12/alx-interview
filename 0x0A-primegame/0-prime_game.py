#!/usr/bin/python3
"""Module defining isWinner function."""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def optimal_move(nums):
    # Sort the list of numbers in reverse order
    nums.sort(reverse=True)

    # Iterate through the sorted list
    for num in nums:
        # If the number is prime, return it
        if is_prime(num):
            return num
    # If no prime number is found, return None
    return None


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of prime numbers in the current set
        prime_count = sum(1 for num in range(1, n + 1) if is_prime(num))

        # If there are an odd number of primes, Maria wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the winner based on the number of rounds won
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
