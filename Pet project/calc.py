calc = 'calc.py'

while True:
    what = input('whats doing? (+, -, *, /): ')

    if what == "+":
        a = int(input("choose first number: "))
        b = int(input("choose second number: "))
        c = a + b
        print('result : ', c)
    elif what == "-":
        a = int(input("choose first number: "))
        b = int(input("choose second number: "))
        c = a - b
        print('result : ', c)
    elif what == "*":
        a = int(input("choose first number: "))
        b = int(input("choose second number: "))
        c = a * b
        print('result : ', c)
    elif what == "/":
        a = int(input("choose first number: "))
        b = int(input("choose second number: "))
        c = a / b
        print('result : ', c)
    elif what == "%":
        a = int(input("choose first number: "))
        b = int(input("choose second number: "))
        c = a % b
        print('result : ', c)
    elif what == "**":
        a = int(input("choose first number: "))
        b = int(input("choose second number: "))
        c = a ** b
        print('result : ', c)
    elif what == "//":
        a = int(input("choose first number: "))
        b = int(input("choose second number: "))
        c = a // b
        print('result : ', c)
    else:
        print('ERROR!')
