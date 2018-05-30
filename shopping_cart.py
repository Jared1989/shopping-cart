import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": 0},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": 0},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": 0},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": 0},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": 0},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": 0},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": 0},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": 0},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": 0},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": 0},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": 0},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": 0},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": 0},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": 0},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": 0},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": 0},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": 0},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": 0},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": 0},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": 0},
    {"id":21, "name": "Professor Rossetti's Bananas", "department": "snacks", "aisle": "ice cream toppings", "price": 0.79, "price_per": 1}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def search(id):
    for p in products:
        if p["id"] == id:
            return True
    return False

def search2(id):
    no_lbs = 0
    for p in products:
        if p["id"] == id:
            if p["price_per"] != 0:
                no_lbs = input("Please input the number of pounds: ")
    return no_lbs

product_ids = []
pounds = []
while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if product_id == "DONE":
        break
    if product_id.isdigit():
        if not search(int(product_id)):
            print("Hey, are you sure that product identifier is correct? Please try again!")
        else:
            weight = search2(int(product_id))
            product_ids.append(int(product_id))
            New_Value = {"id":int(product_id),"price_per":weight}
            pounds.append(New_Value)

def matching_product(product_identifier):
    products_list = [p for p in products if p["id"] == product_identifier]
    return products_list[0]

def matching_product2(product_identifier):
    for p in pounds:
        if p["id"] == product_identifier:
            return p["price_per"]

print("-------------------------------")
print("MY GROCERY STORE")
print("-------------------------------")
print("Web: www.mystore.com")
print("Phone: 1.123.456.7890")
print("Checkout Time: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S"))

print("-------------------------------")
print("Shopping Cart Items:")

raw_total = 0

for pid in product_ids:
    product = matching_product(pid)
    price_dollar = ' (${0:.2f})'.format(product["price"])
    if product["price_per"] == 0:
        raw_total += product["price"]
        print("+" + " " + product["name"] + " " + price_dollar)
    else:
        lbs = matching_product2(pid)
        raw_total += product["price"] * float(lbs) 
        print("+" + " " + product["name"] + " " + str(lbs) + " pounds @" + price_dollar + " per pound")

print("-------------------------------")
print("Subtotal:", '${0:.2f}'.format(raw_total))
total_tax = raw_total * 0.08875
print("Plus NYC Sales Tax (8.875%):", '${0:.2f}'.format(total_tax))
grand_total = raw_total + total_tax
print("Total:", '${0:.2f}'.format(grand_total))

print("-------------------------------")
print("Thanks for your business! Please come again.")


from datetime import datetime
filename=datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'.txt'
f=open(filename,'w')

f.write("-------------------------------\r\n")
f.write("MY GROCERY STORE\r\n")
f.write("-------------------------------\r\n")
f.write("Web: www.mystore.com\r\n")
f.write("Phone: 1.123.456.7890\r\n")
f.write("Checkout Time: " + datetime.now().strftime("%Y-%m-%d %H:%m:%S") + "\r\n")

f.write("-------------------------------\r\n")
f.write("Shopping Cart Items:\r\n")

raw_total = 0

for pid in product_ids:
    product = matching_product(pid)
    price_dollar = ' (${0:.2f})'.format(product["price"])
    if product["price_per"] == 0:
        raw_total += product["price"]
        f.write("+" + " " + product["name"] + " " + price_dollar + "\r\n")
    else:
        lbs = matching_product2(pid)
        raw_total += product["price"] * float(lbs) 
        f.write("+" + " " + product["name"] + " " + str(lbs) + " pounds @" + price_dollar + " per pound" + "\r\n")


f.write("-------------------------------\r\n")
f.write("Subtotal: " + '${0:.2f}'.format(raw_total) + "\r\n")
total_tax = raw_total * 0.08875
f.write("Plus NYC Sales Tax (8.875%): " + '${0:.2f}'.format(total_tax) + "\r\n")
grand_total = raw_total + total_tax
f.write("Total: " + '${0:.2f}'.format(grand_total) + "\r\n")

f.write("-------------------------------\r\n")
f.write("Thanks for your business! Please come again.\r\n")

f.close()
