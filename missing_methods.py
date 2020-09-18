'''
I. Missing methods: Two list methods are not listed here. Using the python documentation find out the missing methods and
play with then to figure out what they do. Write two code snippets for each method proving the usefulness of the methods.

II. Write unique_grid with regular 'for' loops:

    unique_grid = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    print(unique_grid)
'''

# I. Missing methods

sports = ['tennis', 'football', 'basketball', 'swimming', 'snowboarding']
years = [1989, 1918, 2020, 2021, 2050, 1900, 1889, 1989, 2010, 2020, 1989]
simple_numbers = list(range(20))

sports.append('tennis')

print('Number of times \'tennis\' appears in the sports list: ', sports.count('tennis'))
num_1989 = years.count(1989)
print('Number of times 1989 appears in the years list: ', num_1989, '\n')

print('List of simple numbers before reversing: ', simple_numbers)
simple_numbers.reverse()
print('Reversed list of simple numbers: ', simple_numbers, '\n')

print('Years list before sorting: ', years)
years.sort()
print('Years list after sorting: ', years)
years.sort(reverse=True)
print('A reversed years list after sorting: ', years, '\n')

print('List of sports before being sorted: ', sports)
print('List of sports after being sorted: ', sorted(sports))
print('List of sports after being sorted by length: ', sorted(sports, key=len))
print('Reversed list of sports after being sorted by length: ', sorted(sports, key=len, reverse=True), '\n')

duplicate_sports = sports.copy()
duplicate_sports.append('formula 1')
print('Copy of the initial sports list, modified to include \'Formula 1\': ', duplicate_sports)
print('Initial sports list: ', sports, '\n')

print('Index position of the first occurrence of \'tennis\' in the sports list copy after index position 2: ', duplicate_sports.index('tennis', 2))
poz_football = duplicate_sports.index('football')
print('Index position of the first occurrence of \'football\' in the sports list copy: ', poz_football, '\n')

from collections import deque
print('Copy of sports list: ', duplicate_sports)
duplicate_sports = deque(duplicate_sports)
duplicate_sports.popleft()
print('Copy of sports list after first element in list has been removed: ', duplicate_sports, '\n')


# II. unique_grid with regular 'for' loops

unique_grid = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print('Original grid:', unique_grid)

new_unique_grid = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            new_unique_grid.append((x, y))
print('New grid with for loops: ', new_unique_grid)
