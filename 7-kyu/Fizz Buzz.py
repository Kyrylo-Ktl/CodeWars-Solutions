"""
Kata link:
https://www.codewars.com/kata/5300901726d12b80e8000498

Description:
Return an array containing the numbers from 1 to N, where N is the parametered value.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value "Fizz" instead
If the value is a multiple of 5: use the value "Buzz" instead
If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
N will never be less than 1.

Example:
fizzbuzz(10) --> [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz']

Solution link:
https://www.codewars.com/kata/reviews/54908a45efb5978ccc000127/groups/62d06a0d9dd4d700018e2767
"""


def fizzbuzz(n: int) -> list:
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i for i in range(1, n + 1)]
