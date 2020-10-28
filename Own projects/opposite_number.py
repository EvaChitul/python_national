'''given a number, find its opposite.'''

def opposite(number):
  if number < 0:
      return abs(number)
  else:
      return -number

print(opposite(-13))
print(opposite(17))
print(opposite(-145633))