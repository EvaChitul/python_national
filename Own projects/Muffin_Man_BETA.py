import random


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
        self.recipes_box[recipe.name] = recipe.ingredients
        return f'Recipe {recipe.name} has been added to the Recipe Box'

    def delete_recipe(self, recipe):
        del self.recipes_box[recipe.name]
        return f'Recipe {recipe.name} has been removed from the Recipe Box'

    def pick_recipe(self, recipe=None):
        if not recipe:
            choices = list(self.recipes_box.keys())
            recipe_choice = random.choice(choices)
            return f'Here is a random recipe {recipe_choice} and its ingredients {self.recipes_box[recipe_choice]}'
        else:
            return f'Here is your recipe {recipe.name} and the needed ingredients {recipe.ingredients}'


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
        stars = '*' * 20
        print(stars, '\n', 'Items in Fridge:', '\n')
        for index, (product, quantity) in enumerate(self.products_fridge.items(), start=1):
            print(f'{index}. {product.title()}: {quantity}')
        return stars

    def add_item(self, product, quantity):
        self.products_fridge[product] = quantity

    def delete_item(self, product):
        del self.products_fridge[product]
        return f'{product} will be removed from the Fridge'

    def remove_quantity_item(self, product, quantity):
        if product in self.products_fridge.keys():
            if self.products_fridge[product] > quantity:
                self.products_fridge[product] -= quantity
                return f'Removing {quantity} of {product}. You now have {self.products_fridge[product]} ' \
                       f'of {product} left in the Fridge'
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
            return f'{product} quantity has been updated with {quantity} in the Fridge. ' \
                   f'You now have {self.products_fridge[product]}'
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


def check_the_fridge(fridge, recipe_box):
    contents_fridge = set([item.lower() for item in fridge])
    print('Fridge', contents_fridge)

    list_ingredients_for_recipe = {recipe: set(recipe_box[recipe].keys()) for recipe in recipe_box}
    print('Ingredients for recipe:', list_ingredients_for_recipe)

    possible_recipes = []

    for name, ingredients in list_ingredients_for_recipe.items():
        if len(ingredients.intersection(contents_fridge)) >= len(ingredients) / 2:
            possible_recipes.append(name)

    return f'Possible recipes you can make with the products in your fridge:{(list(possible_recipes))}'


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


shopping_archive = []


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


# ************************ TESTS AREA - TO BE MOVED *******************************************

mac_and_cheese_ingredients = {'macaroni': 2, 'cheese': 2}
croque_monsieur_ingredients = {'bread': 10, 'cheese': 5, 'ham': 5}
pasta_pesto_ingredients = {'pasta': 2, 'pesto': 1}
stuffed_peppers_ingredients = {'peppers': 8, 'minced meat': 10, 'rice': 5, 'onion': 1}

mac_and_cheese = Recipe('Mac and Cheese', mac_and_cheese_ingredients)
croque_monsieur = Recipe('Croque Monsieur', croque_monsieur_ingredients)
pasta_pesto = Recipe('Pasta with Pesto', pasta_pesto_ingredients)
stuffed_peppers = Recipe('Stuffed Peppers', stuffed_peppers_ingredients)

print(pasta_pesto)
print(mac_and_cheese)
print(croque_monsieur)

muffin_man_fridge = Fridge()

muffin_man_fridge.add_item('Eggs', 30)
muffin_man_fridge.add_item('Tomatoes', 50)
muffin_man_fridge.add_item('Juice', 4)
muffin_man_fridge.add_item('Cheese', 40)
muffin_man_fridge.add_item('Pesto', 4)

print(muffin_man_fridge)

muffin_man_fridge.delete_item('Eggs')
print(muffin_man_fridge)

print(muffin_man_fridge.remove_quantity_item('Juice', 10))
print(muffin_man_fridge.remove_quantity_item('Apples', 13))
print(muffin_man_fridge.remove_quantity_item('Tomatoes', 10))
print(muffin_man_fridge.remove_quantity_item('Tomatoes', 40))
print(muffin_man_fridge)

muffin_man_fridge.add_item('Cheese', 30)
muffin_man_fridge.add_item('Halloumi', 50)
muffin_man_fridge.add_item('Veggie Burger', 4)
muffin_man_fridge.add_item('Ham', 10)
muffin_man_fridge.add_item('Bread', 20)

if 'Juice' in muffin_man_fridge:
    print('YES!')

print(muffin_man_fridge)
print(len(muffin_man_fridge))

print(muffin_man_fridge.__getitem__('Juice'))
print(muffin_man_fridge.__setitem__('Juice', 20))
del muffin_man_fridge['Juice']

print(muffin_man_fridge.check_recipe(mac_and_cheese))
print(muffin_man_fridge.check_recipe(croque_monsieur))


recipes_box = RecipesBox()

recipes_box.add_recipe(croque_monsieur)
recipes_box.add_recipe(mac_and_cheese)
recipes_box.add_recipe(pasta_pesto)
recipes_box.add_recipe(stuffed_peppers)
print(recipes_box)

print(recipes_box.delete_recipe(pasta_pesto))
print(recipes_box)

print(recipes_box.pick_recipe(mac_and_cheese))
print(recipes_box.pick_recipe())

print(check_the_fridge(muffin_man_fridge, recipes_box))

muffin_man_fridge.pretty_print()
mac_and_cheese.pretty_print()

prepare_shopping_list(muffin_man_fridge, mac_and_cheese)
prepare_shopping_list(muffin_man_fridge, pasta_pesto)
prepare_shopping_list(muffin_man_fridge, croque_monsieur)
prepare_shopping_list(muffin_man_fridge, stuffed_peppers)

mac_and_cheese_ingredients = {'macaroni': 50, 'cheese': 50}

print('This is the Shopping Archive:', shopping_archive)
