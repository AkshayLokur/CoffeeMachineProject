from menu import MENU
from menu import resources as machine_resources

money_earned = 0
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def print_report():
    print(f"\nResources in coffee machine:")
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${money_earned}")


def receive_money():
    quarters = int(input("Enter quarters: "))
    dimes = int(input("Enter dimes: "))
    nickels = int(input("Enter nickels: "))
    pennies = int(input("Enter pennies: "))

    money_received_from_user = round(quarters * QUARTER + dimes * DIME + nickels * NICKEL + pennies * PENNY, 2)
    print(f"Money received: ${money_received_from_user}")

    return money_received_from_user


def return_change(money_received, cost_of_coffee):
    if money_received > cost_of_coffee:
        print(f"Here is ${round(money_received - cost_of_coffee, 2)} dollars in change.")


def make_coffee(coffee_type, water_req, milk_req, coffee_req, cost_of_coffee):
    global money_earned

    machine_resources["water"] -= water_req
    machine_resources["milk"] -= milk_req
    machine_resources["coffee"] -= coffee_req
    money_earned += cost_of_coffee

    print(f"Enjoy your {coffee_type}! ☕️")


def is_resource_sufficient(resource_type, resource_req):
    resource_availability = machine_resources[resource_type]

    if resource_req <= resource_availability:
        return True
    else:
        return False


def are_resources_sufficient(coffee_type):
    if coffee_type not in MENU:
        print(f"\nYou have chosen a wrong drink! '{coffee_type}' can not be served at this machine!")
        return
    else:
        coffee_menu = MENU[coffee_type]
        water_req = coffee_menu["ingredients"]["water"] if "water" in coffee_menu["ingredients"] else 0
        milk_req = coffee_menu["ingredients"]["milk"] if "milk" in coffee_menu["ingredients"] else 0
        coffee_req = coffee_menu["ingredients"]["coffee"] if "coffee" in coffee_menu["ingredients"] else 0
        cost_of_coffee = coffee_menu["cost"]

        if is_resource_sufficient("milk", milk_req) and \
                is_resource_sufficient("coffee", coffee_req) and \
                is_resource_sufficient("water", water_req):
            money_received = receive_money()
            if money_received < cost_of_coffee:
                print("Sorry that's not enough money. Money refunded")
            else:
                return_change(money_received, cost_of_coffee)
                make_coffee(coffee_type, water_req, milk_req, coffee_req, cost_of_coffee)
        else:
            print(f"Sorry! Not enough resources to make a {coffee_type}")


def main():
    while True:
        coffee_type = input("\nWhat would you like? (espresso/latte/cappuccino): ")

        # Shut down coffee machine
        if coffee_type == "off":
            print("Shutting down coffee machine! Bye! 👋🏼")
            exit()
        elif coffee_type == "report":
            print_report()
        else:
            are_resources_sufficient(coffee_type)


if __name__ == "__main__":
    main()
