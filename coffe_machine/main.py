from typing import Any

MENU: dict[str, dict[str, Any]] = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources: dict[str, int | float] = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}

is_on = True


def show_menu() -> str:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Invalid choice. Please try again.")
        return show_menu()
    return prompt


def print_report() -> None:
    for name in resources:
        if name in ["water", "milk"]:
            print(f"{name.title()}: {resources[name]}ml")
        elif name == "coffee":
            print(f"{name.title()}: {resources[name]}g")
        else:
            print(f"{name.title()}: ${resources[name]}")


def check_ingredients(coffee_type: str) -> bool:
    ingredients = MENU[coffee_type]["ingredients"]
    for name in ingredients:
        if resources[name] < ingredients[name]:
            print(f"Sorry there is not enough {name}.")
            return False
    return True


def get_coin_count(coin_name: str) -> int:
    try:
        count = int(input(f"How many {coin_name}? "))
        return max(0, count)
    except ValueError:
        print("Please enter a valid number.")
        return get_coin_count(coin_name)


def process_coins(drink_price: float) -> bool:
    total = get_coin_count("quarters") * 0.25
    total += get_coin_count("dimes") * 0.1
    total += get_coin_count("nickels") * 0.05
    total += get_coin_count("pennies") * 0.01
    if total < drink_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if total > drink_price:
        print(f"Here is ${(total - drink_price):.2f} dollars in change.")
    resources["money"] += drink_price
    return True


def make_coffee(coffee_type: str) -> None:
    for name in MENU[coffee_type]["ingredients"]:
        resources[name] -= MENU[coffee_type]["ingredients"][name]
    print(f"Here is your {coffee_type} ☕️. Enjoy!")


if __name__ == "__main__":
    while is_on:
        choice = show_menu()
        if choice == "off":
            break
        if choice == "report":
            print_report()
        if choice in ["espresso", "latte", "cappuccino"]:
            if check_ingredients(choice):
                if process_coins(MENU[choice]["cost"]):
                    make_coffee(choice)
