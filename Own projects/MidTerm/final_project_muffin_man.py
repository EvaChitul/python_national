import random

shopping_archive = []


class PrettyPrinterMixin:
    name: str
    products_fridge: dict

    def pretty_print(self):
        pretty_string = r'''
  _______________________________
 / \                             \
|   |                            |
 \_ |                            | '''
        if hasattr(self, 'ingredients'):

            pretty_name_string = '\n    |      ' + self.name  # pylint: disable=maybe-no-member
            nstr_len = len(pretty_name_string)
            pretty_string += pretty_name_string + ' ' * (34 - nstr_len) + '|'
            pretty_string += '\n    |                            |'

            for index, (key, value) in enumerate(self.ingredients.items(), start=1):  # pylint: disable=maybe-no-member
                pretty_ingredient_string = '\n    |    ' + str(index) + '. ' + key.title() + ': ' + str(value)
                istr_len = len(pretty_ingredient_string)
                pretty_string += pretty_ingredient_string + ' ' * (34 - istr_len) + '|'

        else:
            pretty_name_string = '\n    |     The Fridge Contains:   |'
            pretty_string += pretty_name_string
            pretty_string += '\n    |                            |'

            for index, (key, value) in enumerate(self.products_fridge.items(),
                                                 start=1):  # pylint:disable=maybe-nomember
                pretty_ingredient_string = '\n    |    ' + str(index) + '. ' + key.title() + ': ' + str(value)
                istr_len = len(pretty_ingredient_string)
                pretty_string += pretty_ingredient_string + ' ' * (34 - istr_len) + '|'

        pretty_string += r'''
    |   _________________________|___
    |  /                            /
    \_/____________________________/ '''
        print(pretty_string)


class Recipe(PrettyPrinterMixin):
    is_initialized = False

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients if ingredients else {}

    def __str__(self):
        number_of_stars = len(self.name) + 3
        pretty_string = '*' * number_of_stars + '\n' + self.name + '\n' + '*' * number_of_stars + '\n'

        for index, (key, value) in enumerate(self.ingredients.items(), start=1):
            pretty_string = '\n'.join((pretty_string, f'{index}. {key.title()}: {value}'))

        pretty_string = pretty_string + '\n' * 2 + '*' * number_of_stars
        return pretty_string

    def __getitem__(self, given_index):
        for index, (key, value) in enumerate(self.ingredients.items(), start=1):
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


class RecipesBox(object):

    def __init__(self):
        self.recipes_box = {}

    def __getitem__(self, index):
        return self.recipes_box[index]

    def __delitem__(self, index):
        del self.recipes_box[index]

    def __setitem__(self, index, recipe):
        self.recipes_box[index] = recipe

    def __len__(self):
        return len(self.recipes_box)

    # def insert(self, index, recipe):
    #     self.recipes_box.insert(index, recipe)

    def __iter__(self):
        return iter(self.recipes_box)

    def __str__(self):
        return f'Recipes Box: {list(self.recipes_box.keys())}'

    def add_recipe(self, recipe):
        if recipe.name in self.recipes_box.keys():
            print(f'Action Log: Recipe {recipe.name} was already in the Recipe Box')
        else:
            self.recipes_box[recipe.name] = recipe.ingredients
            print(f'Action Log: Recipe {recipe.name} has been added to the Recipe Box')

    def delete_recipe(self, recipe):
        if recipe.name in self.recipes_box.keys():
            del self.recipes_box[recipe.name]
            print(f'Action Log: Recipe {recipe.name} has been removed from the Recipe Box')
        else:
            print(f'Action Log: Cannot remove recipe {recipe.name}: recipe not found in Recipe Box')

    def pick_recipe(self, recipe=None):
        if not recipe:
            choices = list(self.recipes_box.keys())
            recipe_choice = random.choice(choices)
            print(f'Here is a random recipe {recipe_choice} and its ingredients {self.recipes_box[recipe_choice]}')
        else:
            print(f'Here is the recipe {recipe.name} and the needed ingredients {recipe.ingredients}')


