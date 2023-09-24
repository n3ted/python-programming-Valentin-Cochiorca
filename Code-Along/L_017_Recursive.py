def main( ):
    print('Start of main()')

    func_b()

    func_a()

    func_b()

    print('End of main()')

def func_a():
    print('Start of a()')

    #func_b()

    print('End of a()')

def func_b():
    print('Start of b()')

    #func_a()

    print('End of b()')


def print_hello_recursive(n):
    print('Hello')
    if n > 1: print_hello_recursive(n - 1)
    return
print_hello_recursive(4)
func_a()
main()
