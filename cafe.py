#create menu list
menu=["coffee", "tea","chicken_sandwich","croissant"]

#stock should contain the value of each item on the menu
stock= {"coffee": 70,
       "tea": 50,
       "chicken_sandwich": 60,
       "croissant": 40}

#Price should contain the dictionary for the price items

price= {"coffee":45,
       "tea":40,
       "chicken_sandwich": 35,
       "croissant": 30}
#*= multiply
total_stock= 0
for item in menu:
    item_value =(stock[item] * price[item])
    total_stock += item_value
    
#print result of the calculation
print(f"the total cafe stock R{total_stock}")