class Fridge(PrettyPrinterMixin):

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
        if len(self.products_fridge) > 0:
            stars = '*' * 30
            print('\n', stars, '\n', 'Items in Muffin Man Fridge:', '\n')
            for index, (product, quantity) in enumerate(self.products_fridge.items(), start=1):
                print(f'{index}. {product.title()}: {quantity}')
            return stars
        else:
            return '\n *** Muffin Man Fridge is empty ***'

    def add_item(self, product, quantity):
        if product in self.products_fridge:
            self.products_fridge[product] += quantity
            print(f'Action Log: {product} already in Muffin Man Fridge. Updating quantity with {quantity}')
        else:
            self.products_fridge[product] = quantity
            print(f'Action Log: Adding {product} to Muffin Man Fridge')

    def delete_item(self, product):
        if product in self.products_fridge:
            del self.products_fridge[product]
            print(f'Action Log: {product} has been removed from the Fridge')
        else:
            print(f'Action Log: Cannot remove {product}: not found in Muffin Man Fridge')

    def remove_quantity_item(self, product, quantity):
        if product in self.products_fridge:
            if self.products_fridge[product] > quantity:
                self.products_fridge[product] -= quantity
                print(f'Action Log: Removing {quantity} of {product}. '
                      f'You now have {self.products_fridge[product]}of {product} left in the Fridge')
            elif self.products_fridge[product] == quantity:
                del self.products_fridge[product]
                print(f'Action Log: Removing {quantity} of {product}. No {product} left. Please buy more!')
            else:
                print(f'Action Log: Insufficient {product} in Fridge. Please adapt quantity to remove')
        else:
            print(f'Action Log: No {product} in the Fridge. Please buy {product}!')

    def add_quantity_item(self, product, quantity):
        if product in self.products_fridge:
            self.products_fridge[product] += quantity
            print(f'Action Log: {product} quantity has been updated with {quantity} in the Fridge.'
                  f'You now have {self.products_fridge[product]}')
        else:
            self.products_fridge[product] = quantity
            print(f'Action Log: You did not have {product} in the Fridge. Quantity now updated to {quantity}')

    def check_recipe(self, recipe):
        items_to_buy = []
        items_in_fridge = []
        for ingredient in recipe.ingredients.keys():
            if ingredient.title() in self.products_fridge.keys():
                items_in_fridge.append(ingredient.title())
            else:
                items_to_buy.append(ingredient.title())
        if items_to_buy and items_in_fridge:
            print(f'Action Log: For the recipe {recipe.name} you already have {items_in_fridge}. '
                  f'You need to buy {items_to_buy}')
        elif not items_to_buy and items_in_fridge:
            print(f'Action Log: You have all the ingredients for the {recipe.name} recipe: {items_in_fridge}')
        else:
            print(f'Action Log: You have none of the ingredients for the {recipe.name} recipe. '
                  f'Go shopping and get {items_to_buy}')
        return items_in_fridge, items_to_buy


def check_the_fridge(fridge, recipe_box):
    contents_fridge = set([item.lower() for item in fridge])
    list_ingredients_for_recipe = {recipe: set(recipe_box[recipe].keys()) for recipe in recipe_box}

    possible_recipes = []

    for name, ingredients in list_ingredients_for_recipe.items():
        if len(ingredients.intersection(contents_fridge)) >= len(ingredients) / 2:
            possible_recipes.append(name)

    print(f'Action Log: Possible recipes you can make with the products in your fridge:{(list(possible_recipes))}')
    return possible_recipes


