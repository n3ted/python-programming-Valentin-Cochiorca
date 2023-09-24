# In python we have 2 types of scope (life-time of a variable):
# 1. LOCAL SCOPE: Only available in a function.
# 2. GLOBAL SCOPE: Available through execution of a program.

name = 'Valle'

def main():
    
    global name # makes variable global
    name = 'Rey'


print(name)

main() # call function and change glabal var

print(name) # get the new global var from the function 


# Python doesn't have block scope, in comparison whit othe languages.
# if name == "Valle":
#       last_name = "Cochiorca"

# print(last_name)

# for i in range(3):
#       print(i)

# print(f"i = {i}")