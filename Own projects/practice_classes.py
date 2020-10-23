class User(object):
    company = 'Py Future inc.'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_legal_to_drink(self):
        return self.age >= 21


users = [
    {'name': 'John Doe', 'age': 19},
    {'name': 'Jack Fluffy', 'age': 22},
    {'name': 'Matthew Wu', 'age': 43},
    {'name': 'Heather Rafferty', 'age': 15},
    {'name': 'Randall Blackdall', 'age': 76},
    {'name': 'Marissa Raynaud', 'age': 34},
    {'name': 'Marlo Ranbot', 'age': 49},
]

users_objects = []
for user in users:
    users_objects.append(User(user['name'].split()[0], user['name'].split()[1], user['age']) )

for user in users_objects:
    print(f' The user name is {user.first_name} {user.last_name}, he is {user.age} years old and works at {user.company}')


class Student(object):

    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, int):
            raise TypeError('Name must be string')
        else:
            self._first_name = first_name

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(
             class_name, self.first_name,
            self.last_name, self.age, id(self) )

    def __str__(self):
        return '{} {}, {}'.format(
            self.first_name, self.last_name, self.age)


eva = Student('Eva', 'Chitul', 31)
print(eva.first_name)
eva.first_name = 'Dana'
print(eva.first_name)
eva.first_name = 25
print(eva.first_name)