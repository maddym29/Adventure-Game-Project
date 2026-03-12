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
def print_welcome(name, width):
""" 
This function welcomes a player with a centered greeting.
    Parameters:
        name (str): names the player
        width (int): width of name
    Returns: none
"""
    greet = f"Hello, {name}!"
    print(f"{greet:^{width}}")
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
""" This function creates a bordered menu.
    Parameters:
        item1Name (str): imputs first name
        item1Price (int): imputs first price (rounds to two decimal places)
        item2Name (str): imputs second name
        item2Price (int): imputs second price (rounds to two decimal places)
"""
    print("//--------------------\\")
    print(f"| {item1Name:<12}${item1Price:>7.2f} |")
    print(f"| {item2Name:<12}${item2Price:>7.2f} |")
    print("\\--------------------//")
print_welcome("Audrey", 6)
print_welcome("Maddy", 5)
print_welcome("Liv", 3)
print_shop_menu("Orange", 2.50, "Mango", 3.00)
print_shop_menu("Cereal", 1.253, "Milk", 4.05)
print_shop_menu("Carrots", 5.55, "Asparagus", 2.45)
