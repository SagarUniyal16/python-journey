
"""
    items: A list of dictionaries, each representing a product with keys:
        - "name": str
        - "price": int
        - "category": str
    
    Returns:
        - List of names of affordable products (price < 500)
        - Set of unique categories
        - Dictionary of product name to price mapping
        - Generator expression converted to list of prices after applying 10% discount
"""



def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    items = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]

    # Write your code below this line
    price = [item["name"] for item in items if item["price"] < 500]
    unq_cat = {item["category"] for item in items}
    dict_name_price = {item["name"]: item["price"] for item in items}
    generated_prices = list(item["price"] * 0.9 for item in items)

    return price, unq_cat, dict_name_price, generated_prices

price_f, unq_cat_f, dict_name_price_f, generated_prices_f=filter_inventory([])
print(price_f, unq_cat_f, dict_name_price_f, generated_prices_f)