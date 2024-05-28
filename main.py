from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
print_resources = CoffeeMaker()
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
resources = CoffeeMaker().resources

print(resources)
while machine_on is True:
    order = input(f"What would you like? ({menu.get_items()}):").lower()
    if order == "report":
        money_machine.report()
        coffee_maker.report()
    elif order == "off":
        machine_on = False
    elif order in menu.get_items():
        menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(menu.find_drink(order)) is True:
            money_machine.make_payment(menu.find_drink(order).cost)
            coffee_maker.make_coffee(menu.find_drink(order))
    else:
        print("Sorry that item is not available.")




















