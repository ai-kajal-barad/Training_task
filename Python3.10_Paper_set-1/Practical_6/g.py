#g. Define the method and display the Average cost and a sale also profit based on the shelf for a specific month.
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

def avg_shelf(store,shelf,month):
	total_cost=0
	total_sale=0
	total_item=0
	if shelf in store:
		for product,product_data in store[shelf].items():
			cost_price = product_data[month]['cost_price']
			sale_price = product_data[month]['sale_price']
			total_cost += sum(cost_price)
			total_sale += sum(sale_price)
			total_item += len(cost_price)
		if total_item > 0:
			avg_cost = total_cost/total_item
			avg_sale = total_sale/total_item
			profit = total_sale - total_cost
			print(f'average cost of shelf:{shelf} and month:{month}={avg_cost}')
			print(f'average sale of shelf:{shelf} and month:{month}={avg_sale}')
			print(f'Profit of shelf:{shelf} and month:{month}={profit}')
		else:
			print("No data found")
	else:
		print("No shelf found")
			
shelf=input("Enter shelf:")
month=input("Enter Month:")						
avg_shelf(store,shelf,month)
