'''Hobby Shop:
Requirements:
    Have at least 400 articles in the shop
    Have at least four types of articles (shirt, scarf, glove, heat)
    Have at least five sizes (S M L XL XXL) for each type of article
    To be able to sell the latest article that was added to the shop
    To be able to sell any item that is in the shop
    To restock the shop with new items'''

shop_articles = [(item, size) for item in ['shirt', 'scarf', 'glove', 'hat', 'dress'] for size in ['XS', 'S', 'M', 'L', 'XL', 'XXL'] ] * 20

print('Number of articles currently in shop:', len(shop_articles))
print ('Articles in shop: ', shop_articles)


def restock(inventory):
    article_to_add = input('What article do you want to add?: ')
    number_of_articles = int(input('How many do you want to add?: '))
    article_size = input('What size are they? S/M/L/XL/XXL: ')

    for num in range(number_of_articles):
        inventory.append((article_to_add, article_size))
    print('Articles added to inventory: ', inventory, '\n')

    if input('Do you want to add another item? Y/N: ') == ('y' or 'Y'):
        restock(inventory)


# restock(shop_articles)

def sell_last(inventory):
    print('The last item has been sold and removed from the inventory: ', inventory.pop())


# sell_last(shop_articles)


def sell_item(inventory):
    article_to_remove = input('What article do you want to sell? :')
    size_article = input('What size do you want to sell?: XS/S/M/XL/XXL ')
    inventory.remove((article_to_remove,size_article))

    print ('Item has been sold and removed from inventory: ', inventory)

sell_item(shop_articles)