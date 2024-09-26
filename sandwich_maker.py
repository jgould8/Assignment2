class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients,inventory):
        """Returns True when order can be made, False if ingredients are insufficient."""
        self.inventory = inventory
        for ingredient in ingredients:
            if ingredient not in self.inventory:
                return False
            else:
                return True

    def make_sandwich(self, sandwich_size, order_ingredients,inventory):
        self.sandwich_size = sandwich_size
        self.inventory = inventory
        self.order_ingredients = order_ingredients

        if not self.check_resources(self.order_ingredients,self.inventory):
            print("Sorry, not enough resources.")
        else:
            self.inventory['bread'] = self.inventory['bread'] - self.sandwich_size['bread']
            self.inventory['ham'] = self.inventory['ham'] - self.sandwich_size['ham']
            self.inventory['cheese'] = self.inventory['cheese'] - self.sandwich_size['cheese']
            return self.inventory
            print("Here is your sandwich.")