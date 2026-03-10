"""Use this module to calculate a purchase or create a monster.

Use this module to create a game, giving your monster the ability
to purchase items, create a menu, and welcome other players.
"""

input random
def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
"""
This function calculates how many items can be purchased with a starting amount.
Parameters: 
    itemPrice: how much does each item cost?
    startingMoney: how much money does your monster have?
    quantityToPurchase: is at least one.
Returns: none
"""
    max_affordable = startingMoney // itemPrice
    if max_affordable < quantityToPurchase:
        items_bought = max_affordable
    else:
        items_bought = quantityToPurchase
    money_left = startingMoney - (items_bought * itemPrice)
    return items_bought, money_left
num_purchased, leftover_money = purchase_item(123, 1000, 3)
num_purchased, leftover_money = purchase_item(3141, 2112)
num_purchased, leftover_money = purchase_item(241, 203, 5)
print(purchase_item(123, 1000, 3))
print(purchase_item(3141, 2112))
print(purchase_item(241, 203, 5))
def new_random_monster():
"""
This function produces a monster.
    Paramaters: none
    Returns: none
"""
    monsters = ["Giraffe Bear", "Smoothie Butterfly", "Kitten Dragon"]
    healthy = [3, 4, 6]
    worth = [500, 200, 400]
    name = random.choice(monsters)
    if name == "Giraffe Bear":
        description = "You are a cuddly creature with a long neck."
        health = random.choice([1,3,5])
        power = "Ability to reach high things and give warm hugs"
        money = random.choice([100, 300, 500])
    elif name == "Smoothie Butterfly":
        description = "You are a beautiful bug with strawberry banana scented wings."
        health = random.choice([2,4,6])
        power = "Ability to slurp up enemies and make a mean kale smoothie."
        money = random.choice([200, 400, 600])
    elif name == "Kitten Dragon":
        description = "You are a blue cat with green eyes and purple wings and tail."
        health = random.choice([6, 8, 10])
        power = "Ability to breath fire on enemies and always land on feet."
        money = random.choice([10, 20, 40])
    else:
        description = "Invalid choice."
        health = "Invalid choice."
        power = "Invalid choice."
        money = "Invalid choice."
    monster = {
        "name": name,
        "description": description,
        "health": health,
        "power": power,
        "money": money
    }     
    return monster
def welcome(name, width):
""" 
This function works to welcome a player.
    Parameters:
        name (str): names the player
        width (int): width of name
    Returns: none
"""
    greet = print(f"Hello,{name:+^width}!")
    return greet
def shop_menu(item1Name, item1Price, item2Name, item2Price):
""" This function creates a boardered menu.
    Parameters:
        item1Name (str): inputs first name
        item1Price (int): inputs first price (rounds to two decimal places)
        item2Name (str): inputs second name
        item2Price (int): inputs second price (rounds to two decimal places)
"""
    line1 = print(//******************\\)
    line2 = print(f"| {item1Name:<12}{item1Price:.2f>8}")
    line3 = print(f"| {item2Name:<12}{item2Price:.2f>8}")
    menu = line1 + line2 + line3 + line1
    return menu
