"""
Kata link:
https://www.codewars.com/kata/53f40dff5f9d31b813000774

Description:
There is a secret string which is unknown to you. Given a collection of random triplets from the string,
recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before
the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that
they contain sufficient information to deduce the original string. In particular, this means that
the secret string will never contain letters that do not occur in one of the triplets given to you.

Solution link:
https://www.codewars.com/kata/reviews/53fbcb9ecfc5f67703000032/groups/62c86258b41bde000112e995
"""

from functools import lru_cache


def recoverSecret(triplets: list) -> str:
    # Initially, the letters are not ordered relative to each other
    graph = {ltr: set() for trip in triplets for ltr in trip}

    # If there is an edge from U to V then U comes after V
    for a, b, c in triplets:
        graph[b].add(a)
        graph[c].add(b)

    # The number of preceding letters is equal to the number of reachable vertices
    @lru_cache(maxsize=None)
    def previous_count(v: int) -> int:
        if not graph[v]:
            return 0
        return max(previous_count(u) for u in graph[v]) + 1

    # Letters are sorted according to the number of letters that come before them
    return ''.join(sorted(graph, key=previous_count))
