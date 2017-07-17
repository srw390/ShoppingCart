import code
import datetime
# List of Products at Mall
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # Products based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

choices = True
sel = []
while choices:
    data = input("Please input a product identifier, or 'Done' if there are no more items: ")
    try:
        valid = int(data)
    except ValueError:
        #code.interact(local=locals())
        if data != 'Done':
            print ("Invalid input, it should be an integer or 'Done'")
            continue
    #code.interact(local=locals())
    if data == 'Done':
        choices = False
    elif int(data) not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
        print('Invalid input, valid inputs from 1 to 20')
    else:
        sel.append(int(data))

print ("---------------------------")
print ("Fresh and Frozen Foods")
print ("---------------------------")
print ("Web: " + "www.FreshFrozenFoods.com")
print ("Phone: " + "973 102 2124")
print ("Time: " + str(datetime.datetime.now()))
print ("---------------------------")
print ("Shopping Cart Items: ")

items = {}

for p in products:
    #Dictionary of each item id
    items.update({p.get("id"):{"name":p.get("name"), "price":p.get("price")}} )
#code.interact(local=locals())
price = 0.0
for s in sel:
    tmp = items.get(s)
    price = price + tmp.get("price")
    print ("+" +  tmp.get("name") + "($" + "{:.2f}".format(tmp.get("price")) + ")")

print ("---------------------------")
print ("Subtotal: " + "$" + "{:.2f}".format(price))
tax = 0.0875*price
print ("Plus NYC Sales Tax (8.875%): " + "$" + "{:.2f}".format(tax))
print ("Total: " + "{:.2f}".format(tax + price))
print ("---------------------------")
print ("Thanks for your business! Please come again.")
