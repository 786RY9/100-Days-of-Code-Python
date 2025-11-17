import art
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b


def calculator():
    keep_calculating = True
    operations = {
        '+':add,
        '-':subtract,
        '*':multiply,
        '/':divide
    }

    print(art.logo)
    n1 = float(input("What's your first number: "))
    while keep_calculating:

        operation = input("""\n
                +\n
                -\n
                *\n
                /\n
Choose your operation from above: 
            """)

        n2 = float(input("What's your second number: "))

        res = operations[operation](n1,n2)
        print(f'Result: {res}')
        start_new = input("Type 'y' to continue using {res} for further operations, or 'n' to start new calculation: ")
        if start_new == 'y':
            n1 = res
            
            
        elif start_new == 'n':
            keep_calculating = False
            print('\n'*20)
            calculator()
            
        else:
            print('Bye!')
            keep_calculating = False
    
calculator()