''' Update the Student class so that the validations are applied also at init
not allowing an object to be created if age is not valid.'''

# Original Class
class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if type(age) is not int:
            raise TypeError('Age must be integer')

        if age < 18:
            raise ValueError('Minimal age is 18')

        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(
            class_name, self.first_name,
            self.last_name, self.age, id(self)
        )

    def __str__(self):
        return '{} {}, {}'.format(
            self.first_name, self.last_name, self.age)


# New Class
class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if type(age) is not int:
            raise TypeError('Age must be integer')

        if age < 18:
            raise ValueError('Minimal age is 18')

        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(
            class_name, self.first_name,
            self.last_name, self.age, id(self)
        )

    def __str__(self):
        return '{} {}, {}'.format(
            self.first_name, self.last_name, self.age)


eva = Student('Eva', 'Chitul', 31)
print(eva.age)

# dana = Student('Dana', 'Mason', 15)
ted = Student('Ted', 'Bundy', 'Washington')