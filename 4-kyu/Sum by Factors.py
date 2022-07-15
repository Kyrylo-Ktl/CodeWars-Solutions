"""
Kata link:
https://www.codewars.com/kata/54d496788776e49e6b00052f

Description:
Given an array of positive or negative integers

I = [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in
Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]

Solution link:
https://www.codewars.com/kata/reviews/551752caa5808b26460007d6/groups/62d11322cd97700001766ae7
"""

from collections import defaultdict
from math import isqrt


def sum_for_list(numbers: list) -> list:
    factors = defaultdict(int)

    for num in numbers:
        for factor in prime_factors(abs(num)):
            factors[factor] += num

    return sorted(map(list, factors.items()))


def prime_factors(n: int) -> set:
    factors = set()

    for i in range(2, isqrt(n + 1)):
        while not n % i:
            factors.add(i)
            n = n // i

    if n > 2:
        factors.add(n)

    return factors
