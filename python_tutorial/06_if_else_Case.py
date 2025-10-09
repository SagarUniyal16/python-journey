available_snack = ["cookies","samosa"]
snack=input("Enter your snack: ").lower()

print(f"User said : {snack}")

if(snack in available_snack):
    print("Order is confirmed")
else:
    print("Order not available")


available_drinks={"small":10,"medium":15,"large":20}

drink_choice=input("enter you drink choice: ").lower()

if(drink_choice in available_drinks):
    print(f"The price of your drink is : {available_drinks[drink_choice]}")
else:
    print("drink not available")
    

order_amount=int(input("Enter the amount :"))

if(order_amount>300):
    print("Delivery is free")
else:
    print("Delivery fee is Rs.30")
    
delivery_fees=0 if order_amount>300 else 30
print(f"Delivery fees is: {delivery_fees}")

seat_type=input("Enter your seat type -> Sleeper/AC/General/Luxury: ")

match seat_type:
    case "sleeper":
        print("No AC, beds are available")
    case "ac":
        print("Air Conditioned, comfy ride")
    case "general":
        print("Cheapest Option")
    case "luxury":
        print("Luxury-premium seats with meal")
    case _:
        print("invalid seat type")
        


employees = {
    "Sagar": {
        "age": 25,
        "salary": 50000,
        "designation": "Software Engineer"
    },
    "Karan": {
        "age": 28,
        "salary": 65000,
        "designation": "Senior Developer"
    },
    "Amit": {
        "age": 30,
        "salary": 70000,
        "designation": "Data Engineer"
    },
    "Raj": {
        "age": 26,
        "salary": 55000,
        "designation": "Backend Developer"
    }
}

print(f"Age of Sagar is: {employees["Sagar"]["age"]}")