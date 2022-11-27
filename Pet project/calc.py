calc = 'calc.py'

while True:
    what = input( ' whats doing? (+, -, *, /): ')

    if what == "+":
        a = float(input("choose first number: "))
        b = float(input("choose second number: "))
        c = a + b
        print('result : ' + str(c).rstrip('.0'))
    elif what == "-":
        a = float(input("choose first number: "))
        b = float(input("choose second number: "))
        c = a - b
        print('result : ' + str(c).rstrip('.0'))
    elif what == "*":
        a = float(input("choose first number: "))
        b = float(input("choose second number: "))
        c = a * b
        print('result : ' + str(c).rstrip('.0'))
    elif what == "/":
        a = float(input("choose first number: "))
        b = float(input("choose second number: "))
        c = a / b
        print('result : ' + str(c).rstrip('.0'))
    elif what == "%":
        a = float(input("choose first number: "))
        b = float(input("choose second number: "))
        c = a % b
        print('result : ' + str(c).rstrip('.0'))
    elif what == "**":
        a = float(input("choose first number: "))
        b = float(input("choose second number: "))
        c = a ** b
        print('result : ' + str(c).rstrip('.0'))
    elif what == "//":
        a = float(input("choose first number: "))
        b = float(input("choose second number: "))
        c = a // b
        print('result : ' + str(c).rstrip('.0'))
    else:
        print('ERROR!')
