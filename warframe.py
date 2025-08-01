import json
from tabulate import tabulate
with open("warframe.json") as e:
    e = json.load(e)

customers = e["customers"]
products = e["products"]

TIP = 0
TC = 0
TP = 0

for c in customers:
    count1 = 0
    items = []
    name = c["name"]
    subtotal = 0
    discount = c["discount"]
    discount_amount = 0
    for o in c["orders"]:
        if o > 0:
            item_name = products[count1]["name"]
            item_type = products[count1]["type"]
            price = products[count1]["price"]
            discounted_price = round((discount / 100) * (price * o), 2)
            if item_type == "Platinum" and discount > 0:
                subtotal += discounted_price
                discount_amount += discounted_price
            else:
                subtotal += round(price * o, 2)
            items.append({
                "Item Purchased":item_name,
                "Price": price,
                "Quantity": o,
                "Type of Item": item_type,
                "Total Item Price": round(price * o, 2)
            })
            TIP += o
        count1 += 1
    TC += 1
    taxed_amount = round(subtotal * 0.06, 2)
    total = round(subtotal * 1.06, 2)
    profit = round(subtotal * 0.7, 2)
    TP += profit
    print(name)
    print(tabulate(items, headers="keys", tablefmt="grid"))
    print(f"The Platinum was discounted by {discount}%, to remove a total of ${discount_amount} from the subtotal")
    print(f"The Subtotal was: ${subtotal}")
    print(f"The amount Digital Extremes Profited off of the order was: ${profit}")
    print(f"The tax of 6% increases the order total by ${taxed_amount}")
    print(f"The total for the order came out to: ${total}")
print()
print()
print(f"Total Items Purchased: {TIP}")
print(f"Total Customers: {TC}")
print(f"Total Profit: ${TP}")