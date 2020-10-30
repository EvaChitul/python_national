'''DONE We also have a fridge that's a mutable mapping that .
1. DONE Holds some products together with their quantities
2. DONE When printing the fridge object, it will print similar to a recipe, its contents.
3. DONE We can also ask if a certain product is in the fridge.
4. DONE Add items to the fridge
5. DONE Remove items from the fridge
6. DONE Update quantities in fridge - if becomes 0 should get notification and remove the product from fridge
7. Check recipe method to see if we have all ingredients for a recipe --> return 2 lists:
                                                                     A) items of recipe we have in fridge
                                                                     B) items we need from the shop
'''

from collections.abc import MutableMapping


class Fridge(MutableMapping):

    def __init__(self):
        self.products_fridge = {}

    def __len__(self):
        return len(self.products_fridge)

    def __getitem__(self, product):
        return f'We have the {self.products_fridge[product]} in the Fridge.'

    def __delitem__(self, product):
        print(f'Deleting product {self.products_fridge[product]} from the Fridge')
        del self.products_fridge[product]

    def __setitem__(self, product, quantity):
        print('Quantity of ', self.products_fridge[product], 'now set at', quantity)
        self.products_fridge[product] = quantity

    def __iter__(self):
        return iter(self.products_fridge)

    def __str__(self):
        return f'These are the products in your fridge: \n{", ".join(list(self.products_fridge.keys()))}'

    def add_item(self, product, quantity):
        self.products_fridge[product] = quantity

    def delete_item(self, product):
        print(f'{product} will be removed from the Fridge')
        del self.products_fridge[product]

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


muffin_man_fridge = Fridge()

muffin_man_fridge.add_item('Eggs', 30)
muffin_man_fridge.add_item('Tomatoes', 50)
muffin_man_fridge.add_item('Juice', 4)

print(muffin_man_fridge)

muffin_man_fridge.delete_item('Eggs')
print(muffin_man_fridge)
print(muffin_man_fridge.remove_quantity_item('Juice', 10))
print(muffin_man_fridge.remove_quantity_item('Apples', 13))
print(muffin_man_fridge.remove_quantity_item('Tomatoes', 10))
print(muffin_man_fridge.remove_quantity_item('Tomatoes',40))
print(muffin_man_fridge)


muffin_man_fridge.add_item('Cheese', 30)
muffin_man_fridge.add_item('Halloumi', 50)
muffin_man_fridge.add_item('Veggie Burger', 4)

if 'Juice' in muffin_man_fridge:
    print('YES!')

print(muffin_man_fridge)
print(len(muffin_man_fridge))