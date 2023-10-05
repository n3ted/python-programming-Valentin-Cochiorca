# Module = one py file 
# Package = few py files
import math 

# We can have many functions or a class in module 
# Create main() and exe function or execute directly 

def main():
    for i in range(5):
        print(f'{i} = {square(i)}')

def square(n):
    return n * n 

def sqrt(n):
    return math.sqrt

# print('Hello world')
# for i in range(5):
#     print(square(i))

# print(__name__) # if local = __main / if imported = module name 

if __name__ == '__main__': # way to call a function whit the name 
    main()   # in the test unit will not be called (diff name)


# A module can import another module 