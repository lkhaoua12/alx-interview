#!/usr/bin/python3
'''
Calculates the fewest number of operations needed to result in n H characters
'''


def minOperations(n):
    """
    a method that calculates the fewest number of operations
    needed to result in exactly n H
    """
    num_of_operations = 0
    min_operations = 2

    while n > 1:
        if (n % min_operations == 0):
            num_of_operations += min_operations
            n = n / min_operations
        else:
            min_operations += 1
    return num_of_operations
