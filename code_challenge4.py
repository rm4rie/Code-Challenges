name = input("enter your name: ") 
maneh1 = eval(input("Enter your deposit: ")) 
print("Hi!",name, " your deposit amount breakdown in PH denominator is as follow")

maneh2 = maneh1 // 1000 
maneh3 =  maneh1 % 1000
print(maneh2, "1000")

maneh4 = maneh3 // 500 
maneh5 = maneh3 % 500
print(maneh4, "500")

maneh6 = maneh5 // 200
maneh7 = maneh5 % 200
print (maneh6, "200")

maneh8 = maneh7 // 100 
maneh9 = maneh7 % 100

maneh10 = maneh9 // 50
maneh11 = maneh9 % 50
print(maneh8, 100)
print(maneh10, "50")

maneh12 = maneh11 // 20 
maneh13 = maneh11 % 20

maneh14 = maneh13 // 10 
maneh15 = maneh13 % 10   
 
maneh16 = maneh15 //5
maneh17 = maneh15 % 5

maneh18 = maneh17 // 1 
missu19 = maneh17 % 1
print(maneh12, "20") 
print(maneh14, "10") 
print(maneh16, "5")
print(maneh18, "1")