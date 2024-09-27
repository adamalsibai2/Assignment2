import data
from sandwich_maker import SandwichMaker
from cashier import Cashier
#

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        user_input = input("What would you like? (small/medium/large/off/report): ").lower()

        if user_input == "off":
            print("Turning off the machine.")
            break
        elif user_input == "report":
            print(f"Current resources:\nBread: {resources['bread']} slices\n"
                  f"Ham: {resources['ham']} slices\n"
                  f"Cheese: {resources['cheese']} ounces")
        elif user_input in recipes:
            sandwich_cost = recipes[user_input]["cost"]
            sandwich_ingredients = recipes[user_input]["ingredients"]

            if not sandwich_maker_instance.check_resources(sandwich_ingredients):
                print(f"Sorry, there is not enough resources to make a {user_input} sandwich.")
                continue

            print(f"The price for a {user_input} sandwich is ${sandwich_cost:.2f}.")
            money_inserted = cashier_instance.process_coins()

            transaction_successful, change = cashier_instance.transaction_result(money_inserted, sandwich_cost)
            if transaction_successful:
                sandwich_maker_instance.make_sandwich(sandwich_ingredients)
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                print(f"Enjoy your {user_input} sandwich!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid option. Please choose 'small', 'medium', 'large', 'off', or 'report'.")

    if __name__ == "__main__":
        main()







