my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}

print(type(my_set))   # <class 'set'>
print(type(my_dict))  # <class 'dict'>

#how to declare empty set and dictionary
s1={}
s2=set()
print(type(s1))  # <class 'dict'>
print(type(s2))  # <class 'set'>


chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(chai_order)
print(f"Removed last item: {last_item}")

d = {'x': 1, 'y': 2, 'z': 3}

print(d.pop('y'))      # ➜ 2
print(d.popitem())     # ➜ ('z', 3)
print(d)               # ➜ {'x': 1}

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}")

customer_note_2 = chai_order.get("note", "NO Note")
print(f"customer_note is: {customer_note_2}")



users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80,  "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "P50": (0.5, 0),
    "F10": (0, 10),
}

discount_price_dict={}

for user in users:
    total_price=user["total"]
    # discount_percent=discounts[user["coupon"]][0]
    # discount_flat=discounts[user["coupon"]][1]
    discount_percent,discount_flat=discounts.get(user["coupon"],(0,0))
    discounted_price=total_price-(discount_percent*total_price) -discount_flat
    print(f"Price after discount for user with id {user["id"]} is: {discounted_price}")
    discount_price_dict[user["id"]]=discounted_price

print(discount_price_dict)


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
    
