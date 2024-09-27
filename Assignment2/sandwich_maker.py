
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if self.resources[item] < ingredients[item]:
                return False
        return True


    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
