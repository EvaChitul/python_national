'''Fix CrayonsBox so that it fully conforms to MutableSequence.'''

from collections.abc import MutableSequence


class CrayonsBox(MutableSequence):

    def __init__(self, iterable):
        self._crayons = list(iterable)

    def __len__(self):
        return len(self._crayons)

    def __getitem__(self, index):
        return self._crayons[index]

    def __delitem__(self, index):
        print('Deleting the', self._crayons[index], 'crayon')
        del self._crayons[index]

    def __setitem__(self, index, item):
        print('Replacing the', self._crayons[index], 'crayon with', item)
        self._crayons[index] = item

    def insert(self, index, item):
        print('Adding', item, 'at position', index, 'in the crayon box')
        self._crayons.insert(index, item)

    def __str__(self):
        return f'The Crayon Box now contains: {self._crayons}'


crayons = 'White Yellow Blue Red Green Black Brown'.split()
crayons_box = CrayonsBox(crayons)


del crayons_box[2]
print(crayons_box, '\n')

crayons_box[5] = 'Purple'
print(crayons_box, '\n')

crayons_box.insert(5, 'Turquoise')
print(crayons_box, '\n')

