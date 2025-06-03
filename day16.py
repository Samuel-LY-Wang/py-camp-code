#Coffee Machine class
class CoffeeMachine():
    def __init__(self):
        self.drinks = {
            'espresso': {'water': 50, 'coffee': 18, 'milk': 0, 'cost': 1.5},
            'latte': {'water': 200, 'coffee': 24, 'milk': 150, 'cost': 2.5},
            'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100, 'cost': 3.0}
        }
        self.inventory = {'water': 2000, 'milk': 500, 'coffee': 100, 'money': 0.0}
        self.valid_options = ['espresso', 'latte', 'cappuccino', 'report', 'refill', 'off']
    def report(self):
        print("Water: {}ml".format(self.inventory['water']))
        print("Milk: {}ml".format(self.inventory['milk']))
        print("Coffee: {}g".format(self.inventory['coffee']))
        print("Money: ${:.2f}".format(self.inventory['money']))
    def refill(self):
        water = int(input("How much water to add? (ml) "))
        milk = int(input("How much milk to add? (ml) "))
        coffee = int(input("How much coffee to add? (g) "))
        self.inventory['water'] += water
        self.inventory['milk'] += milk
        self.inventory['coffee'] += coffee
        print("Inventory refilled.")
    def check_resources(self, drink):
        if self.inventory['water'] < drink['water']:
            print("Not enough water. Please refill.")
            return False
        if self.inventory['milk'] < drink['milk']:
            print("Not enough milk. Please refill.")
            return False
        if self.inventory['coffee'] < drink['coffee']:
            print("Not enough coffee. Please refill.")
            return False
        return True
    def process_payment(self, drink):
        print("Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total = quarters + dimes + nickels + pennies
        if total < drink['cost']:
            print("Not enough money. Please insert more coins.")
            return False
        else:
            self.inventory['money'] += drink['cost']
            change = total - drink['cost']
            if change > 0:
                print("Here is your change: ${:.2f}".format(change))
            return True
    def make_coffee(self, command):
        drink = self.drinks[command]
        if not self.check_resources(drink):
            return False
        if not self.process_payment(drink):
            return False
        print("Making your {}...".format(command))
        self.inventory['water'] -= drink['water']
        self.inventory['milk'] -= drink['milk']
        self.inventory['coffee'] -= drink['coffee']
        print("Here is your {}. Enjoy!".format(command))

machine=CoffeeMachine()
while True:
    command = input("What would you like? Espresso, Latte, or Cappuccino?").lower()
    if command not in machine.valid_options:
        print("Invalid option. Please try again.")
        continue
    if command == 'off':
        exit()
    if command == 'report':
        machine.report()
        continue
    if command == 'refill':
        machine.refill()
    else:
        machine.make_coffee(command)