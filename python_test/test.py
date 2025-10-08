my_cart=["apples","bananas","milk"]
print(my_cart)
my_cart.append("bread")
print(my_cart)
my_cart.insert(0,"ketchup")
print(my_cart)
my_cart.remove("bananas")
print(my_cart)
lenn=len(my_cart)
removed_item=my_cart[lenn-1]
print(removed_item)
my_cart.pop()
my_cart.extend(["rice","butter"])
print(my_cart)
my_cart.sort()
print(my_cart)
my_cart.reverse()
print(my_cart)
new_cart = my_cart + ["juice","jam"]
print(new_cart)
my_cart=my_cart*2
print(my_cart)
str= "tomato cucumber spinach"
str=str.split()
print(str)