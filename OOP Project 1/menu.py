# list of items to make coffee
class MenuItems:
    # Models each menu item.
    def __init__(self, name, milk, coffee, water,cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water':water,
            'milk':milk,
            'coffee':coffee
        }

class Menu:
    # Models the menu with drinks. 
    def __init__(self):
        self.menu = [
            MenuItems(name = "lattee",water = 200, milk = 150, coffee = 24, cost = 2.5),
            MenuItems(name = "espresso",water = 50, milk =0, coffee = 12, cost = 1.5),
            MenuItems(name = "cappuccino",water = 250, milk = 50, coffee = 24, cost = 3.5),
            MenuItems(name = "flatWhite", water = 180, milk = 45, coffee =  23, cost = 2),
            MenuItems(name = "Americano", water = 100, milk = 0, coffee = 21, cost = 1.5)
        ]

    def get_items(self):
        # Returns all the names of the available menu items
        options = " "
        for item in self.menu:
            options += f"{item.name} | "
        return options
    
    def find_drink(self,order_name):
        # searches the menu fo a particular drink by name. Returns the iten if it exists, otherwise returns none.

        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
 
