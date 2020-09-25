'''
Create two sets with 10 numbers each (some of the numbers should be present in both sets).
With these two sets,exemplify the following basic sets operations: union, intersection, difference and symetric difference.
'''


first_set = set(range(50))
second_set = {1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500}
third_set = set(['Hello', 1, 2, 10, 20, 30, 40, 50, 123.456])

union_set = first_set | second_set | third_set
print('A new set with the elements union of the original sets: ', union_set)

intersection_set = first_set & second_set & third_set
print('A set with the common elements of the original sets: ', intersection_set)

difference_set = first_set - second_set - third_set
print('A new set representing the elements of the first set, which are not found in the others (difference): ', difference_set)

symmetric_difference = first_set ^ second_set ^ third_set
print('A set with elements found in either of the given sets, but not in all:', symmetric_difference)