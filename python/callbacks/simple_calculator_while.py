# https://pythonexamples.org/python-return-function/

def add(a, b):
    return a + b

def subs(a, b):
    return a - b

def mult(a, b):
    return a * b

def calculate(operation):
    if operation==1:
        return add
    elif operation==2:
        return subs
    elif operation==3:
        return mult

while True:
    print('Arithmetic operations')
    print('1.- addition')
    print('2.- substraction')
    print('3.- multiplication')
    print('0.- exit')
    operation = int(input('Select operation: '))
    if (operation not in [0, 1, 2, 3]):
        print("wrong number")
        break
    if operation==0:
        break
    func = calculate(operation)
    print('***')
    a = int(input('first operand'))
    b = int(input('second operand'))
    result = func(a, b)
    print('***')
    print('The result is: ', result)
