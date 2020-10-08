
# create a decorator called uppercase that will uppercase the result

def uppercase(func):

    def inner_up(msg):
        print('Message before upper: ', func(msg))
        print('Message after upper: ', func(msg).upper())
    return inner_up


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


greet('World')
greet('Eva')


# Create a decorator called safe_divide that will output a message if the division cannot be performed, othervise it will return the result.

def safe_divide(func):

    def inner_divide(num1, num2):
        print('We will try to divide ', num1, 'and', num2)
        if num2 == 0:
            print('Cannot divide by 0, please insert other numbers')
            return
        return func(num1, num2)
    return inner_divide


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


print('The division result is: ', divide(10, 2), '\n')
print('The division result is: ', divide(10, 0), '\n')

#  Given a set uf print methods, create a decorator called register that will update a list called print_registry with all the decorated functions names.

print_registry = []


def register(func):

    print_registry.append(func.__name__)
    return func


@register
def greet(name):
    return "Greetings {}!".format(name)

@register
def say_hello(name):
    return "Hello {}!".format(name)

@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


print(print_registry, '\n')
print(greet('Eva'))
print(say_goodbye('Dolly'))
