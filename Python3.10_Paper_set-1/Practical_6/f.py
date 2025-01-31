#f. Method to get the maximum or minimum price with the shelf name of a product.Display a proper message that shows the shelf and product.
store = {
    "SHELF_1": {
        "Product_1": {
            "January": {"cost_price": [10, 30, 45, 50], "sale_price": []},
            "February": {"cost_price": [60, 6, 4, 68], "sale_price": []},
        },
        "Product_2": {
            "January": {"cost_price": [66, 67, 81, 75], "sale_price": []},
            "February": {"cost_price": [78, 81, 85], "sale_price": []},
        },
        "Product_3": {
            "January": {"cost_price": [18, 20], "sale_price": []},
            "February": {"cost_price": [21, 22], "sale_price": []},
            "March": {"cost_price": [22, 23, 24], "sale_price": []},
        },
    },
    "SHELF_2": {
        "Product_1": {
            "January": {"cost_price": [206, 220, 225], "sale_price": []},
            "March": {"cost_price": [180, 170, 165], "sale_price": []},
            "April": {"cost_price": [160, 150, 136], "sale_price": []},
        },
        "Product_4": {
            "January": {"cost_price": [300], "sale_price": []},
            "February": {"cost_price": [280,300,385], "sale_price": []},
            "March": {"cost_price": [300, 385], "sale_price": []},
            "April": {"cost_price": [360, 376], "sale_price": []},
        },
    },
    "SHELF_3": {
        "Product_2": {
            "March": {"cost_price": [55, 59, 61], "sale_price": []},
            "April": {"cost_price": [53, 54, 55], "sale_price": []},
        },
        "Product_4": {
            "March": {"cost_price": [300], "sale_price": []},
            "April": {"cost_price": [360, 376], "sale_price": []},
        },
    },
}
def shelf_sale_price(store, shelf, percentage):
    if shelf in store:
        for product in store[shelf]:
            for month in store[shelf][product]:
            	cost_price=store[shelf][product][month]["cost_price"]
            	for cost in cost_price:
            		sale_price=cost + cost * per/100
            		store[shelf][product][month]["sale_price"] = sale_price
        print(f"Sale prices updated for {shelf}.")
    else:
        print(" Wrong input! Shelf not found.")

shelf=input("enter Shelf:")
per=int(input("enter percentage:"))
shelf_sale_price(store,shelf,per)

def get_price_info(store, product_name, price_type="max"):
    price_func = max if price_type == "max" else min
    best_price = None
    best_shelf = None

    for shelf, products in store.items():
        if product_name in products:
            for month in products[product_name]:
                for price in products[product_name][month]["cost_price"]:
                    if best_price is None or price_func(price, best_price) == price:
                        best_price = price
                        best_shelf = shelf

    if best_price is not None:
        print(f"The {price_type.upper()} price of '{product_name}' is {best_price} on {best_shelf}.")
    else:
        print(f"Product '{product_name}' not found in any shelf.")

product=input("enter Product:")
max_min=input("enter max or min:")
get_price_info(store, product, max_min) 
