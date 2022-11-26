# Pizza Menu order sliced up
#from typing import Concatenate


import datetime
now = datetime.datetime.now()

print("Time: " + now.strftime("%H:%M:%S"))
print("--------------\nSLICED UP - PIZZERIA\n--------------")


def GetGST(amount):
    return round(amount * .1,2)

def GetSize():
    validOptions = ["s","m","l"]

    isOk = False
    while (not isOk):
        _given = input("\nWhat size of pizza will you like to order?  S, M, L :\nMake your selection: ").lower()
        if(_given in validOptions):
            return _given
        else:
            print("***\nThat is not a valid size - please select from: S, M, L\n***")

def GetToppings():
    validOptions = ["1", "2", "3", "4", "5"]

    isOk = False
    while (not isOk):
        _given = input("""What type of pizza would you like:
        1. Cheese
        2. Garlic
        3. Supreme
        4. Spicy Jalapeno
        5. Super Pepperoni
        Make your selection: """).lower()

        if(_given in validOptions):
            return int(_given)
        else:
            print("***\nThat is not a valid pizza type, please select from: 1, 2, 3, 4, 5\n***")

def GetDrink():
    validOptions = ["1", "2", "3", "4", "5"]

    isOk = False
    while (not isOk):
        _given = input("""Please select your drink:
        1. Coca-Cola
        2. Coca-Cola - No Sugar
        3. Water
        4. Fanta
        5. None
        Make your selection: """).lower()

        if(_given in validOptions):
            return int(_given)
        else:
            print("***\nthat is not a valid drink, please select from: 1, 2, 3, 4, 5\n***")




#size = input("What size of pizza will you like to order?  S, M, L : ").lower
#pizzatype = input("= = = = = = = = == \nWhat pizza do you want to order? \n 1. Cheese \n 2. Garlic \n 3. Supreme \n 4. Spicy jala \n : ").lower
#drink = input("= = = = = = = = \nselect your drink of choice \n 1. coke \n 2. Coke zeror \n 3. Bottle water \n : ").lower

subTotal = 0



#totalgst = total * GST
#finalcost =  total + totalgst

# size selection
size = GetSize()

if size == "s":
    subTotal += 9.95
    print("1x Small -")
elif size == "m":
    subTotal += 14.95
    print("1x Medium -")
elif size == "l":
    subTotal += 19.95
    print("1x Large -")
else:
    print("That is not a valid size")
    #exit(100)
    #program should end

# pizza toppings
pizzatype = GetToppings()

if pizzatype == 1:
    subTotal += 5.95
    print("added - Just Cheese")
elif pizzatype == 2:
    subTotal += 5.95
    print("added - Garlic cheese")
elif pizzatype == 3:
    subTotal += 9.95
    print("added - Supreme")
elif pizzatype == 4:
    subTotal += 7.5
    print("added = Spicy Jalapeno")
elif pizzatype == 5:
    subTotal += 8
    print("added - Super pepperoni")

else:
    print("Not a valid pizza type")
    #exit(100)

# Drink selection
drink = GetDrink()

if drink == 1:
    subTotal += 2.49
    print("1x Coca-Cola")
elif drink == 2:
    subTotal += 2.49
    print("1x CokE No-Sugar")
elif drink == 3:
    subTotal += 1.59
    print("1x Bottle water")
elif drink == 4:
    subTotal += 2.49
    print("Added Fanta")
elif drink == 5:
    subTotal = subTotal
    print("No drink selected")

else:
    print("That is not a valid drink")


subTotal = round(subTotal,2)
total = round(subTotal + GetGST(subTotal))
gst = GetGST(subTotal)
# Total oweing
print(" \n************************************* ")
print(f"Size:{size.upper()} , Pizza:{pizzatype}, Drink:{drink}")

#print(round(subTotal + GetGST(subTotal)),2)l
print("----------------")
print(f"${total} + {GetGST(subTotal)} GST")
print("----------------")
print(f"TOTAL: ${total + gst}")



