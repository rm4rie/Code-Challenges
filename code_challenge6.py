age = int(input("Enter your age: "))

if age < 0:
    category = "Invalid age"
elif age <= 8:
    category = "Toddler"
elif age <= 14:
    category = "Preteen"
elif age <= 18:
    category = "Teenager"
elif age <= 27:
    category = "Early Adult"
elif age <= 44:
    category = "Middle Adult"
elif age <= 59:
    category = "Past Adult"   
else:
    category = "Senior"

print(f"You are a {category}.")