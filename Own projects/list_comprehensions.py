
number = int(input(' Please insert a number: '))
list_input = range(number)

new_list = [elem+1 for elem in list_input]
print('All the numbers up until', number, ' are ', new_list)

odd_list = [elem for elem in new_list if elem % 2 != 0]
even_list = [elem for elem in new_list if elem % 2 == 0]

print('These are the odd numbers: ', odd_list)
print('These are the even numbers: ', even_list)