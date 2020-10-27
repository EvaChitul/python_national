''' You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of
the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would
make this happen, return -1. '''

def find_even_index(arr):
    for poz in range(len(arr)):
        if sum(arr[:poz]) == sum(arr[poz+1:]):
            return poz
    return -1


prima = [1,2,3,4,5,56,6,67,7,7]
second = [1,2,3,4,3,2,1]
third = [1,100,50,-51,1,1]

print(find_even_index((prima)))
print(find_even_index((second)))
print(find_even_index((third)))