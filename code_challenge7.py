name = input("Please enter your name: ")
print(f"Hi {name}! Welcome to our store!")

print(" **MEAT** \n pork = 300 \n chicken = 220 \n beef = 450")
print(" **DRY GOODS** \n cereal = 120 \n coffee = 70 \n sugar = 70 \n instant noodles = 30")

pur = input("Did you purchased a grocery today? (yes/no): ")
yes = "proceed"

if pur == yes: 
    print("Okay, thank you! Let's proceed!")
else: 
    print("Thank you for visiting our store! :)")

order = input("What did you purchased? ")

#def item_catgorized(name, price, quantity):