chai_items=["Iced Tea","Ginger Tea","Black Tea","Masala Tea","Iced Latte Tea"]

iced_tea=[tea for tea in chai_items if "Iced" in tea]
print(iced_tea)

favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais }
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)
