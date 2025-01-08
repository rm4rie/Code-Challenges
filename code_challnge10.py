x = 5  

# Upper part of the diamond
for f in range(1, x + 1):
    print(" " * (x - f), end="")  
    print("* " * f)               

# Lower part of the diamond
for s in range(x - 1, 0, -1):
    print(" " * (x - s), end="") 
    print("* " * s)              