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
