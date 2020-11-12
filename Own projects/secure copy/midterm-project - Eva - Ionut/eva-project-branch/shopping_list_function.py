
def prepare_shopping_list(fridge, recipe):
    products_fridge = {item.lower(): fridge[item] for item in fridge}

    shopping_list = {}

    for product, quantity in recipe.ingredients.items():
        if product not in products_fridge:
            shopping_list[product] = quantity
        else:
            if quantity > products_fridge[product]:
                shopping_list[product] = quantity - products_fridge[product]

    return f'This is the needed shopping list for {recipe.name}: {shopping_list}'