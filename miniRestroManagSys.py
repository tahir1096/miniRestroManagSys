menu = {
    "Pizza": 1300,
    "Burger": 360,
    "Fries": 180,
    "Russian_Salad": 600,
    "Drink": 60,
    "Wings": 540,
    "Salad": 30,
}

print("Welcome to AL_MADINAH FAST FOOD")
print("================================")
print("Pizza : pkr = 1300\nBurger : pkr = 360\nFries : pkr = 180\nRussian_Salad : pkr = 600\nDrink : pkr = 60\nWings : pkr = 540\nSalad : pkr = 30\n")

order_total = 0

# First order
item_1 = input("Enter item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"You have successfully added {item_1}")
else:
    print("Sorry, we don't have this item in our menu.")

# Check for additional orders
while True:
    another_order = input("Do you want to order more items? (yes/no): ").strip().lower()
    if another_order == "yes":
        item_1 = input("Enter item you want to order : ")  # Ask for a new item each time
        if item_1 in menu:
            order_total += menu[item_1]
            print(f"You have successfully added {item_1}")
        else:
            print("Sorry, we don't have this item in our menu.")
    elif another_order == "no":
        print(f"Your total order is: {order_total} PKR")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
