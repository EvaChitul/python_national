
class Fridge(object):

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