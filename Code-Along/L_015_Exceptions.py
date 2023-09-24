def input_int(promt = ''): #   = '' posibily to get an empty argument
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print('Input must be an integer..')
age = input_int('Input age:')
lenght = input_int('Input lenght:')            
weight = input_int('Input weight:')

print(f'age = {age}, lenght = {lenght}, weight = {weight}')

        