def pretty_print_recipe(shop_list):
    def pretty_recipe(*args):
        if shop_list(*args):
            muffin_man_string = r'''
 ........................................................
 :   ,-.      ,-.      ,-.      ,-.      ,-.      ,-.   :
 : _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_ :
 :(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _):
 :  / o \    / o \    / o \    / o \    / o \    / o \  :
 : (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_) :
 :   ,-.   ....................................   ,-.   :
 : _(*_*)_ :                                  : _(*_*)_ :
 :(_  o  _):          Shopping list:          :(_  o  _):
 :  / o \  :                                  :  / o \  :
 : (_/ \_) :                                  : (_/ \_) :'''

            list_shop = shop_list(*args)
            muffin_index = 1
            space_number = 46
            for index, (key, value) in enumerate(list_shop.items(), start=1):
                if muffin_index == 1:
                    muffin_string = ' :   ,-.   :   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (
                            space_number - len(muffin_string)) + ':   ,-.   :'
                elif muffin_index == 2:
                    muffin_string = ' : _(*_*)_ :   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (
                            space_number - len(muffin_string)) + ': _(*_*)_ :'
                elif muffin_index == 3:
                    muffin_string = ' :(_  o  _):   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (
                            space_number - len(muffin_string)) + ':(_  o  _):'
                elif muffin_index == 4:
                    muffin_string = ' :  / o \  :   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (
                            space_number - len(muffin_string)) + ':  / o \  :'
                elif muffin_index == 5:
                    muffin_string = ' : (_/ \_) :   ' + str(index) + '. ' + key.title() + ': ' + str(value)
                    muffin_man_string += '\n' + muffin_string + ' ' * (
                            space_number - len(muffin_string)) + ': (_/ \_) :'

                muffin_index += 1
                if (muffin_index > 5):
                    muffin_index = 1

            if muffin_index == 2:
                muffin_man_string += '\n : _(*_*)_ :                                  : _(*_*)_ :'
                muffin_index += 1
            if muffin_index == 3:
                muffin_man_string += '\n :(_  o  _):                                  :(_  o  _):'
                muffin_index += 1
            if muffin_index == 4:
                muffin_man_string += '\n :  / o \  :                                  :  / o \  :'
                muffin_index += 1
            if muffin_index == 5:
                muffin_man_string += '\n : (_/ \_) :                                  : (_/ \_) :'

            muffin_man_string += r'''
 :   ,-.   :                                  :   ,-.   :
 : _(*_*)_ :                                  : _(*_*)_ :
 :(_  o  _):                                  :(_  o  _):
 :  / o \  :                                  :  / o \  :
 : (_/ \_) :..................................: (_/ \_) :
 :   ,-.      ,-.      ,-.      ,-.      ,-.      ,-.   :
 : _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_ :
 :(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _):
 :  / o \    / o \    / o \    / o \    / o \    / o \  :
 : (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_) :
 :......................................................: '''
            print(muffin_man_string)
            return list_shop
        else:
            print('No Muffin Man shopping list!')

    return pretty_recipe


def archive_shopping_list(shop_list):
    def archive_store(*args):
        list_to_archive = shop_list(*args)
        if list_to_archive:
            shopping_archive.append(list_to_archive)
        else:
            print(f'No shopping list to add to archive')
    return archive_store


@archive_shopping_list
@pretty_print_recipe
def prepare_shopping_list(fridge, recipe):
    products_fridge = {item.lower(): fridge[item] for item in fridge}

    shopping_list = {}

    for product, quantity in recipe.ingredients.items():
        if product not in products_fridge:
            shopping_list[product] = quantity
        else:
            if quantity > products_fridge[product]:
                shopping_list[product] = quantity - products_fridge[product]
    return shopping_list


# from muffin_man_shopping_list import Recipe, RecipesBox, Fridge, PrettyPrinterMixin, check_the_fridge, \
#     pretty_print_recipe, archive_shopping_list, prepare_shopping_list, shopping_archive

mac_and_cheese_ingredients = {'macaroni': 2, 'cheese': 2, 'oil': 2, 'salt': 2}
croque_monsieur_ingredients = {'bread': 10, 'cheese': 5, 'ham': 5, 'butter': 1}
pasta_pesto_ingredients = {'pasta': 2, 'pesto': 2, 'nuts': 1, 'oil': 3, 'basil': 5, 'garlic': 3}
stuffed_peppers_ingredients = {'peppers': 8, 'minced meat': 10, 'rice': 5, 'onion': 1}
tiramisu_ingredients = {'lady fingers': 40, 'mascarpone': 2, 'eggs': 6, 'cream': 1, 'coffee': 4, 'cocoa': 1}
chocolate_cake_ingredients = {'flour': 10, 'eggs': 5, 'sugar': 2, 'chocolate': 4, 'milk': 2}

mac_and_cheese = Recipe('Mac and Cheese', mac_and_cheese_ingredients)
croque_monsieur = Recipe('Croque Monsieur', croque_monsieur_ingredients)
pasta_pesto = Recipe('Pasta with Pesto', pasta_pesto_ingredients)
stuffed_peppers = Recipe('Stuffed Peppers', stuffed_peppers_ingredients)
tiramisu = Recipe('Tiramisu', tiramisu_ingredients)
chocolate_cake = Recipe('Chocolate Cake', chocolate_cake_ingredients)

print(pasta_pesto)
print(mac_and_cheese)
print(croque_monsieur)
print(chocolate_cake)
print(tiramisu)
print(stuffed_peppers)

