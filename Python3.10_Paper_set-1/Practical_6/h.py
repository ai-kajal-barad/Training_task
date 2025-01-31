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
'''
#h. Display the Average cost and sales also profit based on the product for a specificmonth.

def avg_shelf(store,shelf,product,month):
	total_cost=0
	total_sale=0
	total_item=0
	if shelf in store:
		for shelf,shelf_data in store.items():
			if product in store[shelf]:
				product_data=store[shelf][product]
				cost_price = product_data[month]['cost_price']
				sale_price = product_data[month]['sale_price']
				total_cost += sum(cost_price)
				total_sale += sum(sale_price)
				total_item += len(cost_price)
		if total_item > 0:
			avg_cost = total_cost/total_item
			avg_sale = total_sale/total_item
			profit = total_sale - total_cost
			print(f'average cost of product:{product} and month:{month}={avg_cost}')
			print(f'average sale of product:{product} and month:{month}={avg_sale}')
			print(f'Profit of product:{product} and month:{month}={profit}')
		else:
			print("No data found")
	else:
		print("No shelf found")
			
			
call=avg_shelf(store,'SHELF_1','January','Product_1')'''
def get_product_summary(store, product_name, month):
    total_cost = 0
    total_sale = 0
    count = 0

    for shelf, products in store.items():
        if product_name in products and month in products[product_name]:
            cost_prices = products[product_name][month]["cost_price"]
            sale_prices = products[product_name][month]["sale_price"]

            if cost_prices:
                total_cost += sum(cost_prices)
                count += len(cost_prices)
            
            if sale_prices:
                total_sale += sum(sale_prices)

    if count == 0:
        print(f"No data found for '{product_name}' in {month}.")
        return

    avg_cost = round(total_cost / count, 2)
    avg_sale = round(total_sale / count, 2) if total_sale > 0 else 0
    profit = round(avg_sale - avg_cost, 2)

    print(f" Summary for '{product_name}' in {month}:")
    print(f"   - Average Cost Price: {avg_cost}")
    print(f"   - Average Sale Price: {avg_sale}")
    print(f"   - Profit per unit: {profit}")

product=input("enter Product:")
month=input("enter Month:")
get_product_summary(store, product, month)  


