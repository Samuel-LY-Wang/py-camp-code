#Simple coffee machine
drinks = {'espresso': {'water': 50, 'coffee': 18, 'milk': 0, 'cost': 1.5},
          'latte': {'water': 200, 'coffee': 24, 'milk': 150, 'cost': 2.5},
          'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100, 'cost': 3.0}
          }
inventory = {'water': 2000, 'milk': 500, 'coffee': 100, 'money': 0.0}
validoptions = ['espresso', 'latte', 'cappuccino', 'report', 'refill', 'off']
while True:
    command=input("What would you like? Espresso, Latte, or Cappucino?")
    command = command.lower()
    if command not in validoptions:
        print("Invalid option. Please try again.")
        continue
    if command == 'off':
        exit()
    if command == 'report':
        print("Water: {}ml".format(inventory['water']))
        print("Milk: {}ml".format(inventory['milk']))
        print("Coffee: {}g".format(inventory['coffee']))
        print("Money: ${}".format(inventory['money']))
        continue
    if command == 'refill':
        water= int(input("How much water to add? (ml) "))
        milk = int(input("How much milk to add? (ml) "))
        coffee = int(input("How much coffee to add? (g) "))
        inventory['water'] += water
        inventory['milk'] += milk
        inventory['coffee'] += coffee
        print("Inventory refilled.")
    else:
        drink = drinks[command]
        if inventory['water'] < drink['water']:
            print("Not enough water. Please refill.")
            continue
        if inventory['milk'] < drink['milk']:
            print("Not enough milk. Please refill.")
            continue
        if inventory['coffee'] < drink['coffee']:
            print("Not enough coffee. Please refill.")
            continue
        print("Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total = quarters + dimes + nickels + pennies
        if total < drink['cost']:
            print("Not enough money. Please insert more coins.")
            continue
        else:
            inventory['water'] -= drink['water']
            inventory['milk'] -= drink['milk']
            inventory['coffee'] -= drink['coffee']
            inventory['money'] += drink['cost']
            change = total - drink['cost']
            if change > 0:
                print("Here is your change: ${:.2f}".format(change))
            print("Here is your {}. Enjoy!".format(command))