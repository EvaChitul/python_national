'''
Recipe class that is a mapping
New recipe can be created starting from a name and dictionary of ingredients and quantities
Once a recipe has been created is cannot be updated
'''

from collections.abc import Mapping


class Recipe(Mapping):

    def __init__(self, name, ingredients = None):
        self.name = name
        self.ingredients = ingredients if ingredients else {}

    def __iter__(self):
        return iter(self.ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __getitem__(self, ingredient):
        return self.ingredients[ingredient]

    def __str__(self):
        print('*'*20,'\n',self.name,'\n','*'*20)
        for index, ingredient in enumerate(self.ingredients, start = 1):
            print(index,'.', ingredient.title(),':', self.ingredients[ingredient],'\n')
        return('*' * 20)


mac_and_cheese_ingredients = {'macaroni': 1,'cheese': 0.5 }

mac_and_cheese = Recipe('Mac and Cheese', mac_and_cheese_ingredients)

print(mac_and_cheese)
print(mac_and_cheese.__getitem__('macaroni'))

pasta_pesto_ingredients = { 'pasta': 2, 'pesto' : 1}
pasta_pesto = Recipe('Pasta with Pesto', pasta_pesto_ingredients)
print(pasta_pesto)