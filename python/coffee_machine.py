class CofeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = "Ready"


    def __repr__(self):
        return f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
{self.money} of money
{self.state} state"""


    def __str__(self):
        return f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
{self.money} of money
                        """

    def modify_water(self, delta_water):
        self.water += delta_water

    def modify_milk(self, delta_milk):
        self.milk += delta_milk

    def modify_coffee_beans(self, delta_coffee_beans):
        self.coffee_beans += delta_coffee_beans

    def modify_disposable_cups(self, delta_disposable_cups):
        self.disposable_cups += delta_disposable_cups

    def modify_money(self, delta_money):
        self.money += delta_money

    def buy_espresso(self):
        self.modify_water(-250)
        self.modify_coffee_beans(-16)
        self.modify_disposable_cups(-1)
        self.modify_money(4)

    def buy_latte(self):
        self.modify_water(-350)
        self.modify_milk(-75)
        self.modify_coffee_beans(-20)
        self.modify_disposable_cups(-1)
        self.modify_money(7)

    def buy_cappuccino(self):
        self.modify_water(-200)
        self.modify_milk(-100)
        self.modify_coffee_beans(-12)
        self.modify_disposable_cups(-1)
        self.modify_money(6)

    def check_resources(self, r_water, r_milk, r_coffee_beans):
        if r_water > self.water:
            print("Sorry, not enough water!")
            return False
        elif r_milk > self.milk:
            print("Sorry, not enough milk!")
            return False
        elif r_coffee_beans > self.coffee_beans:
            print("Sorry, not enough coffee beans!")
            return False
        elif self.disposable_cups <= 0:
            print("Sorry, not enough disposable cups!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            return True

    def buy(self, buy_option):
        # buy_option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if buy_option == 'back':
            return
        elif int(buy_option) == 1:
            if self.check_resources(250, 0, 16):
                self.buy_espresso()
        elif int(buy_option) == 2:
            if self.check_resources(350, 75, 20):
                self.buy_latte()
        else:
            if self.check_resources(200, 100, 12):
                self.buy_cappuccino()

    def fill_water(self, water):
        self.modify_water(int(water))

    def fill_milk(self, milk):
        self.modify_milk(int(milk))

    def fill_coffee_beans(self, coffee_beans):
        self.modify_coffee_beans(int(coffee_beans))

    def fill_disposable_cups(self, disposable_cups):
        self.modify_disposable_cups(int(disposable_cups))

    def take(self, money):
        self.modify_money(money * -1)
        print("I gave you $", money)

    def display(self):
        if self.state == "Ready":
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.state == "Buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif self.state == "FillWater":
            print("Write how many ml of water do you want to add:")
        elif self.state == "FillMilk":
            print("Write how many ml of milk do you want to add:")
        elif self.state == "FillCoffeeBeans":
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state == "FillCups":
            print("Write how many disposable cups of coffee do you want to add:")

    def command(self, input):
        if self.state == "Ready" and input == "buy":
            self.state = "Buy"
        elif self.state == "Buy":
            self.buy(input)
            self.state = "Ready"
        elif self.state == "Ready" and input == "fill":
            self.state = "FillWater"
        elif self.state == "FillWater":
            self.fill_water(input)
            self.state = "FillMilk"
        elif self.state == "FillMilk":
            self.fill_milk(input)
            self.state = "FillCoffeeBeans"
        elif self.state == "FillCoffeeBeans":
            self.fill_coffee_beans(input)
            self.state = "FillCups"
        elif self.state == "FillCups":
            self.fill_disposable_cups(input)
            self.state = "Ready"
        elif self.state == "Ready" and input == "remaining":
            print(self)
        elif self.state == "Ready" and input == "take":
            self.take(self.money)

coffee = CofeeMachine()

while True:
    coffee.display()
    action = input()
    if action == "exit":
        break
    else:
        coffee.command(action)