# chocolate_cake.name = 'Banana bread'
# stuffed_peppers.ingredients = {'tomatoes': 4, 'onions': 5, 'zucchini': 3}

recipes_box = RecipesBox()

recipes_box.add_recipe(croque_monsieur)
recipes_box.add_recipe(mac_and_cheese)
recipes_box.add_recipe(pasta_pesto)
recipes_box.add_recipe(stuffed_peppers)
recipes_box.add_recipe(pasta_pesto)
print(recipes_box, '\n')

recipes_box.delete_recipe(pasta_pesto)
recipes_box.delete_recipe(stuffed_peppers)
recipes_box.delete_recipe(stuffed_peppers)
print(recipes_box, '\n')

recipes_box.pick_recipe(mac_and_cheese)
recipes_box.pick_recipe(tiramisu)
recipes_box.pick_recipe()

muffin_man_fridge = Fridge()
print(muffin_man_fridge, '\n')

muffin_man_fridge.add_item('Eggs', 30)
muffin_man_fridge.add_item('Tomatoes', 50)
muffin_man_fridge.add_item('Juice', 4)
muffin_man_fridge.add_item('Cheese', 40)
muffin_man_fridge.add_item('Pesto', 4)
muffin_man_fridge.add_item('Pesto', 10)
muffin_man_fridge.add_item('Mascarpone', 50)
muffin_man_fridge.add_item('Chocolate', 10)
print(muffin_man_fridge, '\n')

muffin_man_fridge.delete_item('Eggs')
muffin_man_fridge.delete_item('Cheese')
muffin_man_fridge.delete_item('Cheese')
print(muffin_man_fridge, '\n')

muffin_man_fridge.remove_quantity_item('Juice', 10)
muffin_man_fridge.remove_quantity_item('Apples', 13)
muffin_man_fridge.remove_quantity_item('Tomatoes', 10)
muffin_man_fridge.remove_quantity_item('Tomatoes', 40)
print(muffin_man_fridge, '\n')

muffin_man_fridge.add_quantity_item('Cheese', 30)
muffin_man_fridge.add_quantity_item('Halloumi', 50)
muffin_man_fridge.add_quantity_item('Veggie Burger', 4)
muffin_man_fridge.add_quantity_item('Ham', 10)
muffin_man_fridge.add_quantity_item('Ham', 20)
muffin_man_fridge.add_quantity_item('Bread', 20)
print(muffin_man_fridge, '\n')

print(muffin_man_fridge.check_recipe(mac_and_cheese))
print(muffin_man_fridge.check_recipe(croque_monsieur))
print(muffin_man_fridge.check_recipe(tiramisu))

if 'Juice' in muffin_man_fridge:
    print('YES! In Muffin Man Fridge')
else:
    print('Not in Muffin Man Fridge!')

if 'Candy' in muffin_man_fridge:
    print('YES! In Muffin Man Fridge')
else:
    print('Not in Muffin Man Fridge!')

print(muffin_man_fridge, '\n')
print(len(muffin_man_fridge))
del muffin_man_fridge['Juice']
muffin_man_fridge.add_item('Pasta', 10)
muffin_man_fridge.add_item('Nuts', 10)
muffin_man_fridge.add_item('Oil', 10)
muffin_man_fridge.add_item('Basil', 10)
muffin_man_fridge.add_item('Garlic', 10)
print(muffin_man_fridge, '\n')

recipes_box.add_recipe(croque_monsieur)
recipes_box.add_recipe(mac_and_cheese)
recipes_box.add_recipe(pasta_pesto)
recipes_box.add_recipe(stuffed_peppers)
recipes_box.add_recipe(pasta_pesto)
print(recipes_box, '\n')

print(check_the_fridge(muffin_man_fridge, recipes_box))

muffin_man_fridge.pretty_print()
mac_and_cheese.pretty_print()
tiramisu.pretty_print()
chocolate_cake.pretty_print()

print(muffin_man_fridge, '\n')
prepare_shopping_list(muffin_man_fridge, mac_and_cheese)
prepare_shopping_list(muffin_man_fridge, pasta_pesto)
prepare_shopping_list(muffin_man_fridge, croque_monsieur)
prepare_shopping_list(muffin_man_fridge, stuffed_peppers)

print('This is the Shopping Archive:', shopping_archive)
