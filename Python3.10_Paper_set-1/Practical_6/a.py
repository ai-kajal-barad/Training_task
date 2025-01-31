#a. Method to update the sale price with a given percentage.
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

print("BEFORE UPDATE",store)
def update_sale_price(store, shelf,product_name,month,per):
	if shelf in store and product_name in store[shelf]:
		if month in store[shelf][product_name]:
			cost_price=store[shelf][product_name][month]['cost_price']
			for cp in cost_price:
				sale_price=cp + cp * per/100
				store[shelf][product_name][month]['sale_price']=sale_price
			print(f"update Sale price is {sale_price}")
		else:
			print('Wrong input')

	else:
		print("SHELF or Product is not found") 
		
shelf=input("Please enter SHELF_1, SHELF_2 or SHELF_3:")
product=input("Enter Product_1, Product_2, Product_3 or Product_4: ")
month=input("Enter Month:")
percentage=int(input("Enter Percentage:"))	
call_sale_price=update_sale_price(store,shelf,product,month,percentage)	
print("AFTER UPDATE",store)	
