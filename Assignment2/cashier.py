class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Insert coins:")
        quarters = float(input("How many quarters? ")) * 0.25
        dimes = float(input("How many dimes? ")) * 0.10
        nickels = float(input("How many nickels? ")) * 0.05
        pennies = float(input("How many pennies? ")) * 0.01
        return quarters + dimes + nickels + pennies



    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            return True, change
        else:
            return False, 0

