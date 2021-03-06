# Makes 3 different coffee recipes: Expresso, Latte, Cappuccino 
# The machine holds the following resources: 300 ml water, 200 ml coffee, and 100 g sugar
# Cost - using American coins quarter, dime, nickel, and penny
# Print a report about the resources left

MENU = {
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#4 Check if there are sufficient resources left to make each order as it is
#placed. If not, tell user their order cannot be made. If so, proceed to
#payment.
def enough_resources(need_ingredients):
	for item in need_ingredients:
		if need_ingredients[item] > resources[item]:
			print("Sorry there is not enough {item}. ")
			return False
	return True

#5 Process payment (payment comes in the form of coins only) 
def receive_payment():
	print("You selected {user_order}. Your total is ${profit}. Please insert coins.")
	total = int(input("How many quarters?: ")) * 0.25
	total += int(input("How many dimes?: ")) * 0.10
	total += int(input("How many nickels?: ")) * 0.05
	total += int(input("How many pennies?: ")) * 0.01
	return total

#6 Check if the user entered enough money to purchase their coffee order.
def check_payment(coins_inserted, cost):
	if coins_inserted >= cost:
		change = round(coins_inserted - cost, 2)
		print(f"Your change is ${change}.")
		global profit
		profit += cost
		return True
	else:
		print("I'm sorry that is not enough money. Your money has been refunded.")
		return False

#7 Make coffee order and deduct what is used from the available resources as well as add funds to the money category
#8 Tell the user "Here is your (drink name). Enjoy!"
def make_order(drink_name, order_ingredients):
	for item in order_ingredients:
		resources[item] -= order_ingredients[item]
		print("Here is your {drink_name}. ☕ Enjoy!")

#1 Prompt user by asking "What would you like? Expresso, Latte, or Cappuccino: "
#2 Turn off Coffee Machine by entering "off" to the prompt
#3 Print report of resources currently in the machine (i.e. water, milk, coffee, and money)
is_on = True

while is_on:
	user_order = input("What would you like? expresso, latte or cappucino: ")
	if user_order == "off":
		is_on = False
	elif user_order == "report":
		print(f"Water: {resources['water']}ml")
		print(f"Milk: {resources['milk']}ml")
		print(f"Coffee: {resources['coffee']}g")
		print(f"Money: ${profit}")
	else:
		drink = MENU[user_order]
		if enough_resources(drink["ingredients"]):
			payment = process_coins()
			if check_payment(payment, drink["cost"]):
				make_order(user_order, drink["ingredients"])


