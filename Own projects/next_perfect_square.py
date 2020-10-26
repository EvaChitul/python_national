'''Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.'''

import math

def find_next_square(sq):
    number = int(math.sqrt(sq))
    if number**2 != sq:
        return -1
    else:
        return (number+1)**2


def alternative_next_square(sq):
    return (int(math.sqrt(sq)) + 1)**2 if int(math.sqrt(sq))**2 == sq else -1

print(find_next_square(144))
print(find_next_square(123445))

print(alternative_next_square(16))
print(alternative_next_square(66))

