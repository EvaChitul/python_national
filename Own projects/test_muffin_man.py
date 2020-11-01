from collections.abc import MutableMapping
from collections.abc import Mapping
from collections.abc import MutableSequence
import random
import pprint


class Recipe(object):
    is_initialized = False

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients if ingredients else {}

    def __str__(self):
        number_of_stars = len(self.name) + 3
        pretty_string = '*' * number_of_stars + '\n' + self.name + '\n' + '*' * number_of_stars + '\n'

        for index, (key, value) in enumerate(self.ingredients.items(), start = 1):
            pretty_string = '\n'.join((pretty_string, f'{index}. {key.title()}: {value}'))

        pretty_string = pretty_string + '\n' * 2 + '*' * number_of_stars
        return pretty_string

    def __getitem__(self, given_index):
        for index, (key, value) in enumerate(self.ingredients.items(), start = 1):
            if given_index == index:
                return {key: value}

    def __len__(self):
        return len(self.ingredients)

    def __iter__(self):
        return iter(self.ingredients)

    def keys(self):
        return self.ingredients.keys()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self.is_initialized:
            raise NameError("You can't update the recipe!")
        self._name = name

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if self.is_initialized:
            raise NameError("You can't update the recipe!")
        self._ingredients = ingredients
        self.is_initialized = True


class RecipesBox():

    recipe_list = list()

    def __init__(self, *recipes):
        for recipe in recipes:
            self.recipe_list.append(recipe)

    def __str__(self):
        string_list = ""

        for index, recipe in enumerate(self.recipe_list):
            string_list = string_list + recipe.name
            if index != len(self.recipe_list)-1:
                string_list += '\n'

        return string_list

    def add_recipe(self, new_recipe):
        self.recipe_list.append(new_recipe)

    def remove_recipe(self, recipe):
        self.recipe_list.remove(recipe)

    def pick(self, name=None):
        if name == None:
            random_number = randint(0, len(self.recipe_list)-1)
            return self.recipe_list[random_number]

        else:
            for recipe in self.recipe_list:
                if recipe.name == name:
                    return recipe


class Fridge(MutableMapping):

    def __init__(self):
        self.products_fridge = {}

    def __len__(self):
        return len(self.products_fridge)

    def __getitem__(self, product):
        return self.products_fridge[product]

    def __delitem__(self, product):
        del self.products_fridge[product]

    def __setitem__(self, product, quantity):
        self.products_fridge[product] = quantity
        return f'Quantity of {product} now set at {quantity}'

    def __iter__(self):
        return iter(self.products_fridge)

    def __str__(self):
        return f'These are the products in your fridge: \n{", ".join(list(self.products_fridge.keys()))}'

    def add_item(self, product, quantity):
        self.products_fridge[product] = quantity

    def delete_item(self, product):
        del self.products_fridge[product]
        return f'{product} will be removed from the Fridge'

    def remove_quantity_item(self, product, quantity):
        if product in self.products_fridge.keys():
            if self.products_fridge[product] > quantity:
                self.products_fridge[product] -= quantity
                return f'Removing {quantity} of {product}. You now have {self.products_fridge[product]} of {product} left in the Fridge'
            elif self.products_fridge[product] == quantity:
                del self.products_fridge[product]
                return f'Removing {quantity} of {product}. No {product} left. Please buy more!'
            else:
                return f'Insufficient {product} in Fridge. Please adapt quantity to remove'
        else:
            return f'No {product} in the Fridge. Please buy {product}!'

    def add_quantity_item(self, product, quantity):
        if product in self.products_fridge.keys():
            self.products_fridge[product] += quantity
            return f'{product} quantity has been updated with {quantity} in the Fridge. You now have {self.products_fridge[product]}'
        else:
            self.products_fridge[product] = quantity
            return f'You did not have {product} in the Fridge. Quantity now updated to {quantity}'

    def check_recipe(self, recipe):
        items_to_buy = []
        items_in_fridge = []
        for ingredient in recipe.ingredients.keys():
            if ingredient.title() in self.products_fridge.keys():
                items_in_fridge.append(ingredient.title())
            else:
                items_to_buy.append(ingredient.title())
        if items_to_buy and items_in_fridge:
            return f'For the recipe {recipe.name} you already have {items_in_fridge}. You need to buy {items_to_buy}'
        elif not items_to_buy and items_in_fridge:
            return f'You have all the ingredients for the {recipe.name} recipe: {items_in_fridge}'
        else:
            return f'You have none of the ingredients for the {recipe.name} recipe. Go shopping and get {items_to_buy}'


mac_and_cheese_ingredients = {'macaroni': 1,'cheese': 0.5 }

mac_and_cheese = Recipe('Mac and Cheese', mac_and_cheese_ingredients)

print(mac_and_cheese)
print(mac_and_cheese.__getitem__('macaroni'))

pasta_pesto_ingredients = {'pasta': 2, 'pesto': 1}
pasta_pesto = Recipe('Pasta with Pesto', pasta_pesto_ingredients)
print(pasta_pesto)

croque_monsieur_ingredients = {'bread': 10, 'cheese': 5, 'ham': 5}
croque_monsieur = Recipe('Croque Monsieur', croque_monsieur_ingredients)
print(croque_monsieur)

# muffin_man_fridge = Fridge()
#
# muffin_man_fridge.add_item('Eggs', 30)
# muffin_man_fridge.add_item('Tomatoes', 50)
# muffin_man_fridge.add_item('Juice', 4)
#
# print(muffin_man_fridge)
#
# muffin_man_fridge.delete_item('Eggs')
# print(muffin_man_fridge)
# print(muffin_man_fridge.remove_quantity_item('Juice', 10))
# print(muffin_man_fridge.remove_quantity_item('Apples', 13))
# print(muffin_man_fridge.remove_quantity_item('Tomatoes', 10))
# print(muffin_man_fridge.remove_quantity_item('Tomatoes',40))
# print(muffin_man_fridge)
#
# muffin_man_fridge.add_item('Cheese', 30)
# muffin_man_fridge.add_item('Halloumi', 50)
# muffin_man_fridge.add_item('Veggie Burger', 4)
# muffin_man_fridge.add_item('Ham', 10)
# muffin_man_fridge.add_item('Bread', 20)
#
# if 'Juice' in muffin_man_fridge:
#     print('YES!')
#
# print(muffin_man_fridge)
# print(len(muffin_man_fridge))
#
# print(muffin_man_fridge.__getitem__('Juice'))
# print(muffin_man_fridge.__setitem__('Juice', 20))
# del muffin_man_fridge['Juice']
#
# print(muffin_man_fridge.check_recipe(mac_and_cheese))
# print(muffin_man_fridge.check_recipe(croque_monsieur))
#
#
# recipes_box = RecipesBox()
#
# recipes_box.add_recipe(croque_monsieur)
# recipes_box.add_recipe(mac_and_cheese)
# recipes_box.add_recipe(pasta_pesto)
# print(recipes_box)
#
# # print(recipes_box.delete_recipe(pasta_pesto))
# # print(recipes_box)
#
# print(recipes_box.pick_recipe(mac_and_cheese))
# print(recipes_box.pick_recipe())
#
# check_the_fridge(muffin_man_fridge,recipes_box)