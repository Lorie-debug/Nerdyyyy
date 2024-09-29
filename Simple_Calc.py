num1 = int(input('enter your first num: '))
num2 = int(input('enter your second num: '))
operator = input('Choose an operator(+ - / * % // ** ): ')

if operator == '+':
    result = num1 + num2
    print(f'{num1} + {num2} is equal to {result}')

elif operator == '-':
    result = num1 - num2
    print(f'{num1} - {num2} is equal to {result}')

elif operator == '/':
    result = num1 / num2
    print(f'{num1} + {num2} is equal to {result:.2f}')

elif operator == '*':
    result = num1 * num2
    print(f'{num1} * {num2} is equal to {result}')

elif operator == '%':
    result = num1 % num2
    print(f'{num1} % {num2} is equal to {result}')

elif operator == '//':
    result = num1 // num2
    print(f'{num1} // {num2} is equal to {result}')

elif operator == '**':
    result = num1 ** num2
    print(f'{num1} + {num2} is equal to {result}')

else:
    print('The operator is invalid {operator}')