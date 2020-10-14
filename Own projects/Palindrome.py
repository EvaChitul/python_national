# Ask for a word and check whether it's a palindrome

to_check = input('Please insert a word: ')

if to_check.lower() == to_check[::-1].lower():
    print ('The word ' + to_check + ' is a palindrome')
else:
    print ('The word ' + to_check + ' is not a palindrome')


