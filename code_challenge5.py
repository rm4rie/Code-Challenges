#Grading decision

name = input("Please enter your name: ")
grade = float(input("Please input your grade: "))

os = 90 - 100
vs = 85 - 89
s = 80 - 84
o = 75-79
f = 74 

#passed = 75
#failed = 74 

if grade > 75:
    print("Good job! You passed!")

else:
    print("You failed. Better luck next time!")
